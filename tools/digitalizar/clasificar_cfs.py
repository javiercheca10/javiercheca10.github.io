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

FOTOS_DIR = Path("/home/checa/FotosUniversidad/Contabilidad financiera y de sociedades")
heic_files = sorted([f for f in os.listdir(FOTOS_DIR) if f.upper().endswith(".HEIC")])

print(f"Fotos HEIC encontradas ({len(heic_files)}): {heic_files}")

PROMPT_CLASIFICACION = """
Actúa como un profesor universitario experto en Contabilidad Financiera y Contabilidad de Sociedades (Grado en ADE).

Examina estas 10 fotos manuscritas de la carpeta 'Contabilidad financiera y de sociedades'.
El alumno cursa el programa de movilidad SICUE en Valencia.
Indica de qué tratan estas 10 hojas (ej. constitución de sociedades, aportaciones dinerarias y no dinerarias, ampliaciones y reducciones de capital, emisión de acciones, empréstitos de obligaciones, aplicación del resultado, dividendos, etc.).

Devuelve un JSON con:
{
  "documentos": [
    {
      "id": "identificador_limpio",
      "titulo": "Título formal del documento",
      "tipo": "TEORÍA / EJERCICIOS / CUENTAS",
      "archivos": ["IMG_xxxx.HEIC"],
      "resumen": "Resumen técnico de su contenido contable (asientos del PGC, cuentas utilizadas, normativa)."
    }
  ],
  "detalle_por_archivo": [
    {
      "archivo": "IMG_xxxx.HEIC",
      "tema": "...",
      "resumen": "..."
    }
  ]
}
"""

parts = []
for f_name in heic_files:
    p = FOTOS_DIR / f_name
    img = Image.open(p)
    img = img.convert("RGB")
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
    "gemini-3.6-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-3-flash-preview"
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
        print(f"  Fallo con {m}: {str(e)[:120]}")
        time.sleep(2)

out_json = Path("/home/checa/Projects/javiercheca10.github.io/tools/digitalizar/clasificacion_cfs.json")
with open(out_json, "w", encoding="utf-8") as f:
    f.write(res.text)

print(f"Guardado en {out_json}")
