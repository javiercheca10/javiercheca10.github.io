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

FOTOS_DIR = Path("/home/checa/FotosUniversidad/FBD")
files = sorted([f for f in os.listdir(FOTOS_DIR) if f.upper().endswith(".HEIC")])

print(f"Detectadas {len(files)} fotos en {FOTOS_DIR}:")
print(files)

PROMPT_CLASIFICACION = """
Actúa como un profesor catedrático universitario de la asignatura 'Fundamentos de Bases de Datos' (FBD) en la ETSIIT UGR.

El alumno dispone de 32 folios manuscritos correspondientes a la asignatura de Bases de Datos (Modelo Entidad-Relación E/R, Modelo Relacional, Álgebra Relacional, SQL / DDL / DML, Normalización: 1FN, 2FN, 3FN, BCNF, Dependencias Funcionales, etc.).

INSTRUCCIONES CLAVE DEL ALUMNO:
- Las hojas están ordenadas cronológicamente por temas.
- Al final de cada tema o bloque hay un pequeño "formulario", resumen de sintaxis, reglas de transformación o chuletario de ese tema.

Por favor, examina las 32 fotos ordenadas de IMG_1086 a IMG_1117 y agrúpalas en bloques temáticos coherentes donde cada bloque contenga sus páginas de desarrollo seguidas de su correspondiente formulario/resumen si lo tiene.

Ignora y omite cualquier mención a "Escaneado con CamScanner".

Devuelve EXCLUSIVAMENTE un objeto JSON válido con la siguiente estructura:
{
  "bloques": [
    {
      "id": "identificador_limpio",
      "titulo": "Título formal del tema / bloque",
      "tipo": "TEORÍA / FORMULARIO",
      "archivos": ["IMG_xxxx.HEIC", "..."],
      "tiene_formulario": true/false,
      "resumen": "Resumen conciso del contenido que cubre este bloque."
    }
  ],
  "detalle_por_archivo": [
    {
      "archivo": "IMG_xxxx.HEIC",
      "tema": "...",
      "es_formulario": true/false,
      "resumen": "..."
    }
  ]
}
"""

def main():
    parts = []
    print("\nOptimizando y preparando 32 imágenes para clasificación...")
    for f_name in files:
        p = FOTOS_DIR / f_name
        img = Image.open(p)
        img = img.convert("RGB")
        max_size = 1200
        if max(img.size) > max_size:
            ratio = max_size / max(img.size)
            new_size = (int(img.width * ratio), int(img.height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
        
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=78)
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
    for attempt in range(4):
        for model_name in models_to_try:
            try:
                print(f"Intento {attempt+1} consultando a {model_name}...")
                res = client.models.generate_content(
                    model=model_name,
                    contents=parts,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json"
                    )
                )
                if res.text:
                    print(f"✅ Respuesta recibida de {model_name}")
                    break
            except Exception as e:
                print(f"  Fallo con {model_name}: {str(e)[:120]}")
                time.sleep(2)
        if res and res.text:
            break
        print("Esperando 5s antes de reintentar...")
        time.sleep(5)

    if not res or not res.text:
        raise RuntimeError("No se obtuvo respuesta de clasificación de FBD")

    out_json = Path("/home/checa/Projects/javiercheca10.github.io/tools/digitalizar/clasificacion_fbd.json")
    with open(out_json, "w", encoding="utf-8") as f:
        f.write(res.text)

    print(f"\n✅ Clasificación de FBD guardada en {out_json}")

if __name__ == "__main__":
    main()
