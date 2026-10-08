# Bloque 1: Vectores, Funciones Lineales, Distancias e Independencia Lineal (Capítulos 1-5)

---

## Capítulo 1: Vectores

### Ejercicio 1.7: Transformación entre dos codificaciones para vectores booleanos

#### Enunciado
Un vector booleano $n$-dimensional es aquel cuyas entradas son todas $0$ o $1$. Tales vectores se utilizan para codificar si se cumple cada una de $n$ condiciones, con $a_i = 1$ significando que se cumple la condición $i$. 

Otro código común de la misma información utiliza los dos valores $-1$ y $+1$ para las entradas. Por ejemplo, el vector booleano $(0, 1, 1, 0)$ se escribiría utilizando esta codificación alternativa como $(-1, +1, +1, -1)$. 

Suponga que $x$ es un vector booleano con entradas que son $0$ o $1$, y $y$ es un vector que codifica la misma información utilizando los valores $-1$ y $+1$. Exprese $y$ en términos de $x$ utilizando notación vectorial. Además, exprese $x$ en términos de $y$ utilizando notación vectorial.

#### Desarrollo y Solución
1. **Relación elemento a elemento:**
   Consideremos la relación entre una entrada booleana $x_i \in \{0, 1\}$ y su correspondiente entrada alternativa $y_i \in \{-1, +1\}$.
   - Si $x_i = 0$, entonces $y_i = -1$.
   - Si $x_i = 1$, entonces $y_i = +1$.

   Podemos expresar analíticamente esta transformación como:
   $$y_i = 2x_i - 1$$

2. **Expresión vectorial para $y$ en términos de $x$:**
   Extender la relación anterior a todo el vector $n$-dimensional:
   $$y = 2x - \mathbb{1}$$
   donde $\mathbb{1}$ representa el vector columna de dimensión $n$ cuyas entradas son todas $1$ (es decir, $\mathbb{1} = (1, 1, \dots, 1)^T$).

3. **Despeje y expresión vectorial para $x$ en términos de $y$:**
   A partir de la ecuación anterior, despejamos $x$:
   $$2x = y + \mathbb{1} \implies x = \frac{1}{2}(y + \mathbb{1})$$

---

### Ejercicio 1.11: Recuento de palabras y vectores de histograma de recuento de palabras

#### Enunciado
Suponga que el $n$-vector $w$ es el vector de recuento de palabras asociado a un documento y a un diccionario de $n$ palabras. Por simplicidad, asumiremos que todas las palabras del documento aparecen en el diccionario.
1. ¿Qué es $\mathbb{1}^T w$?
2. ¿Qué significa $w_{282} = 0$?
3. Sea $h$ el $n$-vector que da el histograma de los recuentos de palabras; es decir, $h_i$ es la fracción de las palabras en el documento que son la palabra $i$. Utilice la notación vectorial para expresar $h$ en términos de $w$. (Puede asumir que el documento contiene al menos una palabra).

#### Desarrollo y Solución
1. **Interpretación de $\mathbb{1}^T w$:**
   El producto interno del vector de unos $\mathbb{1} \in \mathbb{R}^n$ y el vector de recuentos $w \in \mathbb{R}^n$ suma todas las entradas del vector $w$:
   $$\mathbb{1}^T w = \sum_{i=1}^{n} w_i$$
   Esto representa el **número total de palabras** (con repetición) contenidas en el documento.

2. **Significado de $w_{282} = 0$:**
   Indica que la palabra ubicada en la posición $282$ del diccionario **no aparece ni una sola vez** en el documento analizado.

3. **Expresión del histograma $h$ en términos de $w$:**
   Cada componente del vector histograma $h_i$ se define como el recuento de la palabra $i$ dividido por el número total de palabras en el documento:
   $$h_i = \frac{w_i}{\sum_{j=1}^{n} w_j} = \frac{w_i}{\mathbb{1}^T w}$$
   En consecuencia, expresado en notación vectorial compacta:
   $$h = \frac{1}{\mathbb{1}^T w} w$$

---

### Ejercicio 1.15: Proveedor más barato

#### Enunciado
Debes comprar $n$ materias primas en cantidades dadas por el $n$-vector $q$, donde $q_i$ es la cantidad de materia prima $i$ que debes comprar. Un conjunto de $K$ proveedores potenciales ofrece las materias primas a precios dados por los $n$-vectores $p_1, \dots, p_K$. (Nota que $p_k$ es un $n$-vector; $(p_k)_i$ es el precio que cobra el proveedor $k$ por unidad de materia prima $i$). Asumiremos que todas las cantidades y precios son positivos.

Si debes elegir un solo proveedor, ¿cómo lo harías? Tu respuesta debe usar notación vectorial.

Un consultor (altamente pagado) te dice que podrías hacerlo mejor (es decir, obtener un costo total menor) dividiendo tu pedido en dos, eligiendo dos proveedores y pidiendo $(1/2)q$ (es decir, la mitad de las cantidades) a cada uno de los dos. Él argumenta que tener diversidad de proveedores es mejor. ¿Tiene razón? Si es así, explica cómo encontrar los dos proveedores que utilizarías para surtir la mitad del pedido.

#### Desarrollo y Solución
1. **Selección de un único proveedor:**
   El costo total al comprar todas las materias primas al proveedor $k$ se calcula mediante el producto interno entre el vector de precios y el vector de cantidades:
   $$\text{Cost}_k = p_k^T q$$
   Para minimizar el costo total seleccionando un único proveedor, elegimos el índice óptimo $k^*$ tal que:
   $$k^* = \arg\min_{k \in \{1, \dots, K\}} (p_k^T q)$$

2. **Análisis de la propuesta del consultor (división de pedidos):**
   Si dividimos el pedido en partes iguales entre dos proveedores $i$ y $j$, las cantidades solicitadas a cada uno son $\frac{1}{2}q$. El costo total de esta estrategia combinada es:
   $$\text{Cost}_{ij} = p_i^T \left(\frac{1}{2}q\right) + p_j^T \left(\frac{1}{2}q\right) = \frac{1}{2} (p_i + p_j)^T q$$
   Notemos que:
   $$\frac{1}{2} (p_i + p_j)^T q = \frac{1}{2} p_i^T q + \frac{1}{2} p_j^T q = \frac{1}{2} \text{Cost}_i + \frac{1}{2} \text{Cost}_j$$
   Es decir, el costo con dos proveedores es exactamente el promedio aritmético de los costos individuales de dichos proveedores. 

3. **Conclusión sobre el argumento del consultor:**
   - **No siempre tiene razón en términos absolutos de ahorro económico.** El promedio de dos números nunca puede ser estrictamente menor que el mínimo de esos dos números. Por lo tanto, $\frac{1}{2} (p_i^T q + p_j^T q) \ge \min(p_i^T q, p_j^T q)$.
   - Si elegimos como pareja $i$ y $j$ a los dos proveedores más económicos en general, el costo será mayor o igual que el costo obtenido comprando todo al proveedor más barato ($k^*$). 
   - **Excepción:** Solo mejoraría el costo respecto al *peor* proveedor, pero nunca supera al proveedor óptimo único. Por tanto, el consultor **no tiene razón** desde una perspectiva estrictamente de minimización de costos bajo precios lineales independientes de la cantidad.

---

## Capítulo 2: Funciones Lineales

### Ejercicio 2.6: Puntuación de un cuestionario

#### Enunciado
Un cuestionario en una revista tiene $30$ preguntas, divididas en dos conjuntos de $15$ preguntas. Alguien que toma el cuestionario responde cada pregunta con *Rara vez* (*Rarely*), *A veces* (*Sometimes*), o *A menudo* (*Often*). Las respuestas se registran como un $30$-vector $a$, con $a_i = 1, 2, 3$ si la pregunta $i$ se responde como *Rarely*, *Sometimes*, o *Often*, respectivamente. 

La puntuación total en un cuestionario completado se encuentra sumando $1$ punto por cada pregunta respondida *Sometimes* y $2$ puntos por cada pregunta respondida *Often* en las preguntas $1–15$, y sumando $2$ puntos y $4$ puntos para esas mismas respuestas en las preguntas $16–30$. (No se añade nada a la puntuación por las respuestas *Rarely*). 

Exprese la puntuación total $s$ en la forma de una función afín $s = w^T a + v$, donde $w$ es un $30$-vector y $v$ es un escalar (número).

#### Desarrollo y Solución
1. **Definición de pesos por pregunta:**
   Analizamos la contribución a la puntuación $s$ en función de la respuesta $a_i$ para cada tramo de preguntas:
   - **Para las preguntas $i \in \{1, \dots, 15\}$:**
     - Si $a_i = 1$ (*Rarely*): contribución = $0$.
     - Si $a_i = 2$ (*Sometimes*): contribución = $1$.
     - Si $a_i = 3$ (*Often*): contribución = $2$.
     Observamos que la contribución para estas preguntas sigue la regla $1 \cdot (a_i - 1)$.

   - **Para las preguntas $i \in \{16, \dots, 30\}$:**
     - Si $a_i = 1$ (*Rarely*): contribución = $0$.
     - Si $a_i = 2$ (*Sometimes*): contribución = $2$.
     - Si $a_i = 3$ (*Often*): contribución = $4$.
     Observamos que la contribución para estas preguntas sigue la regla $2 \cdot (a_i - 1)$.

2. **Construcción de la función afín:**
   La puntuación total se puede expresar como la suma de las contribuciones de todas las preguntas:
   $$s = \sum_{i=1}^{15} 1 \cdot (a_i - 1) + \sum_{i=16}^{30} 2 \cdot (a_i - 1)$$

   Expandiendo las sumatorias:
   $$s = \left(\sum_{i=1}^{15} 1 \cdot a_i - \sum_{i=1}^{15} 1\right) + \left(\sum_{i=16}^{30} 2 \cdot a_i - \sum_{i=16}^{30} 2\right)$$

   Agrupando en formato de producto interno $s = w^T a + v$:
   - El vector de ponderaciones $w \in \mathbb{R}^{30}$ tiene componentes:
     $$w_i = \begin{cases} 1 & \text{si } 1 \le i \le 15 \\ 2 & \text{si } 16 \le i \le 30 \end{cases}$$
   - El término independiente escalar $v$ se calcula sumando las constantes:
     $$v = -\sum_{i=1}^{15} (1) - \sum_{i=16}^{30} (2) = -(15 \times 1) - (15 \times 2) = -15 - 30 = -45$$

3. **Resultado final:**
   $$s = w^T a - 45$$

---

## Capítulo 3: Normas y Distancia

### Ejercicio 3.1: Distancia entre vectores booleanos

#### Enunciado
Suponga que $x$ y $y$ son vectores booleanos $n$-dimensionales, lo que significa que cada una de sus entradas es $0$ o $1$. ¿Cuál es su distancia $\|x - y\|$?

#### Desarrollo y Solución
1. **Definición de la norma euclidiana aplicada:**
   La distancia entre dos vectores $x$ y $y$ se define mediante la norma euclidiana (o norma-2) de su diferencia:
   $$\|x - y\|_2 = \sqrt{(x - y)^T (x - y)} = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}$$

2. **Simplificación debido a la naturaleza booleana:**
   Dado que $x_i, y_i \in \{0, 1\}$, las únicas diferencias posibles entre las componentes son:
   - Si $x_i = y_i$, entonces $(x_i - y_i)^2 = (0)^2 = 0$.
   - Si $x_i \neq y_i$ (es decir, uno es $0$ y el otro es $1$), entonces $(x_i - y_i)^2 = (\pm 1)^2 = 1$.

3. **Conclusión geométrica:**
   Por lo tanto, el sumando dentro de la raíz cuenta exactamente el número de posiciones (índices) en los cuales los vectores $x$ e $y$ difieren (lo que en teoría de la información se conoce como la *Distancia de Hamming*):
   $$\|x - y\| = \sqrt{\text{número de índices } i \text{ tales que } x_i \neq y_i}$$

---

### Ejercicio 3.10: Documento vecino más cercano

#### Enunciado
Considere las $5$ páginas de Wikipedia. ¿Cuál es el vecino más cercano (del vector de histograma de recuento de palabras de) *Veterans Day* entre los demás? ¿Tiene sentido la respuesta?

*(Nota: Referencia a la tabla de distancias euclidianas entre documentos donde la distancia entre Veterans Day y Memorial Day es $0.095$, Academy Awards es $0.130$, Golden Globe Awards es $0.153$ y Super Bowl es $0.170$).*

#### Desarrollo y Solución
1. **Búsqueda del mínimo:**
   Revisamos las distancias desde *Veterans Day* hacia el resto de los documentos en la matriz de distancias:
   - Memorial Day: $0.095$
   - Academy Awards: $0.130$
   - Golden Globe Awards: $0.153$
   - Super Bowl: $0.170$

   El valor mínimo de distancia corresponde a *Memorial Day* ($d = 0.095$).

2. **Interpretación y sentido práctico:**
   - **¿Tiene sentido la respuesta?** Sí, totalmente. Ambos días festivos (*Veterans Day* y *Memorial Day*) comparten una temática cultural e histórica muy cercana en Estados Unidos (homenaje a veteranos y caídos en servicio militar), por lo que el vocabulario utilizado en sus respectivas páginas de Wikipedia (términos como *military*, *service*, *armed forces*, *fallen*, etc.) presenta una alta superposición estadística, arrojando una distancia menor en el espacio vectorial de palabras.

---

## Capítulo 5: Independencia Lineal

### Ejercicio 5.2: Un descubrimiento sorprendente

#### Enunciado
Un becario en un fondo de cobertura cuantitativo examina los rendimientos diarios de alrededor de $400$ acciones durante un año (que tiene $250$ días de negociación). Le dice a su supervisor que ha descubierto que los rendimientos de una de las acciones, Google (GOOG), se pueden expresar como una combinación lineal de los demás, que incluyen muchas acciones que no están relacionadas con Google (digamos, en un tipo de negocio o sector diferente).

Su supervisor entonces dice: *"Es abrumadoramente improbable que una combinación lineal de los rendimientos de empresas no relacionadas pueda reproducir el rendimiento diario de GOOG. Así que has cometido un error en tus cálculos."*

¿Tiene razón el supervisor? ¿Hizo el becario un error? Dé una explicación muy breve.

#### Desarrollo y Solución
1. **Modelado dimensional del problema:**
   - El rendimiento temporal de cada acción a lo largo de $250$ días de negociación se representa como un vector en el espacio euclidiano $\mathbb{R}^{250}$.
   - Tenemos $400$ vectores de acciones disponibles para intentar reconstruir el vector de Google.

2. **Análisis de independencia y dimensión:**
   - Dimensión del espacio ambiente: $\dim(\mathbb{R}^{250}) = 250$.
   - Número de vectores disponibles para formar combinaciones lineales: $400$ vectores.
   - Como el número de vectores excede la dimensión del espacio ($400 > 250$), **cualquier conjunto de más de 250 vectores en $\mathbb{R}^{250}$ es necesariamente linealmente dependiente**.

3. **Conclusión:**
   El supervisor está **equivocado** desde una perspectiva de álgebra lineal pura. No solo es posible expresar el vector de Google como combinación lineal de los demás, sino que debido a que hay más vectores que la dimensión del espacio, existen infinitas combinaciones lineales (incluso redundantes) que pueden replicar exactamente dicho vector. El becario no cometió un error matemático (aunque esto pueda reflejar sobreajuste o *overfitting* financiero en la práctica).

---

### Ejercicio 5.4: Norma de combinación lineal de vectores ortonormales

#### Enunciado
Suponga que $a_1, \dots, a_k$ son $n$-vectores ortonormales, y $x = \beta_1 a_1 + \dots + \beta_k a_k$, donde $\beta_1, \dots, \beta_k$ son escalares. Exprese $\|x\|$ en términos de $\beta = (\beta_1, \dots, \beta_k)^T$.

#### Desarrollo y Solución
1. **Definición de ortonormalidad:**
   Por hipótesis, los vectores $a_i$ satisfacen la condición de ortonormalidad:
   $$a_i^T a_j = \begin{cases} 1 & \text{si } i = j \\ 0 & \text{si } i \neq j \end{cases}$$

2. **Cálculo del cuadrado de la norma euclidiana:**
   Queremos calcular $\|x\|^2 = x^T x$. Sustituimos la combinación lineal:
   $$\|x\|^2 = \left(\sum_{i=1}^{k} \beta_i a_i\right)^T \left(\sum_{j=1}^{k} \beta_j a_j\right)$$

   Aplicamos la propiedad distributiva del producto interno:
   $$\|x\|^2 = \sum_{i=1}^{k} \sum_{j=1}^{k} \beta_i \beta_j (a_i^T a_j)$$

3. **Simplificación por ortonormalidad:**
   Debido a que los productos internos $a_i^T a_j$ se anulan para todo $i \neq j$ y valen $1$ cuando $i = j$, la suma doble se reduce a una única sumatoria:
   $$\|x\|^2 = \sum_{i=1}^{k} \beta_i^2 (1) = \sum_{i=1}^{k} \beta_i^2 = \|\beta\|_2^2$$

4. **Resultado final para la norma:**
   Tomando la raíz cuadrada en ambos miembros, obtenemos la norma euclidiana del vector resultante en función del vector de coeficientes $\beta$:
   $$\|x\| = \|\beta\|_2$$