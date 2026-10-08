import os
import json
import io
import time
from pathlib import Path
from PIL import Image
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv("/home/checa/Projects/javiercheca10.github.io/.env")

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY no encontrada")

client = genai.Client(api_key=API_KEY)

SCRATCH_DIR = Path("/home/checa/.gemini/antigravity-cli/brain/04bd58e4-b9bf-495e-990a-96f7ab2a417b/scratch/algebra")
PUBLIC_AA = Path("/home/checa/Projects/javiercheca10.github.io/public/subjects/AA")
PUBLIC_AA.mkdir(parents=True, exist_ok=True)

PROMPT_TRANSCRIBIR = """
Eres un profesor universitario de Álgebra Aplicada y Métodos Computacionales (Applied Algebra / Applied Linear Algebra, VMLS Stanford).

Estás transcribiendo y formateando el portafolio de ejercicios y problemas resueltos de la asignatura cursada en el programa Erasmus: '{titulo_bloque}'.

DIRECTRICES TÉCNICAS:
1. Formato de Salida: Markdown impecable con KaTeX para todas las expresiones matemáticas ($...$ para inline, $$...$$ para display math).
2. REGLA ESTRICTA DE LIMPIEZA:
   - NUNCA incluyas frases como "Escaneado con CamScanner", marcas de agua de digitalización o números de página del escáner en el texto final.
3. Rigor Matemático:
   - Presenta cada ejercicio con su enunciado claro, definición formal de vectores/matrices, dimensiones, hipótesis y demostración o desarrollo paso a paso.
   - Utiliza notación vectorial y matricial estándar: matrices en mayúsculas $A, B$, vectores en minúsculas $x, y \in \mathbb{{R}}^n$, vectores columna, productos internos $x^T y$, normas $\|x\|_2$, matrices traspuestas $A^T$, inversas $A^{{-1}}$, etc.
   - Si hay interpretaciones aplicadas (ej. bolsa, procesado de señales, modelos de encuesta, Ley de Moore, mínimos cuadrados), detalla la justificación intuitiva y el modelo matemático subyacente.
4. Idioma: Español formal académico y técnico (manteniendo términos en inglés reconocibles entre paréntesis si procede: Least Squares, Skew-symmetric, Nearest Neighbor, Down-sampling).

Estructura tu respuesta empezando directamente con el título de nivel 1:
# {titulo_bloque}
"""

def transcribir_bloque(subpath_destino, titulo_bloque, lista_archivos):
    out_file = PUBLIC_AA / subpath_destino
    if out_file.exists() and out_file.stat().st_size > 1000:
        print(f"\n--- {subpath_destino} ya existe ({out_file.stat().st_size} bytes). Saltando... ---")
        return

    print(f"\n--- Transcribiendo {subpath_destino}: {titulo_bloque} ({len(lista_archivos)} páginas) ---")
    
    parts = []
    for f_name in lista_archivos:
        img_path = SCRATCH_DIR / f_name
        print(f"  Abriendo {f_name}...")
        img = Image.open(img_path)
        img = img.convert("RGB")
        max_size = 1800
        if max(img.size) > max_size:
            ratio = max_size / max(img.size)
            new_size = (int(img.width * ratio), int(img.height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
        
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=88)
        jpeg_bytes = buf.getvalue()
        
        parts.append(f"--- PÁGINA: {f_name} ---")
        parts.append(types.Part.from_bytes(data=jpeg_bytes, mime_type="image/jpeg"))

    prompt = PROMPT_TRANSCRIBIR.format(titulo_bloque=titulo_bloque)
    parts.append(prompt)

    models_to_try = [
        "gemini-3.5-flash-lite",
        "gemini-3.1-flash-lite",
        "gemini-3-flash-preview",
        "gemini-3.6-flash"
    ]
    
    res = None
    for attempt in range(4):
        for model_name in models_to_try:
            try:
                print(f"  Intento {attempt+1} generando con {model_name}...")
                res = client.models.generate_content(
                    model=model_name,
                    contents=parts,
                )
                if res.text:
                    print(f"  ✅ Recibida respuesta de {model_name}")
                    break
            except Exception as e:
                print(f"    Fallo con {model_name}: {str(e)[:120]}")
                time.sleep(3)
        if res and res.text:
            break
        print("  Esperando 5s antes de reintentar...")
        time.sleep(5)

    if not res or not res.text:
        raise RuntimeError(f"No se pudo transcribir {subpath_destino}")

    texto_limpio = res.text
    for linea in ["Escaneado con CamScanner", "Escaneado con Camscanner", "CamScanner", "Scanned with CamScanner"]:
        texto_limpio = texto_limpio.replace(linea, "")

    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(texto_limpio, encoding="utf-8")
    print(f"  ✅ Guardado en {out_file} ({len(texto_limpio)} caracteres)")

def main():
    # Bloque 1: Vectores, Funciones Lineales, Normas e Independencia Lineal (Páginas 2 a 9)
    paginas_bloque1 = [f"page_{i:02d}.jpg" for i in range(2, 10)]
    transcribir_bloque(
        "bloque1_vectores_normas_independencia.md",
        "Bloque 1: Vectores, Funciones Lineales, Distancias e Independencia Lineal (Capítulos 1-5)",
        paginas_bloque1
    )
    time.sleep(2)

    # Bloque 2: Matrices, Inversas y Ajuste por Mínimos Cuadrados (Páginas 10 a 25)
    paginas_bloque2 = [f"page_{i:02d}.jpg" for i in range(10, 26)]
    transcribir_bloque(
        "bloque2_matrices_inversas_minimos_cuadrados.md",
        "Bloque 2: Álgebra Matricial, Inversas y Ajuste por Mínimos Cuadrados / Ley de Moore (Capítulos 6-13)",
        paginas_bloque2
    )

    print("\n🎉 ¡Todos los bloques de Applied Algebra han sido transcritos con éxito!")

if __name__ == "__main__":
    main()
