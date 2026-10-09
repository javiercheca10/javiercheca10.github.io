# Bloque 3: Principios de Conteo, Combinatoria, Principio del Palomar y Demostraciones de Identidades

A continuación, presento la resolución formal de los ejercicios seleccionados, correspondientes a los principios fundamentales de conteo y combinatoria, basados en la metodología de Kenneth H. Rosen.

---

### Ejercicio 14: Cadenas de caracteres de longitud 8
*(Referencia: Rosen, Sección 6.1)*

**Problema:** Determine el número de cadenas de longitud 8 que pueden formarse bajo diversas restricciones con un alfabeto de 26 letras.

*   **a) Sin restricciones (repetición permitida):** 
    Cada una de las 8 posiciones tiene 26 opciones.
    $$N = 26^8$$
*   **b) Sin repetición:** 
    Es una permutación de 26 elementos tomados de 8 en 8.
    $$P(26, 8) = \frac{26!}{(26-8)!} = \frac{26!}{18!} = 26 \cdot 25 \cdot \dots \cdot 19$$
*   **c) La primera letra es fija (ej. 'x'):** 
    La primera posición tiene 1 opción; las 7 restantes, 26 cada una.
    $$N = 1 \cdot 26^7 = 26^7$$
*   **d) Sin repetición, empezando con un valor fijo y tomando 7 más:**
    $$P(25, 7) = \frac{25!}{(25-7)!} = \frac{25!}{18!}$$
*   **e) Primera y última fijas:** 
    Solo varían las 6 posiciones centrales.
    $$N = 26^6$$
*   **f) Primera y segunda fijas:** 
    Igual que el caso anterior, varían 6 posiciones.
    $$N = 26^6$$
*   **g) Cuatro letras fijas:**
    Varían las $8-4=4$ posiciones restantes.
    $$N = 26^4$$
*   **h) Aplicando el Principio de Inclusión-Exclusión para cadenas que empiezan o terminan con "BO":**
    Sea $A$ el conjunto de cadenas que empiezan con "BO" ($|A|=26^6$) y $B$ el conjunto de cadenas que terminan con "BO" ($|B|=26^6$). La intersección $A \cap B$ son cadenas que empiezan y terminan con "BO" ($|A \cap B|=26^4$).
    $$|A \cup B| = |A| + |B| - |A \cap B| = 26^6 + 26^6 - 26^4$$

---

### Ejercicio 15: Múltiplos en un rango
*(Referencia: Rosen, Sección 6.5, Ejercicio 55)*

**Problema:** ¿Cuántos enteros positivos menores o iguales a 100 son divisibles por 4 o por 6?

1.  **Divisibles por 4 ($|A|$):** $100 / 4 = 25$.
2.  **Divisibles por 6 ($|B|$):** $\lfloor 100 / 6 \rfloor = 16$.
3.  **Divisibles por ambos ($\text{mcm}(4, 6) = 12$):** $\lfloor 100 / 12 \rfloor = 8$.
4.  **Principio de Inclusión-Exclusión:**
    $$|A \cup B| = |A| + |B| - |A \cap B| = 25 + 16 - 8 = 33$$

---

### Ejercicio 16: Principio del Palomar (Pigeonhole Principle)
*(Referencia: Rosen, Sección 6.2, Ejercicio 46)*

**Problema:** 51 casas en una calle tienen direcciones entre 1000 y 1099. Demostrar que existen dos casas con direcciones consecutivas.

*   **Análisis:** Hay 100 números posibles (del 1000 al 1099). Podemos agrupar estos números en 50 pares de números consecutivos: $\{(1000, 1001), (1002, 1003), \dots, (1098, 1099)\}$.
*   **Aplicación:** Al haber 51 casas (palomas) y 50 pares (nidos), por el **Principio del Palomar**, al menos un par debe contener dos casas. Por tanto, dos casas tienen direcciones consecutivas.

---

### Ejercicio 17: Ordenamiento en fila
*(Referencia: Rosen, Sección 6.3, Ejercicio 25)*

**Problema:** 4 hombres y 5 mujeres en fila.
*   **a) Hombres juntos:** Tratamos a los hombres como un único bloque. Tenemos $5$ (mujeres) $+ 1$ (bloque) $= 6$ unidades.
    $$6! \cdot 4! = 720 \cdot 24 = 17,280$$
*   **b) Mujeres juntas:** Tratamos a las mujeres como un bloque. Tenemos $4$ (hombres) $+ 1$ (bloque) $= 5$ unidades.
    $$5! \cdot 5! = 120 \cdot 120 = 14,400$$

---

### Ejercicio 18: Selección de respuestas
*(Referencia: Rosen, Sección 6.3, Ejercicio 30)*

**Problema:** 40 preguntas V/F, 17 son verdaderas. ¿Cuántas claves de respuesta son posibles?
Se trata de elegir 17 posiciones de entre 40 disponibles.
$$\binom{40}{17} = \frac{40!}{17!(40-17)!} = \binom{40}{23}$$

---

### Ejercicio 19: Comités
*(Referencia: Rosen, Sección 6.3, Ejercicio 32)*

**Problema:** Elegir un comité de 5 miembros de un grupo de 7 mujeres y 9 hombres (16 total).
*   **a) Al menos una mujer:** Total menos el caso donde no hay mujeres.
    $$\binom{16}{5} - \binom{9}{5} = 4368 - 126 = 4242$$
*   **b) Al menos una mujer y al menos un hombre:** Total menos casos de "solo mujeres" y "solo hombres".
    $$\binom{16}{5} - \binom{9}{5} - \binom{7}{5} = 4368 - 126 - 21 = 4221$$

---

### Ejercicio 20: Carrera de caballos con empates
*(Referencia: Rosen, Sección 6.4, Ejercicio 46)*

**Problema:** 4 caballos, considerando posibles empates.
*   No hay empates: $4! = 24$
*   3 caballos empatan, 1 separado: $\binom{4}{3} \cdot 2! = 8$
*   3 caballos empatan (en otro grupo), 2 separados: $\binom{4}{2} \cdot 3! = 36$
*   2 pares de empate: $\frac{\binom{4}{2} \cdot 2!}{2} = 6$
*   Todos empatan: $1$
*   **Total:** $24 + 8 + 36 + 6 + 1 = 75$

---

### Ejercicio 21: Identidad de subconjuntos
*(Referencia: Rosen, Sección 6.4, Ejercicio 26)*

**Demostración:** $\binom{n}{r}\binom{r}{k} = \binom{n}{k}\binom{n-k}{r-k}$
*   **Argumento Combinatorio:** Ambos lados cuentan la forma de elegir un comité de tamaño $r$ de $n$ personas, y luego un subcomité de $k$ personas dentro de ese comité.
    1.  LHS: Elegir primero el comité ($r$) y luego el subcomité ($k$).
    2.  RHS: Elegir primero los líderes del subcomité ($k$) de los $n$ originales, y luego completar el resto del comité ($r-k$) de los $n-k$ restantes.

---

### Ejercicio 22: Soluciones enteras (Stars and Bars)
*(Referencia: Rosen, Sección 6.5, Ejercicio 14)*

**Problema:** $x_1 + x_2 + x_3 + x_4 = 17$ (enteros no negativos).
Utilizamos la fórmula de *Stars and Bars*: $\binom{n+k-1}{k-1}$ donde $n=17$ y $k=4$.
$$\binom{17+4-1}{4-1} = \binom{20}{3} = \frac{20 \cdot 19 \cdot 18}{3 \cdot 2 \cdot 1} = 1140$$