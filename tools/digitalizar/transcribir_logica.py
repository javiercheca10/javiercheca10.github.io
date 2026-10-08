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

FOTOS_DIR = Path("/home/checa/FotosUniversidad/logica")
PUBLIC_LMD = Path("/home/checa/Projects/javiercheca10.github.io/public/subjects/LMD")

PROMPT_TRANSCRIBIR = """
Eres un profesor catedrático universitario de la Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación (ETSIIT, Universidad de Granada) y experto en Lógica Matemática, Álgebra de Boole, Métodos Discretos y Teoría de la Computación.

Estás transcribiendo un bloque de apuntes manuscritos oficiales de la asignatura 'Lógica y Métodos Discretos' (LMD).
Se te proporciona una secuencia ordenada de páginas manuscritas que forman este documento: '{titulo_bloque}'.

PAUTAS EDITORIALES DE MÁXIMA CALIDAD:
1. Formato de Salida: Markdown impecable con soporte matemático KaTeX LaTeX completo.
2. Fórmulas Matemáticas y Notación Lógica:
   - Símbolos en línea con $...$: negación $\\neg P$, conjunción $P \\land Q$, disyunción $P \\lor Q$, implicación $P \\to Q$, doble implicación $P \\leftrightarrow Q$, cuantificadores $\\forall x$, $\\exists x$, consecuencia lógica $\\Sigma \\models \\varphi$, tautología $\\models \\varphi$, equivalencia $\\varphi \\equiv \\psi$.
   - Fórmulas destacadas con $$...$$: tablas de verdad, árboles de formación, derivaciones semánticas, sistemas de recurrencias lineales (`\\begin{{cases}} ... \\end{{cases}}`), matrices de Sylvester para cuadráticas y formas normales de Skolem.
3. Tablas y Algoritmos:
   - Para mapas de Karnaugh, tablas de verdad, minterms/maxterms de Quine-McCluskey o trazas del algoritmo de Davis-Putnam / algoritmos de grafos (Kruskal, Prim, Hakimi), genera tablas Markdown elegantes y claras o bloques de pseudocódigo.
4. Integridad y Rigor:
   - Transcribe íntegramente todo el contenido técnico, demostraciones, propiedades, teoremas, ejemplos y enunciados de ejercicios resueltos.
   - Si hay notas al margen explicativas o aclaraciones, agrúpalas como notas editoriales (`> **Nota:** ...`).
   - Redacción pulcra, profesional y rigurosa en español universitario.

Estructura tu respuesta empezando directamente con el título de nivel 1:
# {titulo_bloque}
"""

def transcribir_bloque(subpath_destino, titulo_bloque, lista_archivos):
    out_file = PUBLIC_LMD / subpath_destino
    if out_file.exists() and out_file.stat().st_size > 300:
        print(f"\n--- {subpath_destino} ya existe ({out_file.stat().st_size} bytes). Saltando... ---")
        return

    print(f"\n--- Transcribiendo {subpath_destino}: {titulo_bloque} ({len(lista_archivos)} páginas) ---")
    
    parts = []
    for f_name in lista_archivos:
        img_path = FOTOS_DIR / f_name
        print(f"  Abriendo {f_name}...")
        img = Image.open(img_path)
        img = img.convert("RGB")
        max_size = 2000
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
        "gemini-3.6-flash",
        "gemini-3.5-flash-lite",
        "gemini-3.1-flash-lite",
        "gemini-3-flash-preview"
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
        print("  Esperando 6s antes de reintentar generación...")
        time.sleep(6)

    if not res or not res.text:
        raise RuntimeError(f"No se pudo transcribir {subpath_destino}")

    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(res.text, encoding="utf-8")
    print(f"  ✅ Guardado en {out_file} ({len(res.text)} caracteres)")

def main():
    # 1. Examen Oficial (IMG_1018)
    transcribir_bloque(
        "examenes/examen_ordinaria_junio_2023.md",
        "Examen Oficial de Lógica y Métodos Discretos (19 de Junio de 2023)",
        ["IMG_1018.HEIC"]
    )
    time.sleep(2)

    # 2. Formulario y Resumen de Reglas (IMG_1028, IMG_1029, IMG_1034, IMG_1035, IMG_1043, IMG_1044)
    transcribir_bloque(
        "formulario_resumen_reglas.md",
        "Formulario Maestro de Lógica, Álgebra de Boole y Métodos Discretos",
        ["IMG_1028.HEIC", "IMG_1029.HEIC", "IMG_1034.HEIC", "IMG_1035.HEIC", "IMG_1043.HEIC", "IMG_1044.HEIC"]
    )
    time.sleep(2)

    # 3. Tema 1: Lógica Proposicional (IMG_1030, IMG_1031, IMG_1032, IMG_1033)
    transcribir_bloque(
        "tema1_logica_proposicional.md",
        "Tema 1: Lógica Proposicional (Sintaxis, Semántica y Consecuencia)",
        ["IMG_1030.HEIC", "IMG_1031.HEIC", "IMG_1032.HEIC", "IMG_1033.HEIC"]
    )
    time.sleep(2)

    # 4. Tema 2: Lógica de Primer Orden (IMG_1036, IMG_1037, IMG_1038, IMG_1039, IMG_1040, IMG_1041, IMG_1042)
    transcribir_bloque(
        "tema2_logica_primer_orden.md",
        "Tema 2: Lógica de Primer Orden (Estructuras, Modelos, Prenexas y Skolem)",
        ["IMG_1036.HEIC", "IMG_1037.HEIC", "IMG_1038.HEIC", "IMG_1039.HEIC", "IMG_1040.HEIC", "IMG_1041.HEIC", "IMG_1042.HEIC"]
    )
    time.sleep(2)

    # 5. Tema 3: Métodos de Demostración y Davis-Putnam (IMG_1023, IMG_1024)
    transcribir_bloque(
        "tema3_metodos_demostracion.md",
        "Tema 3: Métodos de Demostración (Davis-Putnam e Inducción Matemática)",
        ["IMG_1023.HEIC", "IMG_1024.HEIC"]
    )
    time.sleep(2)

    # 6. Ejercicios Resueltos de Examen (IMG_1019, IMG_1020, IMG_1021, IMG_1022, IMG_1025, IMG_1026, IMG_1027)
    transcribir_bloque(
        "ejercicios_resueltos_examen.md",
        "Colección de Ejercicios Resueltos de Examen (Recurrencias, Grafos y Davis-Putnam)",
        ["IMG_1019.HEIC", "IMG_1020.HEIC", "IMG_1021.HEIC", "IMG_1022.HEIC", "IMG_1025.HEIC", "IMG_1026.HEIC", "IMG_1027.HEIC"]
    )

    print("\n🎉 ¡Todos los documentos de LMD han sido transcritos con éxito!")

if __name__ == "__main__":
    main()
