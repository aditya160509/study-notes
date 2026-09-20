from __future__ import annotations

import math
import os
from pathlib import Path
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle, Arc, Polygon
from matplotlib.lines import Line2D
import schemdraw
import schemdraw.elements as elm

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    Image,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path('/Users/adityabalaji/Documents/Codex')
OUT = ROOT / 'output' / 'pdf' / 'physics'
DIAG = OUT / 'paper5-electricity-diagrams'
OUT.mkdir(parents=True, exist_ok=True)
DIAG.mkdir(parents=True, exist_ok=True)

NAVY = '#10243e'
BLUE = '#0b9fe3'
GOLD = '#f0a51a'
INK = '#172234'
MUTED = '#61738d'
PALE = '#eef5fa'
PALE_BLUE = '#e3f5fd'
RED = '#cf4b4b'
GRID = '#ccd5df'


def savefig(fig, name: str):
    fig.savefig(DIAG / f'{name}.png', dpi=320, bbox_inches='tight', facecolor='white')
    fig.savefig(DIAG / f'{name}.svg', bbox_inches='tight', facecolor='white')
    plt.close(fig)


def schem_png(name: str, build, dpi: int = 320):
    """Render a circuit with SchemDraw, preserving textbook symbols and wire topology."""
    with schemdraw.Drawing(show=False) as drawing:
        build(drawing)
        drawing.save(DIAG / f'{name}.png', dpi=dpi)
        drawing.save(DIAG / f'{name}.svg')
    return DIAG / f'{name}.png'


def setup(title: str, subtitle: str = ''):
    fig, ax = plt.subplots(figsize=(12, 6.6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.6)
    ax.axis('off')
    fig.subplots_adjust(0, 0, 1, 1)
    ax.text(6, 6.30, title, ha='center', va='center', fontsize=19, weight='bold', color=NAVY)
    if subtitle:
        ax.text(6, 5.93, subtitle, ha='center', va='center', fontsize=10.5, color=MUTED)
    return fig, ax


def wire(ax, pts, color=INK, lw=2.4, ls='-'):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, solid_capstyle='round', solid_joinstyle='round')


def box(ax, x, y, w, h, text, fc=PALE, ec=INK, fs=11, color=INK, radius=0.12, weight='normal'):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0.04,rounding_size={radius}',
                       facecolor=fc, edgecolor=ec, linewidth=1.8)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs, color=color, weight=weight)


def resistor(ax, x1, y, x2, amp=0.18, n=6, color=INK, lw=2.4):
    lead = 0.18
    wire(ax, [(x1, y), (x1 + lead, y)], color=color, lw=lw)
    wire(ax, [(x2 - lead, y), (x2, y)], color=color, lw=lw)
    left, right = x1 + lead, x2 - lead
    pts = [(left, y)]
    dx = (right - left) / (2 * n)
    for i in range(1, 2 * n + 1):
        pts.append((left + i * dx, y + amp * (1 if i % 2 else -1)))
    wire(ax, pts, color=color, lw=lw)


def capacitor(ax, x, y, vertical=False, label='C', color=INK, lw=2.4):
    if vertical:
        wire(ax, [(x, y - 0.45), (x, y - 0.13)], color=color, lw=lw)
        wire(ax, [(x, y + 0.13), (x, y + 0.45)], color=color, lw=lw)
        ax.plot([x - 0.22, x + 0.22], [y - 0.13, y - 0.13], color=color, lw=lw)
        ax.plot([x - 0.22, x + 0.22], [y + 0.13, y + 0.13], color=color, lw=lw)
        ax.text(x + 0.36, y, label, fontsize=11, color=INK, va='center')
    else:
        wire(ax, [(x - 0.45, y), (x - 0.13, y)], color=color, lw=lw)
        wire(ax, [(x + 0.13, y), (x + 0.45, y)], color=color, lw=lw)
        ax.plot([x - 0.13, x - 0.13], [y - 0.35, y + 0.35], color=color, lw=lw)
        ax.plot([x + 0.13, x + 0.13], [y - 0.35, y + 0.35], color=color, lw=lw)
        ax.text(x, y - 0.67, label, fontsize=11, color=INK, ha='center')


def switch(ax, x, y, open_switch=True, color=INK, lw=2.4):
    wire(ax, [(x - 0.35, y), (x - 0.08, y)], color=color, lw=lw)
    wire(ax, [(x + 0.08, y), (x + 0.35, y)], color=color, lw=lw)
    ax.add_patch(Circle((x - 0.08, y), 0.055, facecolor='white', edgecolor=color, lw=1.6))
    ax.add_patch(Circle((x + 0.08, y), 0.055, facecolor='white', edgecolor=color, lw=1.6))
    end = (x + 0.30, y + 0.25) if open_switch else (x + 0.08, y)
    wire(ax, [(x - 0.08, y), end], color=color, lw=lw)


def supply(ax, x, y, label='d.c. supply', w=1.25, h=0.95):
    box(ax, x, y, w, h, label, fc='#f1f4f7', fs=10, weight='bold')
    ax.text(x + 0.33, y + 0.22, '+', fontsize=13, color=RED, ha='center')
    ax.text(x + 0.79, y + 0.22, '-', fontsize=13, color=NAVY, ha='center')


def fig_plates():
    fig, ax = setup('Parallel plates and capacitor', '9702/51/M/J/22 | plan: vary d, measure V, plot 1/V against d')
    # Charge state
    ax.text(2.55, 5.45, 'A  Charge plates', ha='center', fontsize=12, weight='bold', color=BLUE)
    supply(ax, 0.35, 2.55, 'd.c. supply')
    ax.add_patch(Rectangle((2.15, 2.0), 0.12, 2.6, facecolor='#3d4a5c', edgecolor=NAVY, lw=1.2))
    ax.add_patch(Rectangle((3.75, 2.0), 0.12, 2.6, facecolor='#3d4a5c', edgecolor=NAVY, lw=1.2))
    ax.text(2.21, 4.85, 'plate', ha='center', fontsize=9, color=MUTED)
    ax.text(3.81, 4.85, 'plate', ha='center', fontsize=9, color=MUTED)
    wire(ax, [(1.60, 3.25), (2.15, 3.25)])
    wire(ax, [(1.60, 2.80), (1.90, 2.80), (1.90, 1.55), (3.81, 1.55), (3.81, 2.00)])
    wire(ax, [(3.87, 3.25), (4.55, 3.25)])
    ax.annotate('d', xy=(3.0, 2.0), xytext=(3.0, 1.55), ha='center', fontsize=12, color=BLUE,
                arrowprops=dict(arrowstyle='<->', color=BLUE, lw=1.8))
    ax.plot([3.0, 3.0], [4.6, 4.93], color=MUTED, lw=0.8)
    ax.text(3.0, 5.05, r'area $A$', ha='center', fontsize=11, color=INK)
    ax.text(3.0, 1.15, 'same A and fixed charging voltage/time', ha='center', fontsize=8.5, color=MUTED)
    # Measure state
    ax.text(9.0, 5.45, 'B  Isolate supply, connect C', ha='center', fontsize=12, weight='bold', color=BLUE)
    ax.add_patch(Rectangle((7.2, 2.0), 0.12, 2.6, facecolor='#3d4a5c', edgecolor=NAVY, lw=1.2))
    ax.add_patch(Rectangle((8.8, 2.0), 0.12, 2.6, facecolor='#3d4a5c', edgecolor=NAVY, lw=1.2))
    ax.axvline(5.9, color='#d7e0e8', lw=1.0, ls='-')
    wire(ax, [(7.26, 3.25), (6.55, 3.25), (6.55, 1.55), (9.85, 1.55), (9.85, 3.25), (8.86, 3.25)])
    capacitor(ax, 10.55, 3.25, vertical=True, label='C (uncharged)')
    wire(ax, [(8.92, 3.25), (10.55, 3.25)])
    wire(ax, [(7.26, 3.25), (6.55, 3.25)])
    # voltmeter parallel branch
    wire(ax, [(8.92, 3.25), (9.35, 3.25), (9.35, 4.55), (10.55, 4.55), (10.55, 3.70)])
    wire(ax, [(8.92, 2.75), (9.35, 2.75), (9.35, 1.15), (10.55, 1.15), (10.55, 2.80)])
    ax.add_patch(Circle((10.55, 2.85), 0.35, facecolor='white', edgecolor=INK, lw=1.8))
    ax.text(10.55, 2.85, 'V', ha='center', va='center', fontsize=12, weight='bold')
    ax.text(10.55, 0.67, 'voltmeter across C', ha='center', fontsize=8.5, color=MUTED)
    ax.plot([8.0, 8.0], [2.0, 1.55], color=BLUE, lw=1.3)
    ax.plot([7.88, 8.12], [2.0, 2.0], color=BLUE, lw=1.3)
    ax.plot([7.88, 8.12], [1.55, 1.55], color=BLUE, lw=1.3)
    ax.annotate('', xy=(8.0, 2.0), xytext=(8.0, 1.55), arrowprops=dict(arrowstyle='<->', color=BLUE, lw=1.0))
    ax.text(8.0, 4.7, r'area $A$', ha='center', fontsize=11, color=INK)
    ax.text(7.26, 3.55, '+', ha='center', va='center', fontsize=13, color=RED, weight='bold')
    ax.text(8.86, 2.55, '-', ha='center', va='center', fontsize=13, color=NAVY, weight='bold')
    ax.text(6.05, 0.45, 'Use a discharge resistor before each run; switch off before changing d.',
            ha='center', fontsize=9.2, color=RED)
    savefig(fig, 'q1-plates-capacitor-rebuilt')


def fig_coil():
    def build(d):
        d.config(fontsize=8)
        d += elm.SourceV().right()
        d += elm.Switch().right()
        d += elm.Resistor().right()
        d += elm.Inductor().right()
        d += elm.Line().down(4).left(12)
    circuit = schem_png('q1-coil-resistor-circuit-schemdraw', build)
    fig, ax = setup('Coil and resistor timing circuit', '9702/51/M/J/21 | vary R, measure the few-millisecond rise time t')
    ax.imshow(plt.imread(circuit), extent=(0.30, 8.65, 1.55, 4.80), aspect='auto', zorder=1)
    ax.text(1.35, 4.55, 'high-voltage d.c. supply', ha='center', fontsize=9)
    ax.text(3.15, 4.18, 'S', ha='center', fontsize=10)
    ax.text(4.35, 4.18, 'R (swap here)', ha='center', fontsize=9)
    ax.text(6.15, 4.18, 'coil: N turns, area A, length L', ha='center', fontsize=9)
    ax.text(2.55, 4.95, 't = 0 at switch closure', ha='center', fontsize=9, color=BLUE)
    ax.text(4.55, 1.23, "coil's own resistance is separate from R and should be accounted for", ha='center', fontsize=8.7, color=MUTED)
    # CRO branch across R
    ax.add_patch(FancyBboxPatch((8.85, 2.15), 2.25, 1.8, boxstyle='round,pad=0.05,rounding_size=0.10',
                                facecolor='#16243b', edgecolor=INK, lw=1.8))
    ax.text(9.97, 3.55, 'CRO / data logger', ha='center', fontsize=10, color='white', weight='bold')
    ax.plot([9.05, 10.95], [2.72, 2.72], color='#2cc7e8', lw=1.2)
    ax.plot([9.05, 9.35, 9.55, 9.75, 9.95, 10.20, 10.50, 10.95],
            [2.75, 2.95, 2.52, 2.92, 2.57, 2.84, 2.64, 2.74], color='#2cc7e8', lw=1.5)
    ax.text(9.97, 2.30, 'read t to a fixed threshold', ha='center', fontsize=8.5, color='#b9c7d8')
    wire(ax, [(3.55, 3.25), (3.55, 4.35), (9.15, 4.35), (9.15, 3.95)], color=GOLD, lw=1.6, ls='--')
    wire(ax, [(5.10, 3.25), (5.10, 4.02), (10.65, 4.02), (10.65, 3.95)], color=GOLD, lw=1.6, ls='--')
    ax.text(6.95, 4.55, 'CRO connected across R', ha='center', fontsize=9.5, color=GOLD)
    ax.text(6.0, 0.65, 'Keep the same coil, supply setting and threshold; allow the coil to cool between trials.',
            ha='center', fontsize=9.0, color=RED)
    savefig(fig, 'q1-coil-resistor-rebuilt')


def fig_wire():
    fig, ax = setup('Wire expansion under current', '9702/52/O/N/09 | vary diameter d, measure centre displacement y')
    # stands and bench
    ax.plot([1.25, 1.25], [1.05, 4.60], color='#52637d', lw=7)
    ax.plot([10.55, 10.55], [1.05, 4.60], color='#52637d', lw=7)
    ax.plot([0.8, 11.0], [0.75, 0.75], color=INK, lw=2.2)
    for x in [1.25, 10.55]:
        ax.add_patch(Rectangle((x - 0.45, 0.75), 0.9, 0.15, facecolor='#52637d', edgecolor=INK, lw=1))
        ax.add_patch(Rectangle((x - 0.28, 4.40), 0.56, 0.28, facecolor='#52637d', edgecolor=INK, lw=1))
    # clamps and wire
    ax.add_patch(Rectangle((1.65, 4.25), 0.65, 0.25, facecolor='#b9c4d0', edgecolor=INK, lw=1.3))
    ax.add_patch(Rectangle((9.50, 4.25), 0.65, 0.25, facecolor='#b9c4d0', edgecolor=INK, lw=1.3))
    wire(ax, [(2.30, 4.38), (9.50, 4.38)], lw=2.4)
    xs = [2.30 + i * (7.20 / 60) for i in range(61)]
    ys = [4.38 - 0.18 * (1 - ((x - 5.90) / 3.60) ** 2) for x in xs]
    ax.plot(xs, ys, color=BLUE, lw=2.0, ls=(0, (5, 4)))
    ax.text(5.9, 4.72, 'wire, diameter d, fixed length', ha='center', fontsize=10.5, color=INK)
    ax.text(7.55, 3.45, 'wire when current passes', ha='center', fontsize=9.2, color=BLUE)
    # y arrow and scale
    ax.annotate('', xy=(5.9, 4.38), xytext=(5.9, 3.48), arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2.1))
    ax.text(6.16, 3.92, 'y', fontsize=13, color=GOLD, weight='bold')
    ax.plot([7.30, 7.30], [2.55, 4.52], color=INK, lw=1.6)
    for yy in [2.75, 3.20, 3.65, 4.10, 4.50]:
        ax.plot([7.17, 7.43], [yy, yy], color=INK, lw=1.4)
    ax.plot([7.17, 7.43], [4.38, 4.38], color=INK, lw=1.2)
    ax.text(7.30, 2.52, 'vertical scale', fontsize=9.2, color=MUTED)
    ax.text(7.55, 4.38, 'zero', va='center', fontsize=8, color=BLUE)
    # circuit beneath
    supply(ax, 3.9, 0.95, 'd.c. supply', w=1.35, h=0.72)
    ax.add_patch(Circle((2.65, 1.32), 0.32, facecolor='white', edgecolor=INK, lw=1.8))
    ax.text(2.65, 1.32, 'A', ha='center', va='center', fontsize=12, weight='bold')
    ax.text(2.65, 0.83, 'ammeter', ha='center', fontsize=8.5, color=MUTED)
    wire(ax, [(1.95, 1.32), (1.25, 1.32), (1.25, 4.38), (2.30, 4.38)])
    wire(ax, [(9.50, 4.38), (10.55, 4.38), (10.55, 1.32), (5.25, 1.32)])
    wire(ax, [(3.0, 1.32), (3.9, 1.32)])
    ax.annotate('', xy=(4.05, 4.38), xytext=(3.20, 4.38),
                arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.4))
    for x in (2.30, 9.50):
        for y in (1.26, 1.38):
            ax.plot([x - 0.12, x + 0.12], [y - 0.06, y + 0.06], color=INK, lw=0.8)
        ax.plot(x, 4.38, 'o', ms=3, color=BLUE)
    ax.text(8.55, 5.30, 'micrometer reads d here', fontsize=8, color=BLUE)
    ax.text(6.0, 0.30, 'No hanging mass is needed; keep support spacing, material, current and heating time fixed.',
            ha='center', fontsize=9.2, color=RED)
    savefig(fig, 'q1-wire-expansion-rebuilt')


def fig_discharge():
    def build(d):
        d.config(unit=1.0, inches_per_unit=0.34, fontsize=8)
        d += elm.Line().at((0, 0)).to((0, 6))
        d += elm.Line().at((0, 6)).to((8, 6))
        d += elm.Switch().at((1, 6)).right()
        d += elm.SourceV().at((3.2, 6)).right()
        d += elm.Line().at((8, 6)).to((8, 0))
        d += elm.Line().at((0, 4)).to((2, 4))
        d += elm.Capacitor().at((3, 4)).right()
        d += elm.Line().at((4, 4)).to((5, 4))
        d += elm.Capacitor().at((6, 4)).right()
        d += elm.Line().at((7, 4)).to((8, 4))
        d += elm.Line().at((0, 2)).to((3, 2))
        d += elm.MeterV().at((4, 2)).right()
        d += elm.Line().at((5, 2)).to((8, 2))
        d += elm.Line().at((0, 0)).to((3, 0))
        d += elm.ResistorIEC().at((4, 0)).right()
        d += elm.Line().at((5, 0)).to((8, 0))
    circuit = schem_png('q2-capacitor-discharge-circuit-schemdraw', build)
    fig, ax = setup('Capacitor discharge circuit', '9702/52/O/N/23 | charge, open the switch, then record V at fixed t')
    ax.imshow(plt.imread(circuit), extent=(1.0, 10.5, 0.85, 5.05), aspect='auto', zorder=1)
    ax.text(2.55, 4.72, 'S', ha='center', fontsize=10)
    ax.text(4.35, 4.72, 'd.c. supply', ha='center', fontsize=9)
    ax.text(4.05, 3.78, 'C_A', ha='center', fontsize=9)
    ax.text(7.05, 3.78, 'C_B', ha='center', fontsize=9)
    ax.text(5.10, 2.35, 'V', ha='center', fontsize=10)
    ax.text(5.10, 1.18, 'R', ha='center', fontsize=10)
    ax.add_patch(Rectangle((2.25, 2.95), 5.65, 1.25, fill=False, edgecolor=BLUE, lw=1.2, ls='--'))
    ax.text(5.1, 4.58, 'switch closed: charging', ha='center', fontsize=9.3, color=INK)
    ax.text(5.1, 2.72, 'switch open: discharging through R', ha='center', fontsize=9.3, color=RED)
    ax.text(8.75, 5.55, 'open S -> start stopwatch here -> read V at fixed t', ha='center', fontsize=9.0, color=RED)
    ax.text(5.1, 0.82, '1/C = 1/C_A + 1/C_B | R fixed | ideal voltmeter assumed', ha='center', fontsize=8.9, color=MUTED)
    savefig(fig, 'q2-capacitor-discharge-rebuilt')


def fig_phase():
    def build(d):
        d.config(unit=1.0, inches_per_unit=0.34, fontsize=8)
        d += elm.SourceSin().at((0, 3)).up()
        d += elm.Line().at((0, 5)).to((3, 5))
        d += elm.Capacitor().at((3, 4.5)).down()
        d += elm.Resistor().at((3, 2)).down()
        d += elm.Line().at((3, 1)).to((0, 1)).to((0, 2))
    circuit = schem_png('q2-ac-phase-circuit-schemdraw', build)
    fig, ax = setup('a.c. phase-difference circuit', '9702/52/F/M/22 | vary R, measure theta from two oscilloscope traces')
    ax.imshow(plt.imread(circuit), extent=(0.55, 4.75, 1.15, 5.25), aspect='auto', zorder=1)
    ax.text(0.55, 3.45, 'a.c. supply\nf fixed', ha='left', fontsize=9)
    ax.text(3.35, 4.35, 'C', ha='center', fontsize=10)
    ax.text(3.35, 2.05, 'R (swap here)', ha='center', fontsize=9)
    # CRO at right
    box(ax, 6.0, 1.5, 5.2, 3.6, 'dual-beam oscilloscope', fc='#16243b', ec=INK, fs=14, color='white', weight='bold')
    # screen area
    ax.add_patch(Rectangle((6.45, 2.0), 4.3, 2.35, facecolor='#0d1728', edgecolor='#89a2bd', lw=1.0))
    xx = [6.5 + i * 0.08 for i in range(54)]
    y1 = [3.55 + 0.42 * math.sin((i / 53) * 4 * math.pi) for i in range(54)]
    y2 = [2.80 + 0.42 * math.sin((i / 53) * 4 * math.pi - 0.70) for i in range(54)]
    ax.plot(xx, y1, color=GOLD, lw=2.0)
    ax.plot(xx, y2, color='#2cc7e8', lw=2.0)
    ax.text(6.62, 4.55, 'CH1 across R', fontsize=9, color=GOLD)
    ax.text(6.62, 1.82, 'CH2 across C', fontsize=9, color='#2cc7e8')
    ax.annotate('', xy=(7.65, 3.95), xytext=(7.65, 3.20), arrowprops=dict(arrowstyle='<->', color='white', lw=1.2))
    ax.text(7.82, 3.58, 'theta', color='white', fontsize=10, va='center')
    ax.annotate('', xy=(8.95, 3.97), xytext=(7.65, 3.97), arrowprops=dict(arrowstyle='<->', color=GOLD, lw=1.2))
    ax.text(8.30, 4.08, 'T', color=GOLD, fontsize=10, ha='center')
    # scope leads
    wire(ax, [(3.7, 4.85), (4.45, 4.85), (4.45, 4.35), (6.0, 4.35)], color='#2cc7e8', lw=1.6, ls='--')
    wire(ax, [(3.7, 2.0), (4.8, 2.0), (4.8, 2.65), (6.0, 2.65)], color=GOLD, lw=1.6, ls='--')
    ax.text(4.65, 5.25, 'measure time shift Δt and period T', ha='center', fontsize=9.3, color=BLUE)
    ax.text(4.65, 0.47, 'theta = 360 degrees x (Δt / T); keep f and C fixed while changing R.',
            ha='center', fontsize=9.2, color=RED)
    savefig(fig, 'q2-ac-phase-rebuilt')


def q2_cap_graph():
    rows = [(2.2, 2.2, 2.45), (2.2, 3.3, 2.75), (2.2, 5.6, 3.05),
            (3.3, 3.3, 3.10), (3.3, 5.6, 3.50), (5.6, 5.6, 3.85)]
    x, y, sy = [], [], []
    for ca, cb, v in rows:
        x.append((ca + cb) / (ca * cb))
        y.append(math.log(v))
        sy.append(0.05 / v)
    m = -0.8289185423
    c = 1.643171300
    m_lo, m_hi = -0.8793948965, -0.7624333693
    fig, ax = plt.subplots(figsize=(8.2, 5.8))
    ax.errorbar(x, y, yerr=sy, fmt='x', ms=8, mew=1.8, color=BLUE, ecolor=BLUE, capsize=3, label='data ± uncertainty')
    xx = [0.32, 0.94]
    ax.plot(xx, [m*z+c for z in xx], color=NAVY, lw=2.2, label='best fit')
    ax.plot(xx, [m_lo*z+1.67504 for z in xx], color=RED, lw=1.5, ls='--', label='WAL')
    ax.plot(xx, [m_hi*z+1.60742 for z in xx], color=RED, lw=1.5, ls='--')
    ax.set_xlim(0.30, 1.00)
    ax.set_ylim(0.84, 1.42)
    ax.set_xlabel('1/C / 10⁴ F⁻¹', fontsize=11)
    ax.set_ylabel('ln(V / V)', fontsize=11)
    ax.set_title('Model graph for 9702/52/O/N/23', color=NAVY, weight='bold')
    ax.grid(True, color=GRID, lw=0.8)
    ax.legend(frameon=True, fontsize=9, loc='lower left')
    ax.text(0.34, 0.875, 'For the intercept, use c = y - mx because x = 0 is outside the grid.', fontsize=8.5, color=MUTED)
    fig.tight_layout()
    savefig(fig, 'q2-capacitor-graph-model')


def q2_phase_graph():
    rs = [12, 16, 22, 33, 39, 43]
    th = [80.8, 77.5, 73.0, 65.2, 61.7, 59.3]
    x = [1000 / r for r in rs]
    sx = [0.05 * z for z in x]
    y = [math.tan(math.radians(t)) for t in th]
    m = 0.0743529730
    c = -0.07503815
    m_lo, m_hi = 0.0686470, 0.0808584
    fig, ax = plt.subplots(figsize=(8.2, 5.8))
    ax.errorbar(x, y, xerr=sx, fmt='x', ms=8, mew=1.8, color=BLUE, ecolor=BLUE, capsize=3, label='data ± 5% in R')
    xx = [20, 88]
    ax.plot(xx, [m*z+c for z in xx], color=NAVY, lw=2.2, label='best fit')
    ax.plot(xx, [m_lo*z + 0.164 for z in xx], color=RED, lw=1.5, ls='--', label='WAL')
    ax.plot(xx, [m_hi*z - 0.288 for z in xx], color=RED, lw=1.5, ls='--')
    ax.set_xlim(20, 90)
    ax.set_ylim(1.0, 6.55)
    ax.set_xlabel('1/R / 10⁻³ Ω⁻¹', fontsize=11)
    ax.set_ylabel('tan θ', fontsize=11)
    ax.set_title('Model graph for 9702/52/F/M/22', color=NAVY, weight='bold')
    ax.grid(True, color=GRID, lw=0.8)
    ax.legend(frameon=True, fontsize=9, loc='upper left')
    fig.tight_layout()
    savefig(fig, 'q2-ac-phase-graph-model')


for fn in [fig_plates, fig_coil, fig_wire, fig_discharge, fig_phase, q2_cap_graph, q2_phase_graph]:
    fn()


FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'
FONT_B = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
FONT_I = '/System/Library/Fonts/Supplemental/Arial Italic.ttf'
pdfmetrics.registerFont(TTFont('Arial', FONT))
pdfmetrics.registerFont(TTFont('Arial-Bold', FONT_B))
pdfmetrics.registerFont(TTFont('Arial-Italic', FONT_I))


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CoverTitle', parent=styles['Title'], fontName='Arial-Bold', fontSize=26,
                          leading=31, textColor=colors.HexColor(NAVY), alignment=TA_CENTER, spaceAfter=12))
styles.add(ParagraphStyle(name='CoverSub', parent=styles['Normal'], fontName='Arial', fontSize=12,
                          leading=17, textColor=colors.HexColor(MUTED), alignment=TA_CENTER, spaceAfter=7))
styles.add(ParagraphStyle(name='H1x', parent=styles['Heading1'], fontName='Arial-Bold', fontSize=18,
                          leading=22, textColor=colors.HexColor(NAVY), spaceBefore=5, spaceAfter=8))
styles.add(ParagraphStyle(name='H2x', parent=styles['Heading2'], fontName='Arial-Bold', fontSize=13,
                          leading=16, textColor=colors.HexColor(BLUE), spaceBefore=6, spaceAfter=4))
styles.add(ParagraphStyle(name='Bodyx', parent=styles['BodyText'], fontName='Arial', fontSize=9.3,
                          leading=13.1, textColor=colors.HexColor(INK), spaceAfter=4))
styles.add(ParagraphStyle(name='Smallx', parent=styles['BodyText'], fontName='Arial', fontSize=8.2,
                          leading=11.2, textColor=colors.HexColor(MUTED), spaceAfter=3))
styles.add(ParagraphStyle(name='Callout', parent=styles['BodyText'], fontName='Arial', fontSize=9.2,
                          leading=13, textColor=colors.HexColor(INK), backColor=colors.HexColor(PALE_BLUE),
                          borderColor=colors.HexColor(BLUE), borderWidth=0.7, borderPadding=7, spaceBefore=4, spaceAfter=7))
styles.add(ParagraphStyle(name='Eq', parent=styles['BodyText'], fontName='Arial-Bold', fontSize=11,
                          leading=15, textColor=colors.HexColor(NAVY), alignment=TA_CENTER, spaceBefore=4, spaceAfter=6))
styles.add(ParagraphStyle(name='Tiny', parent=styles['BodyText'], fontName='Arial', fontSize=7.5,
                          leading=9.5, textColor=colors.HexColor(INK)))


def P(text, style='Bodyx'):
    return Paragraph(text, styles[style])


def title(text, source=''):
    items = [P(text, 'H1x')]
    if source:
        items.append(P(source, 'Smallx'))
    items.append(HRFlowable(width='100%', thickness=1.2, color=colors.HexColor(BLUE), spaceAfter=8))
    return items


def img(name, width=17.2 * cm):
    return Image(str(DIAG / f'{name}.png'), width=width, height=width * 0.55)


def table(data, widths=None, header=True, small=False):
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign='LEFT')
    fs = 7.8 if small else 8.6
    leading = 9.8 if small else 11.0
    cmd = [
        ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, -1), fs),
        ('LEADING', (0, 0), (-1, -1), leading),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor(INK)),
        ('GRID', (0, 0), (-1, -1), 0.35, colors.HexColor('#c7d2de')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]
    if header:
        cmd += [('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(NAVY)),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('FONTNAME', (0, 0), (-1, 0), 'Arial-Bold')]
    for r in range(1 if header else 0, len(data)):
        if r % 2 == 0:
            cmd.append(('BACKGROUND', (0, r), (-1, r), colors.HexColor('#eaf0f5')))
    t.setStyle(TableStyle(cmd))
    return t


def bullets(items):
    out = []
    for item in items:
        out.append(P(f'• {item}', 'Bodyx'))
    return out


def footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setStrokeColor(colors.HexColor('#d7e0e8'))
    canvas.setLineWidth(0.5)
    canvas.line(1.7 * cm, 1.25 * cm, w - 1.7 * cm, 1.25 * cm)
    canvas.setFont('Arial', 7.5)
    canvas.setFillColor(colors.HexColor(MUTED))
    canvas.drawString(1.7 * cm, 0.82 * cm, 'CAIE Physics 9702 | Paper 5 electricity focus')
    canvas.drawRightString(w - 1.7 * cm, 0.82 * cm, f'{doc.page} / 10')
    canvas.restoreState()


pdf_path = OUT / 'Paper-5-electricity-focus-solved-guide.pdf'
doc = BaseDocTemplate(str(pdf_path), pagesize=A4, leftMargin=1.7 * cm, rightMargin=1.7 * cm,
                      topMargin=1.45 * cm, bottomMargin=1.55 * cm, title='Paper 5 electricity focus solved guide')
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
doc.addPageTemplates([PageTemplate(id='main', frames=frame, onPage=footer)])
story = []

# Cover
story += [Spacer(1, 2.2 * cm), P('CAIE Physics 9702', 'CoverTitle'),
          P('Paper 5 electricity focus', 'CoverTitle'),
          P('Five source-matched questions with 15/15 planning answers, exact table work, graph models and rebuilt diagrams', 'CoverSub'),
          Spacer(1, 0.8 * cm),
          Table([[P('<b>Q1 planning</b><br/>Parallel plates<br/>Coil and resistor<br/>Heated wire', 'Bodyx'),
                  P('<b>Q2 analysis</b><br/>Capacitor discharge<br/>a.c. phase difference', 'Bodyx')]],
                colWidths=[8.4 * cm, 8.4 * cm], style=TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor(PALE)),
                    ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor(BLUE)),
                    ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#c7d2de')),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 12),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 12), ('TOPPADDING', (0, 0), (-1, -1), 10),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
                ])),
          Spacer(1, 1.0 * cm),
          P('Prepared from the 100-page Paper-5-WS_26x27 workbook. The five questions below are the electricity set already identified in your notes.', 'CoverSub'),
          PageBreak()]

# Scope page
story += title('What to revise', 'The question wording and page references below come from the supplied Paper-5-WS_26x27.pdf.')
scope = [
    ['No.', 'Paper page', 'Code', 'Topic', 'What the examiner wants'],
    ['1', '31', '9702/51/M/J/22', 'Parallel plates + capacitor', 'A workable switching arrangement, controls, 1/V vs d, K and W'],
    ['2', '34', '9702/51/M/J/21', 'Coil + resistor timing', 'A series circuit, CRO timing, t vs 1/R, K'],
    ['3', '37', '9702/52/O/N/09', 'Wire heated by current', 'Vary d safely, measure y, lg y vs lg d, q'],
    ['4', '73-76', '9702/52/O/N/23', 'Capacitor discharge', 'ln V vs 1/C, uncertainties, gradient, R, I0 and C'],
    ['5', '77-80', '9702/52/F/M/22', 'a.c. phase difference', 'tan theta vs 1/R, frequency uncertainty, C and R'],
]
story += [table(scope, widths=[0.7*cm, 1.6*cm, 3.0*cm, 4.0*cm, 7.0*cm], small=True), Spacer(1, 0.35*cm)]
story += [P('<b>Paper 5 habit:</b> name the variable you change, name the variable you measure, say exactly what stays fixed, give an instrument for every measurement, then turn the equation into y = mx + c.', 'Callout')]
story += [P('For graph questions, show the processed table before drawing the graph. Put units or scale factors in the headings, add the required error bars, draw a best-fit line and a worst acceptable line, and calculate the gradient from two far-apart points on the line.', 'Bodyx')]
story += [PageBreak()]

# Q1 plates
story += title('Q1. Parallel plates and an uncharged capacitor', '9702/51/M/J/22 | Paper page 31 | 15 marks')
story += [img('q1-plates-capacitor-rebuilt'), P('The cleanest answer shows the experiment in two states: charge the same pair of plates from the supply, isolate the supply, then connect the plates to the uncharged capacitor and place the voltmeter in parallel with it.', 'Smallx')]
story += [P('<b>Variables.</b> Independent variable: plate separation d. Dependent variable: potential difference V across C after transfer. Keep plate area A, capacitor C, charging voltage, charging time, temperature and the plate pair fixed.', 'Bodyx')]
story += [P('<b>Apparatus.</b> Two parallel metal plates on G-clamped stands; d.c. supply; uncharged capacitor C; digital voltmeter; two-position switch or separate switching leads; micrometer or spacers for d; vernier calipers for plate dimensions; discharge resistor; shrouded leads.', 'Bodyx')]
story += [P('<b>Method.</b> Measure the plate length and width at several positions and calculate the mean area A. Set a separation d, measure it at several points and take the mean. Charge the plates at the same supply voltage for the same time on every run. Isolate the supply, connect the plates to the discharged capacitor, and read V across C quickly. Repeat the reading, discharge C through a resistor, then repeat for at least six values of d across the largest safe range.', 'Bodyx')]
story += [P('<b>Controls.</b> Use the same plates and the same capacitor. Keep the charging voltage and charging time fixed, check the supply before each run, keep the plate faces parallel, and work at nearly constant room temperature.', 'Bodyx')]
story += [P('<b>Analysis.</b>', 'H2x'), P('W/V = 1 + Cd/(KA)<br/>1/V = (C/(WKA))d + 1/W', 'Eq')]
story += [table([['Graph', 'Gradient', 'Intercept', 'Constants'],
                  ['Plot 1/V against d', 'm = C/(WKA)', 'c = 1/W', 'W = 1/c; K = C/(mWA)']],
                 widths=[4.1*cm, 4.0*cm, 3.5*cm, 5.6*cm]),
          P('A straight line supports the relationship. Measure d at several points to detect non-parallel plates, use a wide d range to improve the gradient, and discharge the stored charge before touching the circuit. Switch off before changing the spacing.', 'Callout'), PageBreak()]

# Q1 coil
story += title('Q1. Coil and resistor timing', '9702/51/M/J/21 | Paper page 34 | 15 marks')
story += [img('q1-coil-resistor-rebuilt'), P('The oscilloscope is connected across R. The voltage across R is proportional to the current, so the trace gives the time for the current to reach its chosen maximum threshold.', 'Smallx')]
story += [P('<b>Variables.</b> Independent variable: resistance R, using different unmarked resistors. Dependent variable: time t for the current to reach its maximum value. Keep the same coil, so N, A and L stay fixed; keep the supply setting and the timing threshold fixed.', 'Bodyx')]
story += [P('<b>Method.</b> Measure each resistor with an ohmmeter and record R. Connect one resistor and the coil in series with the high-voltage d.c. supply and switch. Connect the CRO across R, close the switch and use the same trace threshold for every reading. Measure t from the switch event to the threshold, repeat each value, and use at least six resistors spread over the available range.', 'Bodyx')]
story += [P('<b>Measurements and controls.</b> Count or use the stated N; measure coil length L and diameter with a metre rule and micrometer, then calculate A = pi d^2/4. Keep the coil fixed, use the same supply voltage, and let the coil cool because its resistance changes as it heats.', 'Bodyx')]
story += [P('<b>Analysis.</b>', 'H2x'), P('t = (K N^2 A/L)(1/R)', 'Eq')]
story += [table([['Graph', 'Gradient', 'Intercept', 'Value of K'],
                  ['Plot t against 1/R', 'm = K N^2 A/L', '0; line should pass through origin', 'K = mL/(N^2 A)']],
                 widths=[4.3*cm, 4.3*cm, 4.3*cm, 4.3*cm]),
          P('Use shrouded leads and switch the supply off before changing R. The coil and resistor can heat; allow them to cool before handling. Clamp the apparatus so it cannot topple.', 'Callout'), PageBreak()]

# Q1 wire
story += title('Q1. Wire expansion caused by current', '9702/52/O/N/09 | Paper page 37 | 15 marks')
story += [img('q1-wire-expansion-rebuilt'), P('The original question measures the extra centre sag of the wire when the current passes. No hanging mass belongs in the redraw; keep the support spacing and the wire material fixed instead.', 'Smallx')]
story += [P('<b>Variables.</b> Independent variable: wire diameter d. Dependent variable: displacement y at the centre when current passes. Use wires of the same material and length, with the same support spacing, current, heating time and initial conditions.', 'Bodyx')]
story += [P('<b>Method.</b> Measure d with a micrometer at several positions and in two orientations, then use the mean. Mount one wire between the same clamps. Use an ammeter to set the same current for every wire, switch on for the same timed interval, and measure the centre displacement y against a vertical scale. Repeat readings and allow the wire to cool before another run. Use at least six diameters.', 'Bodyx')]
story += [P('<b>Analysis.</b>', 'H2x'), P('y = p d^q<br/>lg y = q lg d + lg p', 'Eq')]
story += [table([['Graph', 'Gradient', 'Intercept', 'Required constant'],
                  ['Plot lg y against lg d', 'm = q', 'c = lg p', 'q is the gradient; p = 10^c']],
                 widths=[4.3*cm, 4.3*cm, 4.3*cm, 4.3*cm]),
          P('The log-log graph should be straight. Switch off before touching the hot wire, use a heat-proof mat, wear eye protection because a tensioned wire can snap, and keep the current low enough that the wire does not melt.', 'Callout'), PageBreak()]

# Q2 capacitor
story += title('Q2. Capacitor discharge: full worked table', '9702/52/O/N/23 | Paper pages 73-76 | 15 marks')
story += [img('q2-capacitor-discharge-rebuilt'), P('The two capacitors are in series, so 1/C = 1/C_A + 1/C_B. The resistor, voltmeter and capacitors share the same two rails during discharge; the top branch charges them while the switch is closed.', 'Smallx')]
story += [P('<b>(a) Linear form.</b> Starting with V = I0 R exp(-t/(C R)) and taking natural logs gives:', 'Bodyx'),
          P('ln V = -(t/R)(1/C) + ln(I0 R)', 'Eq'),
          P('Gradient = -t/R.  y-intercept = ln(I0 R).', 'Bodyx')]
cap_table = [
    ['C_A / 10^-4 F', 'C_B / 10^-4 F', '1/C / 10^4 F^-1', 'V / V', 'ln(V / V)', 'Delta(ln V)'],
    ['2.2', '2.2', '0.909', '2.45 ± 0.05', '0.896', '0.020'],
    ['2.2', '3.3', '0.758', '2.75 ± 0.05', '1.012', '0.018'],
    ['2.2', '5.6', '0.633', '3.05 ± 0.05', '1.115', '0.016'],
    ['3.3', '3.3', '0.606', '3.10 ± 0.05', '1.131', '0.016'],
    ['3.3', '5.6', '0.482', '3.50 ± 0.05', '1.253', '0.014'],
    ['5.6', '5.6', '0.357', '3.85 ± 0.05', '1.348', '0.013'],
]
story += [table(cap_table, widths=[2.2*cm,2.2*cm,2.5*cm,2.5*cm,2.5*cm,2.3*cm], small=True),
          P('Example: for the first row, 1/C = (2.2 + 2.2)/(2.2 × 2.2) = 0.909 in the table scale, ln(2.45) = 0.896, and Δ(ln V) = ΔV/V = 0.05/2.45 = 0.020.', 'Callout'), PageBreak()]

story += title('Q2. Capacitor discharge: graph and final values', 'A model graph is shown; small differences in hand-drawn line placement can change the last digit.')
story += [img('q2-capacitor-graph-model', width=15.8*cm), P('<b>(c).</b> Plot ln(V / V) against 1/C / 10^4 F^-1. Add vertical error bars of +/- Delta(ln V). Draw a best-fit line and a WAL. Because x = 0 lies outside the grid, calculate the intercept from c = y - mx using a point on the best-fit line.', 'Bodyx')]
story += [table([['Quantity', 'Model reading'],
                  ['Best-fit gradient on displayed x-axis', '-0.829'],
                  ['WAL range on displayed x-axis', 'about -0.879 to -0.762'],
                  ['Absolute gradient uncertainty', 'about 0.06 displayed units'],
                  ['True gradient', '(-8.29 +/- 0.58) x 10^-5 F'],
                  ['y-intercept', 'c ≈ 1.64']], widths=[7.0*cm, 9.0*cm]), Spacer(1, 0.2*cm)]
story += [P('<b>(d).</b> With t = 30 +/- 1 s, R = -t/m = 3.62 x 10^5 ohm. From c = ln(I0 R), I0 = exp(c)/R = 1.43 x 10^-5 A. The percentage uncertainty in R is approximately 3.3% from t plus 7.0% from the gradient, giving about 10%.', 'Bodyx'),
          P('<b>(e).</b> For V = 1.20 V, C = -t/[R(ln V - c)] = 5.67 x 10^-5 F.', 'Bodyx'),
          P('Keep the power-of-ten in the x-axis heading: a displayed gradient of -0.829 becomes -0.829 x 10^-4 F on the physical x-axis.', 'Callout'), PageBreak()]

# Q2 phase
story += title('Q2. a.c. phase difference: full worked table', '9702/52/F/M/22 | Paper pages 77-80 | 15 marks')
story += [img('q2-ac-phase-rebuilt'), P('<b>(a) Linear form.</b> tan theta = [1/(2 pi f C)](1/R), so the gradient is 1/(2 pi f C). The theoretical intercept is zero.', 'Bodyx')]
phase_table = [
    ['R / ohm', '1/R / 10^-3 ohm^-1', 'absolute uncertainty', 'theta / degrees', 'tan theta'],
    ['12', '83.3', '4.2', '80.8', '6.17'],
    ['16', '62.5', '3.1', '77.5', '4.51'],
    ['22', '45.5', '2.3', '73.0', '3.27'],
    ['33', '30.3', '1.5', '65.2', '2.16'],
    ['39', '25.6', '1.3', '61.7', '1.86'],
    ['43', '23.3', '1.2', '59.3', '1.68'],
]
story += [table(phase_table, widths=[1.7*cm,3.1*cm,3.2*cm,2.8*cm,2.4*cm], small=True),
          P('The resistor uncertainty is 5%, so Δ(1/R) = 0.05(1/R). Calculate tan theta in degree mode. If the oscilloscope gives a time shift, use theta = 360 degrees × (Δt/T).', 'Callout'), PageBreak()]

story += title('Q2. a.c. phase difference: graph and final values', 'A model graph is shown with horizontal error bars from the 5% resistance uncertainty.')
story += [img('q2-ac-phase-graph-model', width=15.8*cm),
          P('<b>(c).</b> Plot tan theta against 1/R / 10^-3 ohm^-1. Add horizontal error bars. Draw the best-fit line and a WAL; the line need not be forced through the origin, but compare the measured intercept with zero.', 'Bodyx')]
story += [table([['Quantity', 'Model reading'],
                  ['Best-fit gradient on displayed x-axis', '0.0744'],
                  ['WAL range on displayed x-axis', 'about 0.0686 to 0.0809'],
                  ['True gradient', '74.4 ohm'],
                  ['Average frequency', 'f = (101 + 97)/2 = 99 ± 2 Hz'],
                  ['Capacitance', 'C = 1/(2 pi f m) = 2.16 x 10^-5 F = 21.6 uF']], widths=[7.0*cm, 9.0*cm]), Spacer(1, 0.2*cm)]
story += [P('<b>(d).</b> The average frequency is 99 Hz with absolute uncertainty 2 Hz.', 'Bodyx'),
          P('<b>(e).</b> Using the gradient and f, C = 2.16 x 10^-5 F. Taking about 8.7% from the graph and 2.0% from f gives a model percentage uncertainty of about 11%, so C is about (21.6 +/- 2.3) uF.', 'Bodyx'),
          P('<b>(f).</b> For theta = 40 degrees, R = m/tan theta = 74.4/tan(40 degrees) = 88.6 ohm, so a suitable final answer is R about 89 +/- 8 ohm using the graph uncertainty.', 'Bodyx'),
          P('Do not forget the factor 2 pi, and do not use radians in the tangent calculation when theta is given in degrees.', 'Callout'), PageBreak()]

# Closing sheet
story += title('One-page Paper 5 checklist', 'Use this immediately before practising each question.')
story += [table([
    ['Planning question', 'Write this in the answer'],
    ['Variables', 'Independent variable; dependent variable; every quantity kept constant and how.'],
    ['Apparatus', 'Named instruments, correct circuit symbols, labels and a setup that can actually be built.'],
    ['Measurements', 'What is read, where it is read, repeat readings, mean and half-range where suitable.'],
    ['Analysis', 'Rearrange to y = mx + c; name the graph; state gradient and intercept; explain what they give.'],
    ['Safety', 'Link the hazard to the action: stored charge, hot wire/coil, live high-voltage leads, snapping wire.'],
], widths=[4.0*cm, 12.0*cm], small=True), Spacer(1, 0.4*cm),
          table([
    ['Graph question', 'Check before handing it in'],
    ['Table', 'Correct scale factors, significant figures, log rule and absolute uncertainties.'],
    ['Plot', 'Both axes labelled; points use the requested processed quantities; error bars are visible.'],
    ['Lines', 'Best fit and WAL are labelled; neither is kinked; use a large triangle.'],
    ['Numbers', 'Keep powers of ten; quote units; calculate percentage uncertainty from the actual inputs.'],
], widths=[4.0*cm, 12.0*cm], small=True), Spacer(1, 0.45*cm),
          P('<b>Most useful algebra to memorise:</b> for ln x, Delta(ln x) = Delta x/x; for lg x, Delta(lg x) = Delta x/(2.303x); for an x-axis written as q / 10^n, restore the 10^n when finding the physical gradient.', 'Callout'),
          P('The five redrawn figures are also saved as standalone SVG and 320 dpi PNG files beside the PDF, so they stay sharp when printed or enlarged.', 'Smallx')]

def clean_canvas(title, subtitle):
    fig, ax = plt.subplots(figsize=(13.0, 7.25), dpi=320)
    ax.set_xlim(0, 13); ax.set_ylim(0, 7.25); ax.axis('off')
    ax.text(6.5, 7.02, title, ha='center', va='top', fontsize=19, weight='bold', color=NAVY)
    ax.text(6.5, 6.66, subtitle, ha='center', va='top', fontsize=9.5, color=MUTED)
    return fig, ax

def line(ax, points, color=INK, lw=2.0, ls='-'):
    ax.plot([p[0] for p in points], [p[1] for p in points], color=color, lw=lw, ls=ls, solid_capstyle='round')

def clean_switch(ax, x, y, closed=False):
    ax.add_patch(Circle((x, y), 0.09, fc='white', ec=INK, lw=1.5))
    ax.add_patch(Circle((x+0.62, y), 0.09, fc='white', ec=INK, lw=1.5))
    line(ax, [(x+0.09, y), (x+0.53, y if closed else y+0.34)], lw=1.8)
    ax.text(x+0.31, y+0.46, 'S', ha='center', fontsize=10)

def clean_resistor(ax, x, y, horizontal=True, label='R'):
    if horizontal:
        xx = [x, x+0.16, x+0.30, x+0.44, x+0.58, x+0.72, x+0.88]
        yy = [y, y, y+0.18, y-0.18, y+0.18, y-0.18, y]
        line(ax, list(zip(xx, yy)), lw=1.8)
        ax.text(x+0.44, y+0.42, label, ha='center', fontsize=10)
    else:
        xx = [x, x, x+0.18, x-0.18, x+0.18, x-0.18, x]
        yy = [y, y-0.16, y-0.30, y-0.44, y-0.58, y-0.72, y-0.88]
        line(ax, list(zip(xx, yy)), lw=1.8)
        ax.text(x+0.40, y-0.45, label, ha='left', fontsize=10)

def clean_capacitor(ax, x, y, horizontal=True, label='C', scale=1.0):
    if horizontal:
        line(ax, [(x-0.55, y), (x-0.12, y)], lw=2)
        line(ax, [(x+0.12, y), (x+0.55, y)], lw=2)
        ax.plot([x-0.12, x-0.12], [y-0.30*scale, y+0.30*scale], color=INK, lw=2.4)
        ax.plot([x+0.12, x+0.12], [y-0.30*scale, y+0.30*scale], color=INK, lw=2.4)
        ax.text(x, y+0.50, label, ha='center', fontsize=10)
    else:
        line(ax, [(x, y+0.55), (x, y+0.12)], lw=2)
        line(ax, [(x, y-0.12), (x, y-0.55)], lw=2)
        ax.plot([x-0.32*scale, x+0.32*scale], [y+0.12, y+0.12], color=INK, lw=2.4)
        ax.plot([x-0.32*scale, x+0.32*scale], [y-0.12, y-0.12], color=INK, lw=2.4)
        ax.text(x+0.42, y, label, ha='left', va='center', fontsize=10)

def clean_source(ax, x, y, ac=False, label='d.c. supply'):
    ax.add_patch(Circle((x, y), 0.38, fc='white', ec=INK, lw=1.8))
    if ac:
        t = np.linspace(-np.pi, np.pi, 80)
        ax.plot(x+0.25*t/np.pi, y+0.17*np.sin(t), color=BLUE, lw=1.4)
    else:
        ax.text(x-0.12, y+0.12, '+', color='#e45756', fontsize=13, ha='center')
        ax.text(x+0.12, y-0.12, '-', color=INK, fontsize=13, ha='center')
    ax.text(x, y-0.67, label, ha='center', fontsize=9)

def redraw_clean_diagrams():
    # 1. Plates and uncharged capacitor: two clear experimental states.
    fig, ax = clean_canvas('Parallel plates and capacitor', '9702/51/M/J/22 | charge plates, isolate supply, connect uncharged capacitor C')
    ax.axvline(6.5, 0.7, 6.35, color='#d8e0e8', lw=1)
    for ox, tag in [(0.0, 'A  Charge plates'), (6.65, 'B  Isolate supply, connect C')]:
        ax.text(ox+2.75, 6.20, tag, ha='center', fontsize=12, weight='bold', color=BLUE)
    # A
    clean_source(ax, 1.15, 3.35)
    for x in (2.75, 4.50):
        ax.add_patch(Rectangle((x, 2.05), 0.16, 2.55, fc='#9aa9ba', ec=NAVY, lw=1.2))
    line(ax, [(1.53,3.48),(2.75,3.48)]); line(ax, [(1.53,3.22),(2.1,3.22),(2.1,1.55),(4.58,1.55),(4.58,3.22)])
    ax.text(3.62, 4.90, r'area $A$', ha='center', fontsize=10); ax.plot([3.62,3.62],[4.72,4.57], color=MUTED, lw=0.8)
    ax.annotate('', xy=(4.83,2.05), xytext=(4.83,1.55), arrowprops=dict(arrowstyle='<->', color=BLUE, lw=1.4)); ax.text(5.03,1.80,r'$d$',color=BLUE,va='center',fontsize=11)
    ax.text(3.62,0.98,'same A and fixed charging voltage/time',ha='center',fontsize=8.5,color=MUTED)
    # B
    x1,x2=9.25,10.95
    for x in (x1,x2): ax.add_patch(Rectangle((x,2.05),0.16,2.55,fc='#9aa9ba',ec=NAVY,lw=1.2))
    ax.text(10.1,4.90,r'area $A$',ha='center',fontsize=10)
    line(ax,[(8.1,3.35),(9.25,3.35)]); line(ax,[(10.95,3.35),(11.50,3.35),(11.50,4.60),(12.15,4.60)])
    clean_capacitor(ax,12.15,3.35,label='C (uncharged)',scale=1.2)
    line(ax,[(10.95,3.10),(11.25,3.10),(11.25,1.45),(8.1,1.45),(8.1,3.10)])
    ax.add_patch(Circle((12.15,1.85),0.30,fc='white',ec=INK,lw=1.7)); ax.text(12.15,1.85,'V',ha='center',va='center',fontsize=11)
    line(ax,[(12.15,2.15),(12.15,3.35)]); line(ax,[(12.15,1.55),(12.15,1.10)])
    ax.text(9.05,4.12,'+',color='#e45756',fontsize=12,weight='bold'); ax.text(9.05,2.28,'-',color=NAVY,fontsize=12,weight='bold')
    ax.annotate('',xy=(10.1,2.05),xytext=(10.1,1.45),arrowprops=dict(arrowstyle='<->',color=BLUE,lw=1.4)); ax.text(10.28,1.76,r'$d$',color=BLUE,va='center',fontsize=11)
    ax.text(10.75,0.98,'voltmeter across C',ha='center',fontsize=8.5,color=MUTED)
    ax.text(6.5,0.35,'Use a discharge resistor before each run; switch off before changing d.',ha='center',fontsize=9,color='#d9534f')
    fig.savefig(DIAG/'q1-plates-capacitor-rebuilt.png',dpi=320,bbox_inches='tight'); plt.close(fig)

    # 2. Coil timing: simple series loop and CRO connection.
    fig, ax = clean_canvas('Coil and resistor timing circuit', '9702/51/M/J/21 | vary R and measure the rise time t to a fixed CRO threshold')
    clean_source(ax,1.2,3.45,label='high-voltage d.c. supply'); clean_switch(ax,2.3,3.45)
    line(ax,[(2.92,3.45),(3.35,3.45)]); clean_resistor(ax,3.35,3.45,label='R (swap here)')
    line(ax,[(4.25,3.45),(4.75,3.45)]); t=np.linspace(0,2*np.pi,100); ax.plot(5.15+0.45*t/(2*np.pi),3.45+0.18*np.sin(5*t),color=INK,lw=1.8); ax.text(5.65,4.02,'coil: N turns, area A, length L',ha='center',fontsize=9)
    line(ax,[(5.6,3.45),(7.0,3.45),(7.0,1.20),(1.2,1.20),(1.2,3.07)])
    ax.add_patch(FancyBboxPatch((8.0,2.2),3.7,2.1,boxstyle='round,pad=0.08',fc='#17263e',ec='#17263e')); ax.text(9.85,3.85,'CRO / data logger',ha='center',color='white',weight='bold',fontsize=10)
    ax.plot([8.45,8.85,9.1,9.35,9.7,10.1,10.55,11.25],[3.0,3.35,2.55,3.25,2.85,3.15,2.72,3.0],color='#2cc7e8',lw=1.5); ax.text(9.85,2.47,'CH1 across R — fixed threshold',ha='center',color='#b9c4d0',fontsize=8)
    line(ax,[(3.35,4.05),(3.35,4.65),(9.0,4.65),(9.0,4.3)],color='#f0a202',lw=1.1,ls='--'); line(ax,[(4.0,4.05),(4.0,4.35),(8.5,4.35),(8.5,4.3)],color='#f0a202',lw=1.1,ls='--')
    ax.text(2.1,5.25,'t = 0 at switch closure',color=BLUE,fontsize=9); ax.text(6.15,5.25,'CRO connected across R',color='#f0a202',fontsize=9,ha='center')
    ax.text(6.0,0.62,"Account for the coil's own resistance; keep the same coil and allow it to cool between trials.",ha='center',fontsize=8.5,color='#d9534f')
    fig.savefig(DIAG/'q1-coil-resistor-rebuilt.png',dpi=320,bbox_inches='tight'); plt.close(fig)

    # 3. Heated wire: restrained sag and measurement scale.
    fig, ax = clean_canvas('Wire expansion under current', '9702/52/O/N/09 | vary diameter d and measure centre displacement y')
    line(ax,[(1.3,4.35),(11.7,4.35)],lw=2.3); xs=np.linspace(2.2,10.8,100); ys=4.35-0.22*(1-((xs-6.5)/4.3)**2); ax.plot(xs,ys,color=BLUE,lw=1.7,ls='--')
    for x in (1.7,11.3):
        ax.add_patch(Rectangle((x-0.25,3.95),0.5,0.8,fc='#9aa9ba',ec=NAVY,lw=1)); ax.add_patch(Rectangle((x-0.16,1.0),0.32,3.0,fc='#52637d',ec=NAVY,lw=1)); ax.plot([x-0.45,x+0.45],[0.85,0.85],color=NAVY,lw=2)
    ax.annotate('',xy=(6.5,4.35),xytext=(6.5,4.13),arrowprops=dict(arrowstyle='<->',color='#f0a202',lw=1.5)); ax.text(6.72,4.22,r'$y$',color='#f0a202',fontsize=11,weight='bold')
    ax.plot([7.5,7.5],[3.2,4.62],color=INK,lw=1.4); [ax.plot([7.35,7.65],[yy,yy],color=INK,lw=1.0) for yy in np.linspace(3.2,4.62,6)]; ax.text(7.85,3.0,'vertical scale; zero at original wire',fontsize=8.5,color=MUTED)
    clean_source(ax,6.5,1.75); ax.add_patch(Circle((3.8,1.75),0.28,fc='white',ec=INK,lw=1.6)); ax.text(3.8,1.75,'A',ha='center',va='center',fontsize=10); ax.text(3.8,1.30,'ammeter',ha='center',fontsize=8.5,color=MUTED); line(ax,[(3.52,1.75),(1.7,1.75),(1.7,4.35)]); line(ax,[(11.3,4.35),(11.3,1.75),(6.9,1.75)]); line(ax,[(4.08,1.75),(6.12,1.75)])
    ax.text(6.5,5.0,'wire, diameter $d$, fixed length',ha='center',fontsize=10); ax.text(6.5,0.35,'Measure d with a micrometer; keep support spacing, material, current and heating time fixed.',ha='center',fontsize=8.5,color='#d9534f')
    fig.savefig(DIAG/'q1-wire-expansion-rebuilt.png',dpi=320,bbox_inches='tight'); plt.close(fig)

    # 4. Capacitor discharge: separate charging and discharging states.
    fig, ax = clean_canvas('Capacitor discharge circuit', '9702/52/O/N/23 | charge, open S, start the stopwatch, and read V at fixed t')
    ax.axvline(6.5,0.7,6.1,color='#d8e0e8',lw=1); ax.text(3.25,6.1,'A  switch closed: charging',ha='center',fontsize=12,weight='bold',color=BLUE); ax.text(9.75,6.1,'B  switch open: discharging through R',ha='center',fontsize=12,weight='bold',color=BLUE)
    # left charging state
    clean_source(ax,2.15,3.25); clean_switch(ax,3.0,4.7,closed=True); line(ax,[(1.8,3.25),(1.8,4.7),(2.85,4.7)]); line(ax,[(3.62,4.7),(5.2,4.7),(5.2,2.3),(1.8,2.3),(1.8,3.0)]); clean_capacitor(ax,4.0,3.5,label='C_A + C_B',scale=1.2); ax.text(3.25,1.25,'same two capacitors charge from the d.c. supply',ha='center',fontsize=8.5,color=MUTED)
    # right discharge state
    clean_switch(ax,8.0,4.7,closed=False); clean_capacitor(ax,9.4,4.7,label='C_A and C_B',scale=1.0); clean_resistor(ax,10.7,2.4,horizontal=False,label='R'); ax.add_patch(Circle((9.4,2.4),0.28,fc='white',ec=INK,lw=1.6)); ax.text(9.4,2.4,'V',ha='center',va='center',fontsize=10); line(ax,[(7.4,4.7),(7.4,2.4),(9.12,2.4)]); line(ax,[(9.68,2.4),(11.2,2.4),(11.2,4.7),(8.38,4.7)]); line(ax,[(10.7,1.52),(10.7,1.0),(7.4,1.0),(7.4,2.4)],color=BLUE,lw=1.5,ls='--'); ax.text(9.75,0.60,'start stopwatch as S opens; read V at the same time t',ha='center',fontsize=8.5,color='#d9534f')
    fig.savefig(DIAG/'q2-capacitor-discharge-rebuilt.png',dpi=320,bbox_inches='tight'); plt.close(fig)

    # 5. AC phase: clean circuit and CRO with labelled time measurements.
    fig, ax = clean_canvas('a.c. phase-difference circuit', '9702/52/F/M/22 | vary R, keep f and C fixed, and measure theta from two CRO traces')
    clean_source(ax,1.55,3.65,ac=True,label='a.c. supply, f fixed'); line(ax,[(1.55,4.03),(1.55,5.2),(3.3,5.2)]); clean_capacitor(ax,3.3,4.65,horizontal=False,label='C'); line(ax,[(3.3,4.1),(3.3,2.2)]); clean_resistor(ax,3.3,2.2,horizontal=False,label='R (swap here)'); line(ax,[(3.3,1.32),(1.55,1.32),(1.55,3.27)])
    ax.add_patch(FancyBboxPatch((6.2,1.2),5.6,4.8,boxstyle='round,pad=0.10',fc='#17263e',ec='#17263e')); ax.text(9.0,5.55,'DUAL-BEAM OSCILLOSCOPE',ha='center',color='white',weight='bold',fontsize=10); ax.add_patch(Rectangle((6.8,2.0),4.4,2.9,fc='#0e1a2d',ec='#8196b3',lw=0.8))
    xx=np.linspace(6.9,11.1,240); ax.plot(xx,3.75+0.52*np.sin((xx-6.9)*3.0),color='#f0a202',lw=1.5); ax.plot(xx,3.0+0.52*np.sin((xx-6.9)*3.0-0.85),color='#2cc7e8',lw=1.5); ax.text(6.95,5.10,'CH1 across R',color='#f0a202',fontsize=8.5); ax.text(6.95,1.62,'CH2 across C',color='#2cc7e8',fontsize=8.5)
    ax.annotate('',xy=(8.6,4.65),xytext=(9.95,4.65),arrowprops=dict(arrowstyle='<->',color='#f0a202',lw=1.2)); ax.text(9.27,4.82,'T',ha='center',color='#f0a202',fontsize=9); ax.annotate('',xy=(8.0,3.75),xytext=(8.0,3.33),arrowprops=dict(arrowstyle='<->',color='white',lw=1.2)); ax.text(8.15,3.52,r'$	heta$',color='white',fontsize=9); ax.text(7.15,1.0,'Measure horizontal zero-crossing shift Δt and one full period T.',fontsize=8.5,color=BLUE); ax.text(9.0,0.45,r'$	heta = 360^\circ(\Delta t/T)$',ha='center',fontsize=10,color='#d9534f')
    # Cover the legacy tab-corrupted annotation from the earlier composite and redraw it cleanly.
    ax.add_patch(Rectangle((7.85,3.25),0.75,0.60,fc='#0e1a2d',ec='none',zorder=20))
    xfix=np.linspace(7.85,8.60,50)
    ax.plot(xfix,3.75+0.52*np.sin((xfix-6.9)*3.0),color='#f0a202',lw=1.5,zorder=20)
    ax.plot(xfix,3.0+0.52*np.sin((xfix-6.9)*3.0-0.85),color='#2cc7e8',lw=1.5,zorder=20)
    ax.text(8.15,3.52,'theta',color='white',fontsize=9,zorder=21)
    ax.add_patch(Rectangle((8.05,0.28),2.05,0.36,fc='white',ec='none',zorder=20))
    ax.text(9.0,0.45,'theta = 360 deg (Delta t / T)',ha='center',fontsize=9.5,color='#d9534f',zorder=21)
    fig.savefig(DIAG/'q2-ac-phase-rebuilt.png',dpi=320,bbox_inches='tight'); plt.close(fig)

redraw_clean_diagrams()
doc.build(story)
print(pdf_path)
