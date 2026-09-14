"""
Fusiona plantilla_8_correos.md con leads.csv para generar una secuencia de 8
correos personalizada por contacto.

Uso: python3 generar_secuencia.py
Lee:   ../leads.csv, plantilla_8_correos.md
Escribe: secuencia_personalizada.csv (127 filas x 8 asunto/cuerpo)
"""
import csv
import re
from pathlib import Path

BASE = Path(__file__).parent
LEADS_CSV = BASE.parent / "leads.csv"
TEMPLATE_MD = BASE / "plantilla_8_correos.md"
OUT_CSV = BASE / "secuencia_personalizada.csv"


def parse_template(text: str):
    """Split the template into 8 (asunto, cuerpo) blocks."""
    blocks = re.split(r"^## CORREO \d+\s*$", text, flags=re.MULTILINE)[1:]
    emails = []
    for block in blocks:
        m = re.search(r"\*\*Asunto:\*\*\s*(.+)", block)
        asunto = m.group(1).strip()
        cuerpo = block[m.end():].strip()
        cuerpo = cuerpo.split("\n-----", 1)[0].strip()
        emails.append((asunto, cuerpo))
    assert len(emails) == 8, f"esperaba 8 correos, encontré {len(emails)}"
    return emails


def saludo_for(nombre_contacto: str, empresa: str) -> str:
    nombre_contacto = (nombre_contacto or "").strip()
    if nombre_contacto:
        primer_nombre = nombre_contacto.split()[0]
        return f"Hola {primer_nombre},"
    return f"Hola equipo de {empresa.strip()},"


def render(text: str, saludo: str, institucion: str) -> str:
    return text.replace("{{SALUDO}}", saludo).replace("{{INSTITUCION}}", institucion.strip())


def main():
    template_text = TEMPLATE_MD.read_text(encoding="utf-8")
    emails = parse_template(template_text)

    with LEADS_CSV.open(newline="", encoding="utf-8") as fh:
        leads = list(csv.DictReader(fh))

    fieldnames = [
        "Empresa", "Pais", "Nombre_Contacto", "Cargo", "Email",
        "Confianza",
    ]
    for i in range(1, 9):
        fieldnames += [f"Correo_{i}_Asunto", f"Correo_{i}_Cuerpo"]

    rows_out = []
    for lead in leads:
        saludo = saludo_for(lead["Nombre_Contacto"], lead["Empresa"])
        row = {
            "Empresa": lead["Empresa"],
            "Pais": lead["Pais"],
            "Nombre_Contacto": lead["Nombre_Contacto"],
            "Cargo": lead["Cargo"],
            "Email": lead["Email"],
            "Confianza": lead["Confianza"],
        }
        for i, (asunto, cuerpo) in enumerate(emails, start=1):
            row[f"Correo_{i}_Asunto"] = render(asunto, saludo, lead["Empresa"])
            row[f"Correo_{i}_Cuerpo"] = render(cuerpo, saludo, lead["Empresa"])
        rows_out.append(row)

    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows_out)

    print(f"Escribí {len(rows_out)} filas x 8 correos en {OUT_CSV}")


if __name__ == "__main__":
    main()
