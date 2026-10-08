# Examen Oficial de Lógica y Métodos Discretos (19 de Junio de 2023)

**DATOS DEL EXAMEN**  
* **Asignatura:** Lógica y Métodos Discretos (LMD)  
* **Fecha:** 19 de Junio de 2023  
* **Apellidos y Nombre:** Checa Casas, Francisco Javier  
* **D.N.I.:** 77448162P  
* **Grupo:** Doble Grado (Inf + ADE)  

> **Instrucciones:** Todas las respuestas han de estar debidamente justificadas.

---

## Ejercicio 1

Sean $f, g : \mathbb{B}^3 \to \mathbb{B}$ las funciones booleanas dadas por:

$$f(y, z, t) = (y \uparrow z) \uparrow t$$

$$g(y, z, t) = (\bar{y} \downarrow z) \downarrow \bar{t}$$

y sea $h : \mathbb{B}^4 \to \mathbb{B}$ la función definida por:

$$h(x, y, z, t) = \begin{cases} f(y, z, t) & \text{si } x = 0 \\ g(y, z, t) & \text{si } x = 1 \end{cases}$$

1. Calcula la forma canónica conjuntiva de $g$.
2. Expresa $g$ usando únicamente el operador $\text{NAND}$ ($\uparrow$).
3. Calcula todos los implicantes primos de $h$.
4. Calcula una expresión reducida o minimal, como suma de producto de literales, de la función $h$.

---

## Ejercicio 2

Nos encontramos en la isla donde hay dos grupos de personas: los que dicen siempre la verdad y los que siempre mienten. Queremos averiguar tres cosas:
1. Si hay oro en la isla.
2. Si está en la isla Paco López (el entrenador del Granada CF, que está intentando aislarse del mundo después del cansancio de la temporada).
3. Si ha habido buena cosecha.

Los habitantes de la isla conocen la respuesta a nuestras tres preguntas, pero la respuesta que nos dan no siempre nos aclara lo que queremos saber.

Preguntamos a tres nativos, cuyos nombres son (o eso creemos) Ana, Bartolomé y Carmen, y las respuestas que nos dan son:

* **Ana:** *Hay oro y buena cosecha.*
* **Bartolomé:** *Si hay oro, no hay buena cosecha.*
* **Carmen:** *Si está Paco López, hay buena cosecha.*

Después de pensar no llegamos a ninguna conclusión, por lo que les pedimos más información. Entonces, Bartolomé nos dice que *si no hay oro, Paco López no viene por aquí*, a lo que añade Ana *pues no ha venido*.

¿Podrías responder a las tres cuestiones que traíamos?

---

## Ejercicio 3

Interpreta cada una de las siguientes fórmulas en cada una de las estructuras que se describen:

1. $\alpha_1 = \exists x \forall y \, P(f(y), x)$
2. $\alpha_2 = \forall x \exists y \, P(f(y), x)$
3. $\alpha_3 = \forall y \exists x \, P(f(y), x)$

### Estructuras:

| Estructura 1 | Estructura 2 | Estructura 3 |
| :--- | :--- | :--- |
| $D_1 = \mathbb{R}$ | $D_2 = \mathbb{Z}_5$ | $D_3 = \mathbb{Z}_2$ |
| $f(z) = z^2$ | $f(z) = z^2$ | $f(z) = z^2$ |
| $P(x, y) \equiv x + y = 0$ | $P(x, y) \equiv x + y = 0$ | $P(x, y) \equiv x + y = 0$ |

¿Es alguna de ellas universalmente válida? Razona la respuesta.