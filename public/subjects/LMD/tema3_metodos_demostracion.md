# Tema 3: Métodos de Demostración (Davis-Putnam e Inducción Matemática)

---

## 1. Satisfactibilidad: Método de Davis-Putnam

Para comprobar si es cierta una implicación semántica de la forma $\Sigma \models \varphi$:

1. **Teorema de la deducción:** Se utiliza para pasar todos los elementos de la premisa a un único lado, incorporando la negación de la conclusión al conjunto de premisas.
2. **Comprobar si el conjunto de fórmulas es insatisfactible:**
   2.1. **Pasar todas las fórmulas a forma clausal** utilizando las siguientes equivalencias y reglas de transformación:
   $$\begin{aligned}
   a \leftrightarrow b &\equiv (a \to b) \land (b \to a) \\
   a \to b &\equiv \neg a \lor b \\
   \neg(a \lor b) &\equiv \neg a \land \neg b \\
   \neg(a \land b) &\equiv \neg a \lor \neg b
   \end{aligned}$$

   > **Nota:** Para la resolución y elección de literales en Davis-Putnam, se sigue la siguiente jerarquía:
   > 1. **Cláusula unitaria** (un único literal).
   > 2. **Literal puro** (literal que aparece siempre con la misma polaridad, sin negar o negado).
   > 3. **Elegir cualquier otro literal** de forma arbitraria.

   2.2. **Aplicación iterativa del algoritmo:**
   - **2.2.1.** Si hay **cláusula unitaria**, se fija su valor eliminando las apariciones de dicho literal y retirando la cláusula contraria (o aplicando resolución directa).
   - **2.2.2.** Si no hay cláusulas unitarias, pero hay **literal puro**, se elimina de las cláusulas donde aparece.
   - **2.2.3.** Si no se cumple ninguna de las anteriores, **se elige un literal cualquiera** y se crean dos ramas (una con el literal y otra con su negado), repitiendo el proceso de forma recursiva en cada rama.

3. **Criterio de parada:** Si llegamos a la **cláusula vacía $\Box$ en TODAS las ramas**, el conjunto es **insatisfactible** (y por tanto la demostración por reducción al absurdo es correcta).

> **Ejemplo:** Ver si una fórmula $\alpha$ es una tautología ($\models \alpha$).

---

## 2. Inducción Matemática (Tema 5)

Para demostrar una propiedad $P(n)$ para todo $n \in \mathbb{N}$ mediante el principio de inducción matemática:

1. **Caso base:** Evaluamos y demostramos que la propiedad se cumple para el primer elemento (típicamente $n = 0$ o $n = 1$).
2. **Hipótesis de inducción:** Asumimos que la propiedad es cierta para un número genérico $n$ ($P(n)$ es verdadera).
3. **Paso inductivo:** Demostramos que la propiedad también se cumple para el siguiente elemento, es decir, para $n + 1$ ($P(n + 1)$).