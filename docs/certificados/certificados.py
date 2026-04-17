import fitz  # pymupdf
import os
import re

def normalize_filename(name: str) -> str:
    """Convierte a minúsculas y reemplaza espacios/símbolos por guiones bajos."""
    name = name.lower()
    name = re.sub(r"\.pdf$", "", name)              # quitar extensión
    name = re.sub(r"[^a-z0-9]+", "_", name)         # todo lo no válido → _
    name = re.sub(r"_+", "_", name)                 # evitar múltiples _
    return name.strip("_") + ".png"

pdf_folder = "../certificados"
img_folder = "../images/certificados"
os.makedirs(img_folder, exist_ok=True)

for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith(".pdf"):
        doc = fitz.open(os.path.join(pdf_folder, pdf_file))
        page = doc[0]
        pix = page.get_pixmap(dpi=200)

        img_name = normalize_filename(pdf_file)
        pix.save(os.path.join(img_folder, img_name))

        print(f"✅ {img_name} generado")
        doc.close()