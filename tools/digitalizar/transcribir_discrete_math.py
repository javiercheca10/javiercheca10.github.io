import os
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

PAGES_DIR = Path("/tmp/dm_pages")
PUBLIC_DM = Path("/home/checa/Projects/javiercheca10.github.io/public/subjects/DM")
PUBLIC_DM.mkdir(parents=True, exist_ok=True)

PROMPT_TRANSCRIBIR = """
Eres un profesor universitario de Matemáticas Discretas y Computación Teórica (Discrete Mathematics, Kenneth H. Rosen).

Estás transcribiendo y formateando el portafolio de ejercicios y problemas resueltos de la asignatura cursada en el programa Erasmus en Atenas (Universidad del Pireo / UniPi): '{titulo_bloque}'.

DIRECTRICES TÉCNICAS Y EDITORIALES:
1. Formato de Salida: Markdown estructurado e impecable con KaTeX para todas las expresiones matemáticas ($...$ para inline y $$...$$ para display math).
2. REGLA ESTRICTA DE LIMPIEZA:
   - NUNCA incluyas frases como "Escaneado con CamScanner", marcas de agua de digitalización o números de página del escáner físico.
3. Rigor Matemático y Pedagógico:
   - Presenta cada ejercicio con su referencia textual exacta del libro de Rosen (ej. *Sección 1.1, Ejercicio 39; Sección 1.3, Ejercicio 55; Sección 4.3, Ejercicio 41; Sección 6.4, Ejercicio 26*).
   - Enuncia el problema formalmente y desglosa la solución paso a paso.
   - En lógica: incluye tablas de verdad completas en Markdown con columnas $p$, $q$, $r$, subexpresiones y resultado final, demostraciones por resolución derivando la cláusula vacía $\\square$.
   - En teoría de números: Algoritmo de Euclides Extendido paso a paso para el $\\text{{mcd}}(a, b)$, sustitución regresiva para hallar coeficientes de Bézout, inversos modulares y Pequeño Teorema de Fermat.
   - En inducción: Caso base, hipótesis inductiva y paso inductivo justificado rigurosamente.
   - En combinatoria: Justificación formal del modelo de conteo (permutaciones con/sin repetición, combinaciones, principio de inclusión-exclusión, principio del palomar / Pigeonhole Principle, método de barras y estrellas / Stars and Bars, y demostración combinatoria y algebraica de identidades binomiales).
4. Idioma: Español formal académico y riguroso, manteniendo términos técnicos en inglés entre paréntesis donde enriquezca la lectura académica Erasmus (ej. Truth Table, Resolution, Pigeonhole Principle, Stars and Bars, Extended Euclidean Algorithm).

Estructura tu respuesta empezando directamente con el título de nivel 1:
# {titulo_bloque}
"""

def transcribir_bloque(subpath_destino, titulo_bloque, paginas):
    out_file = PUBLIC_DM / subpath_destino
    if out_file.exists() and out_file.stat().st_size > 1000:
        print(f"\n--- {subpath_destino} ya existe ({out_file.stat().st_size} bytes). Saltando... ---")
        return

    print(f"\n--- Transcribiendo {subpath_destino}: {titulo_bloque} ({len(paginas)} páginas) ---")
    
    parts = []
    for p in paginas:
        img_path = PAGES_DIR / f"page-{p:02d}.png"
        img = Image.open(img_path).convert("RGB")
        max_size = 1400
        if max(img.size) > max_size:
            ratio = max_size / max(img.size)
            new_size = (int(img.width * ratio), int(img.height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
        
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=80)
        jpeg_bytes = buf.getvalue()
        
        parts.append(f"--- PÁGINA DEL CUADERNO {p} ---")
        parts.append(types.Part.from_bytes(data=jpeg_bytes, mime_type="image/jpeg"))

    prompt = PROMPT_TRANSCRIBIR.format(titulo_bloque=titulo_bloque)
    parts.append(prompt)

    models_to_try = [
        "gemini-3.8-flash",
        "gemini-3.1-flash-lite",
        "gemini-3.7-flash",
        "gemini-flash-latest"
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
                time.sleep(2)
        if res and res.text:
            break
        print("  Esperando 4s antes de reintentar...")
        time.sleep(4)

    if not res or not res.text:
        raise RuntimeError(f"No se pudo transcribir {subpath_destino}")

    texto_limpio = res.text
    for linea in ["Escaneado con CamScanner", "Escaneado con Camscanner", "CamScanner", "Scanned with CamScanner"]:
        texto_limpio = texto_limpio.replace(linea, "")

    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(texto_limpio, encoding="utf-8")
    print(f"  ✅ Guardado en {out_file} ({len(texto_limpio)} caracteres)")

def main():
    # Bloque 1: Lógica Proposicional, Equivalencias y Demostraciones por Resolución (Págs 2 a 9)
    transcribir_bloque(
        "bloque1_logica_equivalencias_resolucion.md",
        "Bloque 1: Lógica Proposicional, Tablas de Verdad, Tautologías y Demostraciones por Resolución",
        list(range(2, 10))
    )
    time.sleep(3)

    # Bloque 2: Teoría de Números, Aritmética Modular e Inducción Matemática (Págs 10 a 16)
    transcribir_bloque(
        "bloque2_teoria_numeros_induccion.md",
        "Bloque 2: Teoría de Números, Algoritmo de Euclides Extendido, Inversos Modulares e Inducción Matemática",
        list(range(10, 17))
    )
    time.sleep(3)

    # Bloque 3: Principios de Conteo, Combinatoria Avanzada y Demostraciones (Págs 17 a 28)
    transcribir_bloque(
        "bloque3_combinatoria_conteo_demostraciones.md",
        "Bloque 3: Principios de Conteo, Combinatoria, Principio del Palomar y Demostraciones de Identidades",
        list(range(17, 29))
    )

    print("\n🎉 ¡Todos los bloques de Discrete Mathematics han sido transcritos con éxito!")

if __name__ == "__main__":
    main()
