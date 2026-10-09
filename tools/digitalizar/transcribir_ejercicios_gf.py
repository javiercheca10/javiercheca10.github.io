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

TMP_DIR = Path("/tmp/gf_ejercicios")
PUBLIC_GFE = Path("/home/checa/Projects/javiercheca10.github.io/public/subjects/GFE")

PROMPT_TRANSCRIBIR_IVA = """
Eres un catedrático de Derecho Tributario y Gestión Fiscal en la Universidad de Valencia.
Estás transcribiendo y formalizando con la máxima calidad y rigor académico la colección de ejercicios de examen resueltos de:
'CASOS PRÁCTICOS DE EXAMEN: IVA - REGLA DE PRORRATA, REGULARIZACIÓN DE BIENES DE INVERSIÓN, MODELO 303 Y CONTABILIZACIÓN'

Las imágenes corresponden a las páginas 2 a 15 del cuaderno de ejercicios de exámenes oficiales:
- Examen Enero 2025 - Modelo A (págs. 2 a 4)
- Examen Enero 2025 - Modelo B (págs. 5 a 7)
- Examen Recuperación Enero 2023 - Modelo B (págs. 8 a 10)
- Examen Parcial 2 (Curso 24-25) - Modelo D (págs. 11 a 13)
- Examen 2023/24 Cuatrimestre B - Ejercicio 1 (págs. 13 a 15)

DIRECTRICES:
1. Formato: Markdown impecable con títulos `#`, `##`, `###`, enunciados claros, datos de partida y desarrollo analítico paso a paso.
2. Fórmulas: Emplea KaTeX estándar ($...$ y $$...$$) para el cálculo de prorratas definitivas, redondeos por exceso a la unidad superior, regla del 10% de la prorrata especial y fórmulas de regularización de bienes de inversión:
   $$R = \\frac{\\text{Cuota deducida originaria} \\times (P_{\\text{definitiva}} - P_{\\text{adquisición}})}{5 \\text{ (o 10)}}$$
3. Tablas comparativas: Prorrata General vs. Prorrata Especial, justificación de obligatoriedad según el art. 103 LIVA.
4. Liquidación Modelo 303 (4T): Cuadro de IVA Devengado (bases, tipos, cuotas, recargos de equivalencia, adquisiciones intracomunitarias) e IVA Deducible (operaciones interiores corrientes, bienes de inversión, regularizaciones de prorrata y saldos a compensar).
5. Asientos contables del PGC: Presenta tablas `Debe (€) | Cuentas y Concepto | Haber (€)` utilizando cuentas oficiales (472, 477, 4750, 4700, 6341, 6342, 231...).
6. REGLA ESTRICTA: Cero menciones a CamScanner o marcas de escaneo.

Empieza directamente con:
# Casos Prácticos de Examen: IVA - Regla de Prorrata, Bienes de Inversión, Liquidación y Contabilización
"""

PROMPT_TRANSCRIBIR_IRPF = """
Eres un catedrático de Derecho Tributario y Gestión Fiscal en la Universidad de Valencia.
Estás transcribiendo y formalizando con la máxima calidad y rigor académico la colección de ejercicios de examen resueltos de:
'CASOS PRÁCTICOS DE EXAMEN: IRPF - RENDIMIENTOS DE ACTIVIDADES ECONÓMICAS (EDN vs EDS), INCENTIVOS FISCALES Y BASE DEL AHORRO'

Las imágenes corresponden a las páginas 16 a 20 del cuaderno de ejercicios de exámenes oficiales:
- Examen 2023/24 Cuatrimestre B - Ejercicio 2 (págs. 16 y 17)
- Examen Recuperación 2024 - Ejercicio 2 IRPF completo (págs. 18, 19 y 20)

DIRECTRICES:
1. Formato: Markdown impecable con títulos `#`, `##`, `###`, enunciados claros, datos de partida y desarrollo analítico paso a paso.
2. Fórmulas: Emplea KaTeX estándar ($...$ y $$...$$).
3. Comparativa metódica entre Estimación Directa Normal (EDN) y Estimación Directa Simplificada (EDS):
   - Amortizaciones de inmovilizado (tablas lineales, coeficientes máximos, libertad de amortización por creación de empleo / incentivos para ERD).
   - Delimitación positiva y negativa de ingresos de actividades económicas vs. Rendimientos del Capital Mobiliario (dividendos, intereses bancarios).
   - Gastos deducibles, partidas no deducibles (sanciones, multas, gastos particulares).
   - Límite fiscal a las atenciones a clientes (1% del INCN).
   - Provisiones por insolvencias en EDN vs. provisión global / gastos de difícil justificación en EDS (5% con límite de 2.000 €).
4. Determinación de la Base Imponible del Ahorro: Rendimientos del capital mobiliario e integración de ganancias/pérdidas patrimoniales por transmisión de elementos no afectos.
5. REGLA ESTRICTA: Cero menciones a CamScanner o marcas de escaneo.

Empieza directamente con:
# Casos Prácticos de Examen: IRPF - Rendimientos de Actividades Económicas (EDN vs. EDS), Amortizaciones y Base del Ahorro
"""

def procesar_bloque(nombre_archivo, prompt, paginas):
    out_path = PUBLIC_GFE / nombre_archivo
    print(f"\n--- Generando {nombre_archivo} ({len(paginas)} páginas) ---")
    
    parts = []
    for p in paginas:
        img_p = TMP_DIR / f"page-{p:02d}.png"
        img = Image.open(img_p).convert("RGB")
        max_size = 1300
        if max(img.size) > max_size:
            ratio = max_size / max(img.size)
            img = img.resize((int(img.width * ratio), int(img.height * ratio)), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=80)
        parts.append(f"--- PÁGINA {p} ---")
        parts.append(types.Part.from_bytes(data=buf.getvalue(), mime_type="image/jpeg"))

    parts.append(prompt)

    models_to_try = [
        "gemini-3.8-flash",
        "gemini-3.7-flash",
        "gemini-3.1-flash-lite",
        "gemini-flash-latest"
    ]

    res = None
    for attempt in range(3):
        for m in models_to_try:
            try:
                print(f"  Intento {attempt+1} con {m}...")
                res = client.models.generate_content(model=m, contents=parts)
                if res.text:
                    print(f"  ✅ Respuesta recibida de {m}")
                    break
            except Exception as e:
                print(f"    Fallo con {m}: {str(e)[:120]}")
                time.sleep(3)
        if res and res.text:
            break
        time.sleep(4)

    if not res or not res.text:
        raise RuntimeError(f"Error generando {nombre_archivo}")

    texto = res.text
    for s in ["CamScanner", "Escaneado con CamScanner", "Scanned with CamScanner"]:
        texto = texto.replace(s, "")

    out_path.write_text(texto, encoding="utf-8")
    print(f"  ✅ Guardado en {out_path} ({len(texto)} caracteres)")

def main():
    # 1. Bloque IVA: páginas 2 a 15
    procesar_bloque(
        "ejercicios_iva_prorrata_regularizacion_m303.md",
        PROMPT_TRANSCRIBIR_IVA,
        list(range(2, 16))
    )
    time.sleep(3)

    # 2. Bloque IRPF: páginas 16 a 20
    procesar_bloque(
        "ejercicios_irpf_actividades_economicas_ahorro.md",
        PROMPT_TRANSCRIBIR_IRPF,
        list(range(16, 21))
    )

    print("\n🎉 ¡Ejercicios transcritos con total fidelidad y éxito!")

if __name__ == "__main__":
    main()
