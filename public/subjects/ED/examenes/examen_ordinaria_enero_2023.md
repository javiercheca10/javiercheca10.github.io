# UNIVERSIDAD DE GRANADA
**Departamento de Ciencias de la Computación e Inteligencia Artificial**

* **Asignatura:** Estructuras de datos
* **Curso académico:** 2022-2023
* **Convocatoria:** Convocatoria ordinaria de Enero
* **Titulaciones:** Grado en Ingeniería Informática, Doble Grado en Ingeniería Informática y Matemáticas, Doble Grado en Ingeniería Informática y ADE

---

1. **(1 punto)** 
   
   **(a)** Si insertamos un conjunto de enteros **ordenado** ascendentemente en un ABB, un APO-min y un AVL: ¿En cuál de los 3 es más eficiente la operación de inserción? **Razonarlo**.

   **(b)** 
   * **(b1)** ¿Cuántos elementos, en promedio, hay en cada lista en una tabla hash abierta de tamaño $B$ con $N$ elementos? **(b1)** $(N/B)$ **(b2)** $(N + B)$ **(b3)** $(B/N)$ **(b4)** $1$. **Razonarlo**.
   * **(b2)** ¿Es correcto en un esquema de hashing cerrado con un tamaño de la tabla $B$ primo con resolución de colisiones usando hashing doble, el uso como función hash: $h(x) = [(x \pmod C) \pmod B]$? ¿Y como función hash secundaria $h_0(x) = [(x \cdot C) \pmod{B-2}]$? $B, C$ primos entre sí. **Razonarlo**.

   **(c)** Dadas las siguientes 3 afirmaciones:
   * Dados $A$ y $B$ dos árboles binarios (con más de un nodo) distintos con etiquetas diferentes, nunca puede ocurrir simultáneamente: $\text{Pre}(A) = \text{Post}(B)$ y $\text{Post}(A) = \text{Pre}(B)$
   * Un APO puede reconstruirse de forma unívoca dado su recorrido en postorden
   * Solo hay un APO que tiene como $\text{preorder} = \{4, 9, 24, 33, 21, 74, 63\}$
   
   * **(c1)** Todas son falsas 
   * **(c2)** Hay 2 ciertas y 1 falsa 
   * **(c3)** Hay 1 cierta y dos falsas 
   * **(c4)** Todas son ciertas. 
   
   **Razonar la respuesta.**

   **(d)** Dados los siguientes recorridos en $\text{preorder} = (A,Z,W,R,X,Q,T,Y,L,V)$, y $\text{postorden} = (R,W,Q,X,Z,Y,V,L,T,A)$ de un árbol binario:
   * **(d1)** No hay ningún árbol binario con esos recorridos asociados; 
   * **(d2)** Hay 1 solo árbol binario con esos recorridos asociados; 
   * **(d3)** Hay exactamente dos árboles binarios con esos recorridos asociados; 
   * **(d4)** Todo lo anterior es falso. 
   
   **Razonar la respuesta.**

2. **(1 punto)** Se desea construir un **traductor** de un idioma origen a un idioma destino. Una palabra en el idioma origen puede tener más de una traducción en el idioma destino.

   Usando como **representación** para el **TDA Traductor** un `map<string, set<string>>`:
   * Implementar una **clase iteradora** dentro de la clase Traductor para **dada una palabra** en el idioma de destino, iterar por todas las palabras del idioma de origen que tengan como traducción esa palabra. Han de implementarse (aparte de las de la clase iteradora) las funciones `begin` y `end`.

3. **(1 punto)** Implementar una función

   cpp
   void intercambia_sec (list<int>& L);
   

   que dada una lista $L$, intercambie el grupo de los primeros elementos consecutivos impares por el siguiente grupo de elementos consecutivos pares de principio a final de la lista.

   > **Restricción:** **No pueden usarse estructuras de datos auxiliares.**

   Por ejemplo si $L = \{1, 2, 4, 5, 6, 8, 7, 9, 13, 2, 9\}$ después de llamar a `intercambia_sec(L)` debe quedar $L = \{2, 4, 1, 6, 8, 5, 2, 7, 9, 13, 9\}$.
