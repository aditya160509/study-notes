from io import BytesIO
from pathlib import Path
import re

import fitz
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
TMP = ROOT / "work" / "tmp" / "pdfs"
OUTPUTS.mkdir(parents=True, exist_ok=True)
TMP.mkdir(parents=True, exist_ok=True)


def span_origin(page: fitz.Page, rect: fitz.Rect) -> tuple[float, float]:
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                span_rect = fitz.Rect(span["bbox"])
                if span_rect.intersects(rect) and "Anita Balaji" in span.get("text", ""):
                    return tuple(span["origin"])
    raise RuntimeError("Could not find the original text baseline")


def replace_order_details() -> None:
    source = ROOT / "Order Details.pdf"
    target = OUTPUTS / "Order Details - Krishna Balaji.pdf"
    doc = fitz.open(source)
    page = doc[0]
    hits = page.search_for("Anita Balaji")
    if len(hits) != 1:
        raise RuntimeError(f"Expected one name in {source.name}, found {len(hits)}")

    font_bytes = doc.extract_font(5)[3]
    font_path = TMP / "AmazonEmber-Regular.ttf"
    font_path.write_bytes(font_bytes)
    old = hits[0]
    origin = span_origin(page, old)
    cover = fitz.Rect(old.x0 - 0.5, old.y0, old.x1 + 28, old.y1)
    page.add_redact_annot(cover, fill=(1, 1, 1))
    page.apply_redactions()
    page.insert_text(
        origin,
        "Krishna Balaji",
        fontfile=str(font_path),
        fontsize=7.5495,
        color=(0, 0, 0),
    )
    doc.save(target, garbage=4, deflate=True)
    doc.close()


def replace_invoice() -> None:
    source = ROOT / "invoice.pdf"
    target = OUTPUTS / "invoice - Krishna Balaji.pdf"
    doc = fitz.open(source)
    total_hits = 0
    for page in doc:
        for xref, _name, _invoker, _matrix in page.get_xobjects():
            stream = doc.xref_stream(xref)
            hits = stream.count(b"(Anita Balaji)") + stream.count(b"(Anita Balaji )")
            if hits:
                lines = stream.splitlines()
                for i, line in enumerate(lines[:-1]):
                    if not re.match(rb"^1 0 0 1 [0-9.]+ [0-9.]+ Tm$", line):
                        continue
                    text_line = lines[i + 1]
                    if text_line not in (b"(Anita Balaji)Tj", b"(Anita Balaji )Tj"):
                        continue
                    match = re.match(rb"^1 0 0 1 ([0-9.]+) ([0-9.]+) Tm$", line)
                    old_x = float(match.group(1))
                    old_width = fitz.get_text_length(
                        "Anita Balaji" if text_line == b"(Anita Balaji)Tj" else "Anita Balaji ",
                        fontname="helv",
                        fontsize=11.25,
                    )
                    new_width = fitz.get_text_length("Krishna Balaji", fontname="helv", fontsize=11.25)
                    new_x = old_x + old_width - new_width
                    lines[i] = re.sub(rb"^1 0 0 1 [0-9.]+ ", f"1 0 0 1 {new_x:.2f} ".encode(), line)
                    lines[i + 1] = b"(Krishna Balaji)Tj"
                updated = b"\n".join(lines)
                doc.update_stream(xref, updated)
                total_hits += hits
    if total_hits != 6:
        raise RuntimeError(f"Expected six names in {source.name}, found {total_hits}")
    doc.save(target, garbage=4, deflate=True)
    doc.close()


def replace_tax_invoice() -> None:
    source = ROOT / "tax-invoice-print-friendly.pdf"
    target = OUTPUTS / "tax-invoice-print-friendly - Krishna Balaji.pdf"
    doc = fitz.open(source)
    total_hits = 0
    old_text = b"(ANITA BALAJI) Tj"
    new_text = b"(KRISHNA BALAJI) Tj"
    old_width = fitz.get_text_length("ANITA BALAJI", fontname="hebo", fontsize=5.5)
    new_width = fitz.get_text_length("KRISHNA BALAJI", fontname="hebo", fontsize=5.5)
    for xref in doc[0].get_contents():
        stream = doc.xref_stream(xref)
        if old_text not in stream:
            continue
        lines = stream.splitlines()
        for i, line in enumerate(lines[:-1]):
            if line != old_text:
                continue
            baseline_index = next(
                (j for j in range(i - 1, -1, -1) if re.match(rb"^1 0 0 1 [0-9.]+ [0-9.]+ Tm$", lines[j])),
                None,
            )
            match = (
                re.match(rb"^(1 0 0 1 )([0-9.]+)( [0-9.]+ Tm)$", lines[baseline_index])
                if baseline_index is not None
                else None
            )
            if not match:
                raise RuntimeError("Could not locate the tax invoice name baseline")
            old_x = float(match.group(2))
            new_x = old_x + old_width - new_width
            lines[baseline_index] = match.group(1) + f"{new_x:.2f}".encode() + match.group(3)
            lines[i] = new_text
            total_hits += 1
        doc.update_stream(xref, b"\n".join(lines))
    if total_hits != 1:
        raise RuntimeError(f"Expected one name in {source.name}, found {total_hits}")
    doc.save(target, garbage=4, deflate=True)
    doc.close()


def replace_addendum() -> None:
    source = ROOT / "e46f28c0-14a2-4531-afec-0dcf226a6a2f.pdf"
    target = OUTPUTS / "e46f28c0-14a2-4531-afec-0dcf226a6a2f - Krishna Balaji.pdf"
    source_doc = fitz.open(source)
    source_page = source_doc[0]
    images = source_page.get_images(full=True)
    if len(images) != 1:
        raise RuntimeError(f"Expected one embedded image in {source.name}, found {len(images)}")
    image_info = source_doc.extract_image(images[0][0])
    image = Image.open(BytesIO(image_info["image"])).convert("RGB")
    draw = ImageDraw.Draw(image)
    font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"
    font = ImageFont.truetype(font_path, 17)

    # OCR inspection identified the two billing/shipping name lines in the embedded image.
    for x0, y0, x1, y1 in ((47, 672, 160, 693), (590, 672, 705, 693)):
        draw.rectangle((x0, y0, x1, y1), fill="white")
        draw.text((x0 + 2, y0 - 1), "Krishna Balaji", font=font, fill="black")

    image_buffer = BytesIO()
    image.save(image_buffer, format="PNG")
    image_bytes = image_buffer.getvalue()
    image_rect = source_page.get_image_rects(images[0][0])[0]
    out = fitz.open()
    page = out.new_page(width=source_page.rect.width, height=source_page.rect.height)
    page.insert_image(image_rect, stream=image_bytes)
    out.set_metadata(source_doc.metadata)
    out.save(target, garbage=4, deflate=True)
    out.close()
    source_doc.close()


def replace_duplicate_invoice() -> None:
    source = ROOT / "duplicate-invoice-original-print-friendly.pdf"
    target = OUTPUTS / "duplicate-invoice-original-print-friendly - Krishna Balaji.pdf"
    doc = fitz.open(source)
    page = doc[0]

    # The customer name is outlined as vector artwork rather than searchable text.
    # OCR inspection at 288 dpi located ANITA at approximately (324, 107)-(353, 114) pt.
    old_rect = fitz.Rect(323.0, 106.0, 355.0, 116.0)
    page.draw_rect(old_rect, color=(1, 1, 1), fill=(1, 1, 1), overlay=True)
    page.insert_text(
        (324.25, 115.0),
        "KRISHNA BALAJI",
        fontname="helv",
        fontsize=11.25,
        color=(0, 0, 0),
        overlay=True,
    )
    doc.save(target, garbage=4, deflate=True)
    doc.close()


replace_order_details()
replace_invoice()
replace_tax_invoice()
replace_addendum()
replace_duplicate_invoice()
print("Created corrected PDFs in", OUTPUTS)
