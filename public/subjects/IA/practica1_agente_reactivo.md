# Práctica 1: Percepción Sensorial y Agente Reactivo

En esta primera fase del desarrollo del agente para el simulador de **Inteligencia Artificial** (ETSIIT UGR), se implementa la arquitectura sensorial y reactiva de un agente situado en un entorno matricial bidimensional con visibilidad parcial y restricciones de orientación.

---

## 1. Modelo del Entorno y Sistema de Sensores

El agente interactúa con el simulador a través del método `think(Sensores sensores)`, que proporciona información instantánea del entorno en cada ciclo de ejecución:

* **Posición y Orientación:**
  * Coordenadas discretas `(posF, posC)` en la matriz del mapa.
  * Orientación mediante brújula de 8 direcciones: `norte`, `noreste`, `este`, `sureste`, `sur`, `suroeste`, `oeste`, `noroeste`.
* **Cono de Visión:**
  * Sensor de terreno `sensores.terreno`: vector con las casillas visibles en el cono frontal del agente (hasta alcance 3).
  * Sensor de agentes `sensores.agentes`: detección de entidades dinámicas (otros jugadores, aldeanos y perros).
* **Estado Interno:**
  * Nivel de batería / energía restante (`sensores.vida`).
  * Indicador de colisión física (`sensores.colision`) y reinicio de posición (`sensores.reset`).

---

## 2. Tipos de Terreno y Restricciones Físicas

El mapa se compone de distintos tipos de casillas con propiedades de transitabilidad y coste:

| Símbolo | Tipo de Terreno | Transitabilidad | Comportamiento |
| :---: | :--- | :---: | :--- |
| `S` | Suelo estándar / Asfalto | Sí | Consumo energético base bajo |
| `T` | Terreno de bosque | Sí | Mayor coste energético sin equipamiento |
| `A` | Agua | Sí | Coste muy elevado; requiere bikini |
| `B` | Arena | Sí | Coste medio; requiere zapatillas |
| `P` | Precipicio | No | Casilla no transitable (obstáculo mortal) |
| `M` | Muro / Pared | No | Obstáculo infranqueable |
| `K` | Bikini | Objeto | Reduce drásticamente el consumo en agua |
| `D` | Zapatillas | Objeto | Reduce drásticamente el consumo en bosque/arena |
| `G` | Casilla de recarga | Especial | Recarga los puntos de batería del agente |

---

## 3. Comportamiento Reactivo y Cinemática

El agente actualiza su estado interno según la última acción ejecutada:

* `actWALK`: Avanza una casilla en la dirección actual de la brújula.
* `actRUN`: Avanza dos casillas consecutivas (si ambas son transitables).
* `actTURN_L`: Gira 90° a la izquierda (decrementa 2 posiciones mod 8 en la brújula).
* `actTURN_SR`: Giro suave a la derecha (incrementa 1 posición mod 8).
* `actIDLE`: Permanece en espera.

El control reactivo prioriza:
1. Esquivar obstáculos no transitables (`P` y `M`) detectados en el cono frontal.
2. Evitar colisiones frontales con aldeanos o perros.
3. Buscar casillas de recarga energética (`G`) cuando el nivel de batería desciende de un umbral crítico.
4. Explorar casillas desconocidas actualizando el mapa mental del agente.
