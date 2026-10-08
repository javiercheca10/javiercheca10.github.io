# UNIVERSIDAD DE GRANADA
**Departamento de Ciencias de la Computación e Inteligencia Artificial**

**Asignatura:** Estructuras de datos  
**Curso académico:** 2022-2023  
**Convocatoria:** Convocatoria extraordinaria de Febrero  
**Titulaciones:** 
* Grado en Ingeniería Informática
* Doble Grado en Ingeniería Informática y Matemáticas
* Doble Grado en Ingeniería Informática y ADE

---

### 1. (1 punto)

**(a)** Si inserto las claves $\{18, 10, 14, 26, 12, 21, 33, 4\}$ en un AVL de enteros:
* **(a1):** Hay que hacer dos rotaciones simples y una rotación doble.
* **(a2):** Hay que hacer una rotación simple y una rotación doble.
* **(a3):** Hay que hacer dos rotaciones dobles y una rotación simple.
* **(a4):** Todo lo anterior es falso.

**Restricción:** **Mostrar el árbol final**.

**(b)** ¿Puede reconstruirse forma unívoca un árbol binario en el que todos los nodos tienen 0 ó 2 hijos, conociendo su preorden? ¿y un árbol binario completo conociendo su postorden? Razonarlo.

**(c)** Dados los siguientes recorridos Preorden y Postorden:
$$\text{Pre} = \{A,Z,W,R,V,X,Q,T,Y,L\}$$
$$\text{Post} = \{R,V,W,Q,X,Z,Y,L,T,A\}$$

* **(c1)** Hay exactamente 2 árboles binarios con esos recorridos.
* **(c2)** No hay ningún árbol binario con esos recorridos.
* **(c3)** Hay exactamente 1 árbol binario con esos recorridos.
* **(c4)** Hay más de 2 árboles binarios con esos recorridos.

**(d)** Dado el siguiente fragmento de código:

```cpp
{map <int,int> M; M[0]=1; map <int,int> ::iterator p; p=M.find(9);}
```



¿Cuál de las siguientes afirmaciones es verdadera?
* **d-1:** `M` no se modifica y `p->first=9`
* **d-2:** Da un error
* **d-3:** `M` se modifica y `p->first=9`
* **d-4:** `M` se modifica y `p=M.end()`

---

### 2. (1 punto) 

Tenemos un contenedor de pares de elementos, **{clave, bintree\<int\>}** definida como:

```cpp
template <typename T>
class contenedor {
    private:
        unordered_map<T, bintree<int> > datos;
        ............
};
```



Implementar un **iterador** que itere sobre las claves que cumplan la propiedad de que el bintree asociado tenga como suma de sus etiquetas un número par. Se deben implementar (aparte de las de la clase iterator) las funciones `begin()` y `end()` de la clase contenedor.

---

### 3. (1 punto) 

Implementar una función:

```cpp
bool permutalista (list<int> & L1, list<int> & L2)
```



que devuelva `true` si `L1` y `L2` tienen la misma cantidad de elementos y los elementos de `L1` son una permutación de los de `L2`.

*P.ej:* si $L1=\{1,23,21,4,2,3,0\}$ y $L2=\{21,1,3,2,4,23,0\}$ devolvería `TRUE` pero si $L1=\{1,3,5\}$ y $L2=\{1,5,4\}$ devolvería `FALSE`.

Si hay elementos repetidos tienen que estar el mismo número de veces en las 2 listas para poder ser `TRUE`. 

**Restricciones:** 
* **No pueden usarse estructuras auxiliares**.
* El algoritmo puede ser destructivo y no conservar las listas iniciales.
* **No puede usarse ningún algoritmo de ordenación**.

---

### 4. (1 punto) 

Dado un `bintree<int>`, implementar una función:

```cpp
void prom_nivel(bintree<int> &T, list<float> &P);
```



que genere una lista de reales `P`, donde el primer elemento de la lista sea el promedio de los nodos del árbol de nivel 0, el segundo sea el promedio de los de nivel 1, el tercero el promedio de los de nivel 2, y así sucesivamente. Es decir, que si el árbol tiene profundidad $N$, la lista tendrá $N+1$ elementos de tipo `float`.

**Ejemplo:**

text
      A
      1
     / \
    4   7          prom_nivel( A, P)
   / \ / \
  8  9 20 15       P={1.0, 5.5, 13.0, 14.0}
    /   \  \
   18   14 10


---

### 5. (1 punto) 

Implementar una función:

```cpp
bool tiene_suma_constante (set<int> s, int M);
```



que dado un conjunto de enteros **s** y un entero **M**, devuelva `true` si existe un subconjunto de elementos enteros cuyos valores sumen exactamente `M`.

*P.ej si:* $s=\{1,2,3,4,5,6\}$; **tiene_suma_constante(s,15)** devolvería **true** y si hacemos **tiene_suma_constante(s,22)** devolvería **false**.

---

### 6. (1 punto) 

**(a)** Insertar en el orden indicado (detallando los pasos) las siguientes claves en un **APO**: $\{10, 5, 12, 12, 5, 3, 9, 4, 3\}$. Borrar dos elementos y mostrar el APO resultante.

**(b)** Insertar (detallando los pasos) las siguientes claves (en el orden indicado):
$$\{47, 31, 49, 66, 50, 52, 82, 38, 7, 63, 53\}$$
en una tabla hash cerrada de tamaño 13 con resolución de colisiones usando hashing doble.

---
**Tiempo:** 2.30 horas
