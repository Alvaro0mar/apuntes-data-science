# PROGRAMA DE ESPECIALIZACIÓN EN INTELIGENCIA ARTIFICIAL

## MÓDULO: FUNDAMENTOS DE IA y MACHINE LEARNING

---

## Ciencia de Datos con Python

**Flujo de trabajo:**

```
Reality ──▶ Raw Data Collected ──▶ Data Is Processed ──▶ Clean Dataset
                                                              │
                                        ┌─────────────────────┼─────────────────────┐
                                        ▼                                           ▼
                              Exploratory Data Analysis                  Models & Algorithms
                                                                                    │
                              ┌─────────────────────────────────────────────────────┤
                              ▼                                                     ▼
                        Data Product                                  Communicate Visualize Report
                              │                                                     │
                              ▼                                                     ▼
                          Reality                                          Make Decisions
```

---

## ¿Por qué amamos Python para el trabajo de ciencia de datos?

Python es un excelente lenguaje de programación para el trabajo de ciencia de datos. He aquí por qué nos encanta...

- **Python es fácil de aprender.** Desde una perspectiva de programación, Python es uno de los lenguajes más fáciles de aprender.
- **Python es flexible.** Se ejecuta en casi todas las plataformas, incluidas Windows y MacOS. Como idioma, funciona lo suficientemente bien para una variedad de usos, lo que lo hace versátil y flexible.
- **Los programadores de Python son más asequibles.** Si bien puede hacer mucho con Java, R y el marco Hadoop... eso no significa que el trabajo tenga un precio asequible.
- **Los líderes de la industria confían en Python.** Google, Youtube, Instagram, NASA, IBM, Netflix, Spotify, Uber, Pinterest, Reddit y más usan Python.
- **Python es eficiente en el código.** Para lo que puede lograr en R, usará mucho menos código escribiéndolo en Python.

---

## Python para Machine Learning

### NumPy

**NUMerical + PYthon**

- Potente estructuras de datos
- Implementa matrices y matrices multidimensionales
- Estas estructuras garantizan cálculos eficientes con matrices

NumPy es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos. Incorpora una nueva clase de objetos llamados **arrays** que permite representar colecciones de datos de un mismo tipo en varias dimensiones, y funciones muy eficientes para su manipulación.

---

## La clase de objetos array

Un array es una estructura de datos de un mismo tipo organizada en forma de tabla o cuadrícula de distintas dimensiones.

Las dimensiones de un array también se conocen como **ejes**.

**Ejemplos:**
- **1D array:** `[7, 2, 9, 10]` → axis 0 → shape: (4,)
- **2D array:** `[[5.2, 3.0, 4.5], [9.1, 0.1, 0.3]]` → axis 0 / axis 1 → shape: (2, 3)
- **3D array:** cubo de valores con axis 0, axis 1, axis 2 → shape: (4, 3, 2)

---

## Creación de arrays con NumPy

⚠️ Los elementos de la lista o tupla deben ser del mismo tipo.

```python
>>> # Array de una dimensión
>>> a1 = np.array([1, 2, 3])
>>> print(a1)
[1 2 3]

>>> # Array de dos dimensiones
>>> a2 = np.array([[1, 2, 3], [4, 5, 6]])
>>> print(a2)
[[1 2 3]
 [4 5 6]]

>>> # Array de tres dimensiones
>>> a3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
>>> print(a3)
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
```

---

## Pandas

Pandas es una librería de Python especializada en el manejo y análisis de estructuras de datos.

**PANel + DAta**

- Librería de código abierto
- Proporciona herramientas de análisis y manipulación de datos de alto rendimiento

**Las principales características de esta librería son:**

- Define nuevas estructuras de datos basadas en los arrays de la librería NumPy pero con nuevas funcionalidades.
- Permite leer y escribir fácilmente ficheros en formato CSV, Excel y bases de datos SQL.
- Permite acceder a los datos mediante índices o nombres para filas y columnas.
- Ofrece métodos para reordenar, dividir y combinar conjuntos de datos.
- Permite trabajar con series temporales.
- Realiza todas estas operaciones de manera muy eficiente.

---

## Tipos de datos de Pandas

Pandas dispone de tres estructuras de datos diferentes:

- **Series:** Estructura de una dimensión.
- **DataFrame:** Estructura de dos dimensiones (tablas).
- **Panel:** Estructura de tres dimensiones (cubos).

Estas estructuras se construyen a partir de arrays de la librería NumPy, añadiendo nuevas funcionalidades.

---

## Funciones principales de Pandas

```
pandas
  ├── Cargar
  ├── Modelar
  ├── Analizar
  ├── Manipular
  └── Preparar
```

---

## ¡Las preguntas de análisis de datos están en todas partes!

### Necesidad de científicos de datos!

Un científico de datos puede recopilar, analizar e interpretar datos de una variedad de fuentes (interacción social, procesos comerciales, sistemas ciberfísicos).

**¡Convierte datos en valor!!**
