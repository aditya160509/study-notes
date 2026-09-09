from pathlib import Path
from pypdf import PdfReader, PdfWriter, Transformation

downloads = Path('/Users/adityabalaji/Downloads')
out = Path('/Users/adityabalaji/Documents/Codex/2026-08-31/ch/output/pdf/all-print-friendly')
out.mkdir(parents=True, exist_ok=True)
A4_W, A4_H, MARGIN = 595.28, 841.89, 18

for src in sorted(downloads.glob('*.pdf')):
    try:
        reader = PdfReader(str(src), strict=False)
        if not reader.pages:
            continue
    except Exception:
        continue
    writer = PdfWriter()
    for page in reader.pages:
        w, h = float(page.mediabox.width), float(page.mediabox.height)
        scale = min((A4_W - 2*MARGIN) / w, (A4_H - 2*MARGIN) / h)
        tx, ty = (A4_W - w*scale)/2, (A4_H - h*scale)/2
        dest = writer.add_blank_page(width=A4_W, height=A4_H)
        dest.merge_transformed_page(page, Transformation().scale(scale).translate(tx, ty))
    target = out / f'{src.stem}-A4-print.pdf'
    with target.open('wb') as f:
        writer.write(f)
    print(target.name, len(writer.pages))
