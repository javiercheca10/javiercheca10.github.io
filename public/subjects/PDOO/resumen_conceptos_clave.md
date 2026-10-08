# Resumen Técnico: Atributos, Encapsulamiento y Constructores (Java vs Ruby)

---

## 1. Atributos y Modificadores de Estado

En el diseño orientado a objetos, el estado de un objeto se define mediante sus atributos. A continuación, se detallan las reglas fundamentales sobre su comportamiento, inmutabilidad y ámbito de acceso en **Java** y **Ruby**:

* **Inmutabilidad:** Un atributo declarado como `final` en Java no se puede modificar una vez inicializado.
* **Encapsulamiento de Atributos Privados:** Un atributo `private` no es accesible directamente desde el exterior; requiere obligatoriamente de métodos de acceso (**consultores** o *getters*) y de modificación (**modificadores** o *setters*).
* **Ámbito de Clase vs. Instancia:**
  * Un atributo de clase (estático) es accesible tanto desde el contexto de la clase como desde el de sus instancias.
  * En Java, la pertenencia a la clase se define mediante la palabra reservada `static`.
  * En Ruby, los atributos de clase o variables de clase se identifican mediante el prefijo `@@`. Los atributos de instancia utilizan `@`.
* **Uso de la referencia actual:** La palabra reservada `this` (en Java) o `self` (en Ruby) se utiliza exclusivamente dentro de los **métodos de instancia** para referenciar al objeto receptor del mensaje actual.

---

## 2. Ocultación de Información y Modularidad

La ocultación de información (*Information Hiding*) es uno de los pilares fundamentales del paradigma orientado a objetos, permitiendo desacoplar la interfaz de la implementación:

* **En Java:** La ocultación y organización a nivel de código se gestiona mediante **paquetes** (*packages*) y los modificadores de visibilidad (`public`, `protected`, *default/package-private*, `private`).
* **En Ruby:** La modularidad y encapsulación lógica se consigue mediante el uso de **módulos** (*modules*), además de las directivas de visibilidad (`public`, `protected`, `private`).

---

## 3. Acceso a Atributos (Java vs. Ruby)

Las reglas para acceder a los atributos varían según el lenguaje y la sintaxis empleada:

| Concepto | Java | Ruby |
| :--- | :--- | :--- |
| **Acceso a Variables de Instancia** | Depende estrictamente de la visibilidad (`private`, `public`, etc.). | Si se utiliza la notación con una arroba (`@`), solo se puede acceder desde la propia clase. |
| **Acceso a Variables de Clase** | Depende de los modificadores de acceso estáticos. | Si se utiliza doble arroba (`@@`), se puede acceder tanto desde la clase como desde sus instancias. |

> **Nota sobre importaciones en Java:** Si se utiliza una directiva `import`, la clase no se "mete" físicamente en el paquete actual; simplemente se habilita su visibilidad en el ámbito de compilación. Las clases externas importadas solo serán accesibles si sus miembros son `public`.

---

## 4. Constructores y Ciclo de Vida de los Objetos

El proceso de construcción e inicialización de un objeto asegura que este alcance un estado válido desde su creación:

* **En Java:** Los constructores pueden **sobrecargarse** (*overloading*), permitiendo múltiples formas de inicializar un objeto según los parámetros proporcionados.
* **En Ruby:** El mecanismo de inicialización por defecto se implementa mediante la definición explícita del método reservado `initialize` dentro de la clase:

```ruby
class MiClase
  def initialize(parametro)
    @atributo = parametro
  end
end
```