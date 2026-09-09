from pathlib import Path
from pypdf import PdfReader, PdfWriter, Transformation

base = Path('/Users/adityabalaji/Documents/Codex/2026-08-31/ch')
out = base / 'output' / 'pdf'
out.mkdir(parents=True, exist_ok=True)

A4_W, A4_H = 595.28, 841.89

def make_a4(src_name, dst_name, enlarge=False):
    reader = PdfReader(str(base / src_name))
    page = reader.pages[0]
    box = page.mediabox
    w, h = float(box.width), float(box.height)
    writer = PdfWriter()
    if enlarge:
        margin = 24
        scale = min((A4_W - 2*margin) / w, (A4_H - 2*margin) / h)
        tx = (A4_W - w*scale) / 2
        ty = (A4_H - h*scale) / 2
        new_page = writer.add_blank_page(width=A4_W, height=A4_H)
        new_page.merge_transformed_page(page, Transformation().scale(scale).translate(tx, ty))
    else:
        writer.add_page(page)
    with open(out / dst_name, 'wb') as f:
        writer.write(f)

make_a4('8813bbe6-43ae-4c68-a591-65bbc488d28a.pdf', 'tax-invoice-print-friendly.pdf', enlarge=True)
make_a4('b47b83c0-6795-48a3-9d9d-35c276e03331 (1).pdf', 'duplicate-invoice-print-friendly.pdf', enlarge=False)
make_a4('b47b83c0-6795-48a3-9d9d-35c276e03331.pdf', 'duplicate-invoice-original-print-friendly.pdf', enlarge=False)
