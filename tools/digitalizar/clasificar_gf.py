import os
import json
import io
import time
from pathlib import Path
from PIL import Image
import pillow_heif
from google import genai
from google.genai import types
from dotenv import load_dotenv

pillow_heif.register_heif_opener()
load_dotenv("/home/checa/Projects/javiercheca10.github.io/.env")

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY no encontrada")

client = genai.Client(api_key=API_KEY)

FOTOS_DIR = Path("/home/checa/FotosUniversidad/Gestion Fiscal de la Empresa")
heic_files = sorted([f for f in os.listdir(FOTOS_DIR) if f.upper().endswith(".HEIC")])

print(f"Fotos HEIC encontradas ({len(heic_files)}): {heic_files}")

PROMPT_CLASIFICACION = """
Actúa como un profesor universitario experto en Gestión Fiscal de la Empresa y Derecho Tributario (Grado en ADE).

Examina estas 14 fotos de apuntes manuscritos de la carpeta 'Gestion Fiscal de la Empresa' del alumno en el programa de movilidad SICUE en Valencia.
Analiza con precisión qué temas, bloques teóricos, leyes (LGT, IRPF, IVA, IS, etc.) y ejercicios o liquidaciones tributarias cubren estas 14 hojas.

Devuelve un JSON estrictamente estructurado con:
{
  "asignatura": "Gestión Fiscal de la Empresa",
  "codigo_sugerido": "GFE",
  "documentos": [
    {
      "id": "identificador_slug_limpio",
      "titulo": "Título formal del documento o tema",
      "tipo": "TEORÍA / PRÁCTICA / RESUMEN",
      "archivos": ["IMG_xxxx.HEIC"],
      "resumen": "Resumen técnico detallado de su contenido (conceptos clave, leyes, hechos imponibles, bases imponibles, deducciones, fórmulas, modelos tributarios)."
    }
  ],
  "detalle_por_archivo": [
    {
      "archivo": "IMG_xxxx.HEIC",
      "tema": "Tema y título exacto que aparece en la hoja",
      "resumen": "Descripción concisa del contenido de la hoja"
    }
  ]
}
"""

parts = []
for f_name in heic_files:
    p = FOTOS_DIR / f_name
    img = Image.open(p).convert("RGB")
    max_size = 1400
    if max(img.size) > max_size:
        ratio = max_size / max(img.size)
        new_size = (int(img.width * ratio), int(img.height * ratio))
        img = img.resize(new_size, Image.Resampling.LANCZOS)
    
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=80)
    jpeg_bytes = buf.getvalue()
    
    parts.append(f"FOTO: {f_name}")
    parts.append(types.Part.from_bytes(data=jpeg_bytes, mime_type="image/jpeg"))

parts.append(PROMPT_CLASIFICACION)

models_to_try = [
    "gemini-3.7-flash",
    "gemini-3.5-flash",
    "gemini-3.8-flash",
    "gemini-3.1-flash-lite"
]

res = None
for m in models_to_try:
    try:
        print(f"Clasificando con {m}...")
        res = client.models.generate_content(
            model=m,
            contents=parts,
            config=types.GenerateContentConfig(response_mime_type="application/json")
        )
        if res.text:
            print(f"✅ Respuesta recibida de {m}")
            break
    except Exception as e:
        print(f"  Fallo con {m}: {str(e)[:140]}")
        time.sleep(2)

if not res or not res.text:
    raise RuntimeError("No se obtuvo respuesta de ningún modelo")

out_json = Path("/home/checa/Projects/javiercheca10.github.io/tools/digitalizar/clasificacion_gf.json")
with open(out_json, "w", encoding="utf-8") as f:
    f.write(res.text)

print(f"Guardado exitosamente en {out_json}")
