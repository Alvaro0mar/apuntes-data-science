# Clase 2

## Comentarios de varias líneas

Cuando se desea hacer un comentario de varias líneas, se puede utilizar tres comillas al inicio y tres comillas al final, como en este ejemplo.

> Este es un comentario de varias líneas.

Sin embargo, en Jupyter no se puede tener una celda con solo un comentario de varias líneas, así que se añadirá al final una variable que no hace nada.

```python
"""
Este es un comentario de varias líneas.
"""
a = 0
```

---

## Repaso

Ingresar un número por teclado e indicar si es negativo, si es 0, si es menor que 100, o si es mayor o igual a 100.

```python
n = input("Ingresar un número:")
# Dado que input retorna una cadena de caracteres (string) es necesario convertir esta cadena en un número
n = float(n)  # También se podría utilizar "int(n)" o "eval(n)"

if (n<0):
    print("{} es un número negativo".format(n))
elif (n==0):
    print("El número es 0")
elif (n<100):
    print("{} es menor que 100".format(n))
else:
    print("{} es mayor o igual a 100".format(n))
```

**Salida:**
```
Ingresar un número:25
25.0 es menor que 100
```

---

## Bucles (loops)

Existen dos formas principales de realizar bucles: utilizando `for` o utilizando `while`.

Se puede utilizar `for` con el formato `for i in range(n):`, donde `n` es un número entero. El funcionamiento es el siguiente: `range(n)` genera números enteros de 0 a n-1 (es decir, crea la secuencia 0, 1, 2, ..., n-1) y los asigna a la variable `i` en cada iteración. Así, el bucle `for` se ejecutará `n` veces. La primera vez, `i=0`, la segunda `i=1`, y así sucesivamente, hasta que en la última iteración `i=n-1`.

```python
# El siguiente bucle se repite 4 veces y los valores que toma i en cada iteración son 0, 1, 2, 3.
for i in range(4):
    print(i)
```

**Salida:**
```
0
1
2
3
```

### Ejemplo: factorial de un número

El factorial de un número `n` se puede obtener multiplicando `1*2*3*...*n`. En forma de bucle, la idea es multiplicar de dos en dos almacenando el resultado. Es decir, en el primer bucle `f = 1*1 = 1`, en el segundo `f = 2*f = 2*1 = 2`, en el tercero `f = 3*f = 3*2 = 6`, en el cuarto `f = 4*f = 4*6 = 24`, y así sucesivamente.

```python
num = 5   # Número del cual se desea obtener el factorial
fact = 1  # Valor inicial del factorial

for i in range(num):   # Bucle que se repite tantas veces como indica el mismo número
    fact *= (i+1)       # Se usa i+1, ya que se desea comenzar con 1, pero i comienza en 0
                         # La línea anterior es equivalente a fact=fact*(i+1)
print(fact)
```

**Salida:**
```
120
```

### La sentencia `pass`

Si un bucle o un condicional no tiene nada de contenido, habría un error. Para evitar este error se utiliza la sentencia `pass`. Esta sentencia solamente evita que haya errores, pero no hace nada además de eso.

```python
# El siguiente bucle se repite 10 veces pero no hace nada en cada iteración
for i in range(10):
    pass
```

### Bucle `while`

En el caso del bucle `while`, el formato es `while(condicion):`. Mientras la condición sea verdadera, el bucle se ejecuta. A diferencia del bucle `for`, en el bucle `while` no se indica cuántas veces se debe repetir el bucle.

```python
# En este ejemplo, se inicializa la variable i a 0, y el bucle while se ejecuta mientras
# el valor de i sea menor a 5. Es importante notar que dentro del bucle se debe
# explícitamente incrementar el valor de i, de lo contrario sería un bucle infinito
# (i siempre sería menor que 5)
i = 0
while (i<5):
    print(i)
    i += 1  # Equivalente a: i = i + 1
```

**Salida:**
```
0
1
2
3
4
```

### La sentencia `continue`

La sentencia `continue` detiene la iteración actual y sigue con la siguiente iteración. Es decir, cuando en un bucle se encuentra `continue`, las sentencias que siguen a `continue` no son ejecutadas sino que se pasa a la siguiente iteración.

**Ejemplo:** mostrar números del 1 al 6 sin incluir el 4. Idea: cuando en el bucle se encuentre el 4, se usará un `continue` para evitar que se muestre su valor.

```python
i = 1  # Inicialización de i a 1
while (i<=6):  # Este bucle se repite mientras i sea menor o igual a 6
    if (i==4):    # Si i es igual a 4 ...
        i += 1     # Incrementar i a 5
        continue   # Continuar a la siguiente iteración sin ejecutar el print que sigue
    print(i)
    i += 1  # Incrementar i. Esto es equivalente a i = i + 1
```

**Salida:**
```
1
2
3
5
6
```

### La sentencia `break`

La sentencia `break` detiene la iteración actual y sale completamente fuera del bucle. Es decir, cuando en un bucle se encuentra `break`, se fuerza la terminación del bucle.

**Ejemplo:** mostrar números impares del 5 al 9. Idea: cuando `i` en el bucle sea mayor a 9 (en este caso 11, debido a que se está utilizando números impares) se detendrán las iteraciones (se saldrá del bucle). Notar que se usa un bucle infinito, y si no hubiera un `break`, se imprimirían números impares infinitamente.

```python
i = 5  # Inicialización en 5
while (True):  # Bucle infinito (la condición siempre es verdadera "True")
    if (i==11):   # Cuando i es 11 ...
        break      # break hace que se termine el bucle (que se salga por completo del bucle)
    print(i)
    i += 2  # Incrementa i de 2 en 2. Equivalente a: i = i + 2
```

**Salida:**
```
5
7
9
```

---

## Listas

Una lista en Python es un contenedor de datos (cualquier tipo de datos). Sus valores son modificables. Su declaración se realiza con `[]`, y los datos van separados por comas.

```python
# Declaración de 3 listas diferentes: a, b y c
a = [4, 7, 0, 1, 5]                              # Esta lista contiene solo números
b = ['cebollas', 'naranjas', 'yucas']            # Esta lista contiene solo cadenas de caracteres
c = [0, 'camiones', 9, 3.14, 'computadoras']     # Esta lista contiene números y cadenas de caracteres

print(a)
print(b)
print(c)

# Todas las listas son de tipo "list"
print("Tipo de una lista: ", type(b))  # En lugar de usar type(b), se puede usar: b.__class__
```

**Salida:**
```
[4, 7, 0, 1, 5]
['cebollas', 'naranjas', 'yucas']
[0, 'camiones', 9, 3.14, 'computadoras']
Tipo de una lista:  <class 'list'>
```

### Indexación de listas

Para acceder a cada elemento de la lista, se escribe el nombre de la lista seguido de `[i]`, donde `i` (llamado índice) es la posición del elemento deseado. Esta posición comienza a partir de 0 para el primer elemento. Al hecho de obtener un elemento de la lista se denomina indexación de la lista.

```python
b = ['cebollas', 'naranjas', 'yucas']

# Indexación de la lista:
print("b[0] es: ", b[0])  # Primer elemento de b
print("b[1] es: ", b[1])  # Segundo elemento de b
print("b[2] es: ", b[2])  # Tercer elemento de b
```

**Salida:**
```
b[0] es:  cebollas
b[1] es:  naranjas
b[2] es:  yucas
```

Para indexar varios elementos se utiliza el nombre de la lista seguido de los corchetes: `[indice_inicial : indice_final+1]`, donde los elementos a indexar irán desde el `índice_inicial` hasta el `índice_final+1`.

```python
# Indexación de varios elementos de la lista
b = ['cebollas', 'naranjas', 'yucas', 'camotes', 'tomates', 'mandarinas', 'manzanas']
print(b[1:5])  # Indexa la lista desde el índice 1 hasta el índice 4
```

**Salida:**
```
['naranjas', 'yucas', 'camotes', 'tomates']
```

### Longitud de una lista

La longitud de una lista se puede obtener utilizando el comando `len`.

```python
lista = ['cebollas', 'naranjas', 'yucas', 'camotes', 'tomates', 'mandarinas']
print("Lista: ", lista)
longitud_lista = len(lista)  # Número de elementos de la lista
print("La lista tiene {} elementos".format(longitud_lista))
```

**Salida:**
```
Lista:  ['cebollas', 'naranjas', 'yucas', 'camotes', 'tomates', 'mandarinas']
La lista tiene 6 elementos
```

### Concatenación de listas

Para concatenar dos listas se utiliza el operador `+`.

```python
lista1 = ['manzanas', 'peras']
lista2 = ['naranjas', 'tomates']
lista3 = lista1 + lista2  # Concatenación de la lista1 con la lista2
print("lista3: ", lista3)

# Usando concatenación también se puede aumentar elementos al inicio o al final de una lista
lista1 = ['mandarinas'] + lista1  # Aumentar elementos al inicio de la lista
print("lista1 aumentada: ", lista1)
```

**Salida:**
```
lista3:  ['manzanas', 'peras', 'naranjas', 'tomates']
lista1 aumentada:  ['mandarinas', 'manzanas', 'peras']
```

### Modificación de elementos

Las listas son modificables (o "mutables"). Esto significa que sus elementos pueden modificarse, añadirse, o eliminarse. Para modificar un elemento, solo se debe indexar el elemento y asignarlo a otro valor.

```python
lista = ['naranjas', 'cebollas', 'yucas']  # Lista inicial
print("Lista inicial: ", lista)

lista[0] = 'manzanas'  # Modificación del elemento 0
lista[2] = 'tomates'   # Modificación del elemento 2
print("Lista modificada: ", lista)
```

**Salida:**
```
Lista inicial:  ['naranjas', 'cebollas', 'yucas']
Lista modificada:  ['manzanas', 'cebollas', 'tomates']
```

### Métodos de listas

Algunos métodos para el uso de listas son los siguientes:

- `append(x)`: añade el elemento x al final de la lista
- `pop()`: remueve el último elemento de la lista
- `pop(i)`: remueve el elemento con índice i
- `remove(x)`: remueve el primer elemento x que aparece en la lista
- `clear()`: borra todos los elementos de la lista
- `index(x)`: retorna el índice que tiene el primer elemento x en la lista
- `insert(i, x)`: inserta el elemento x en el índice i
- `sort()`: ordena los elementos de forma ascendente
- `count(x)`: retorna el número de veces que aparece x en la lista
- `reverse()`: invierte el orden de los elementos en la lista

```python
lista = [4, 7, 0, 1, 5]  # Lista inicial
print("Lista inicial: ", lista)

lista.append('hola')  # Añade 'hola' al final de la lista
lista.append('chau')  # Añade 'chau' al final de la lista
print("Lista luego de usar append 2 veces: ", lista)

lista.pop()  # Remueve el último elemento de la lista
print("Lista luego de usar pop() una vez: ", lista)

lista.pop()  # Remueve el último elemento de la lista
print("Lista luego de usar pop() otra vez: ", lista)

lista.pop(3)  # Remueve el elemento con índice 3 (cuyo valor es "1", en este caso)
print("Lista luego de usar pop(3): ", lista)
```

**Salida:**
```
Lista inicial:  [4, 7, 0, 1, 5]
Lista luego de usar append 2 veces:  [4, 7, 0, 1, 5, 'hola', 'chau']
Lista luego de usar pop() una vez:  [4, 7, 0, 1, 5, 'hola']
Lista luego de usar pop() otra vez:  [4, 7, 0, 1, 5]
Lista luego de usar pop(3):  [4, 7, 0, 5]
```

```python
lista = [0, 'camiones', 3.14, 'computadoras', 'camiones']
print("Lista inicial: ", lista)

idx_camiones = lista.index('camiones')  # Índice del primer elemento camiones en la lista
print("El índice del primer elemento camiones es: ", idx_camiones)

lista.remove('camiones')  # Remueve la primera aparición de "camiones" en la lista
print("Lista luego de remove(camiones) es: ", lista)

lista.insert(2, "manzanas")
print("Lista luego de insertar manzanas en el índice 2: ", lista)

lista.clear()
print("Lista luego de usar clear(): ", lista)
```

**Salida:**
```
Lista inicial:  [0, 'camiones', 3.14, 'computadoras', 'camiones']
El índice del primer elemento camiones es:  1
Lista luego de remove(camiones) es:  [0, 3.14, 'computadoras', 'camiones']
Lista luego de insertar manzanas en el índice 2:  [0, 3.14, 'manzanas', 'computadoras', 'camiones']
Lista luego de usar clear():  []
```

```python
lista1 = [4, 7, 0, 1, 5]
print("Lista1 inicial: ", lista1)
lista1.sort()  # Ordena números de forma ascendente
print("Lista1 ordenada con sort(): ", lista1)

lista2 = ['naranjas', 'cebollas', 'yucas', 'almendras']
print("\nLista2 inicial: ", lista2)
lista2.sort()  # Ordena cadenas de caracteres alfabéticamente
print("Lista2 ordenada con sort(): ", lista2)
```

**Salida:**
```
Lista1 inicial:  [4, 7, 0, 1, 5]
Lista1 ordenada con sort():  [0, 1, 4, 5, 7]

Lista2 inicial:  ['naranjas', 'cebollas', 'yucas', 'almendras']
Lista2 ordenada con sort():  ['almendras', 'cebollas', 'naranjas', 'yucas']
```

```python
lista = [9, 'camiones', 9, 9, 'computadoras', 'camiones']
print("Lista: ", lista)

n_camiones = lista.count('camiones')  # Cuenta cuántas veces aparece camiones en la lista
print("El elemento camiones aparece {} veces en la lista".format(n_camiones))

n_manzanas = lista.count('manzanas')  # Cuenta cuántas veces aparece manzanas en la lista
print("El elemento manzanas aparece {} veces en la lista".format(n_manzanas))

lista.reverse()  # Invertir el orden de los elementos en la lista
print("La lista luego de usar reverse() es: ", lista)
```

**Salida:**
```
Lista:  [9, 'camiones', 9, 9, 'computadoras', 'camiones']
El elemento camiones aparece 2 veces en la lista
El elemento manzanas aparece 0 veces en la lista
La lista luego de usar reverse() es:  ['camiones', 'computadoras', 9, 9, 'camiones', 9]
```

---

## Tuplas (tuples)

Una tupla en Python es un contenedor de datos (cualquier tipo de datos) pero a diferencia de una lista, su característica principal es ser **inmutable**. Esto significa que sus valores no se pueden modificar. Su declaración se realiza con `()`, y los datos van separados por comas.

```python
tupla = (4, 7, 0, 1, 5, 4, 3, 4)  # Creación de una tupla
print("La siguiente es una tupla: ", tupla)
print("El tipo de una tupla es: ", tupla.__class__)  # Equivalentemente, se puede usar: type(tupla)
```

**Salida:**
```
La siguiente es una tupla:  (4, 7, 0, 1, 5, 4, 3, 4)
El tipo de una tupla es:  <class 'tuple'>
```

```python
# Una tupla es inmutable (no se puede modificar)
# La ejecución del siguiente comando lleva a un error
tupla[0] = 40
```

**Salida (error):**
```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-21-504b9a437f60> in <module>
      2
      3 # La ejecución del siguiente comando lleva a un error
----> 4 tupla[0] = 40

TypeError: 'tuple' object does not support item assignment
```

### Métodos de tuplas

Algunos métodos para el uso de tuplas son:

- `count(x)`: cuenta cuántas veces aparece el elemento x en la tupla
- `index(x)`: retorna el índice del elemento x

```python
tupla = (4, "naranjas", 0, "naranjas", 5, 4, "peras", 4)
print("Tupla: ", tupla)

cnt = tupla.count(4)  # Cuenta cuántas veces aparece "4" en la tupla
print("El elemento 4 aparece {} veces en la tupla".format(cnt))

idx_naranjas = tupla.index('naranjas')  # índice de la primera aparición de "naranjas" en la lista
print("El índice del primer elemento naranjas en la lista es: ", idx_naranjas)
```

**Salida:**
```
Tupla:  (4, 'naranjas', 0, 'naranjas', 5, 4, 'peras', 4)
El elemento 4 aparece 3 veces en la tupla
El índice del primer elemento naranjas en la lista es:  1
```

```python
# Al igual que para listas, el número de elementos de una tupla se obtiene con "len"
tupla = (4, "naranjas", 0, "naranjas", 5, 4, "peras", 4)
print("Tupla: ", tupla)
nelementos = len(tupla)
print("La tupla tiene {} elementos".format(nelementos))
```

**Salida:**
```
Tupla:  (4, 'naranjas', 0, 'naranjas', 5, 4, 'peras', 4)
La tupla tiene 8 elementos
```

---

## Bucles usando listas o tuplas

Si `lst` es una lista, el formato del bucle `for` para iterar cada elemento de esta lista es: `for i in lst:`. En este bucle, en la primera iteración, el valor de `i` será `lst[0]`, en la segunda iteración el valor de `i` será `lst[1]` y así sucesivamente hasta iterar todos los elementos de la lista. Lo mismo es válido para una tupla.

```python
# Mostrar los elementos de una tupla usando una iteración
tupla = ('naranjas', 'cebollas', 'manzanas', 'almendras')
for i in tupla:  # i contendrá cada elemento de la tupla
    print(i)
```

**Salida:**
```
naranjas
cebollas
manzanas
almendras
```

```python
# Recorrer todos los elementos de la lista y avisar cuando se encuentre "almendras"
lista = ['naranja', 'cebolla', 'almendra', 'manzana']
for i in lista:  # i contendrá cada elemento de la lista
    if(i=='almendras'):  # compara el elemento actual con "almendras"
        print('El elemento {} es una almendra'.format(i))
    else:
        print('El elemento {} no es una almendra'.format(i))
```

**Salida:**
```
El elemento naranja no es una almendra
El elemento cebolla no es una almendra
El elemento almendra no es una almendra
El elemento manzana no es una almendra
```

---

## Listas o tuplas anidadas (nested)

Las listas o tuplas se pueden anidar; es decir, se puede colocar una lista o tupla como un elemento de otra lista o tupla.

```python
# Listas anidadas
# Cada elemento de la lista "a" es otra lista
a = [[1,2], [3,6], [4,8], [5,2]]
print("Lista a: ", a)

# Indexación de elementos de a:
print("Elemento a[0]: ", a[0])
print("Elemento a[1]: ", a[1])
print("Elemento a[2]: ", a[2])
print("Elemento 0 de a[0] es a[0][0]: ", a[0][0])  # Elemento 0 de a[0]
print("Elemento 1 de a[0] es a[0][1]: ", a[0][1])  # Elemento 1 de a[0]
print("Elemento 1 de a[2] es a[2][1]: ", a[2][1])  # Elemento 1 de a[2]
```

**Salida:**
```
Lista a:  [[1, 2], [3, 6], [4, 8], [5, 2]]
Elemento a[0]:  [1, 2]
Elemento a[1]:  [3, 6]
Elemento a[2]:  [4, 8]
Elemento 0 de a[0] es a[0][0]:  1
Elemento 1 de a[0] es a[0][1]:  2
Elemento 1 de a[2] es a[2][1]:  8
```

---

## Ejercicio

Realizar una función llamada `distancia` que tome como parámetros de entrada una lista de puntos con el formato `((x1,y1), (x2,y2), (x3,y3), ...)` y que retorne la distancia euclideana de dichos puntos al origen `(d1, d2, d3, ...)`, donde `di` corresponde a la distancia euclideana del punto `(xi, yi)`.

> **Nota:** la distancia euclideana de un punto `(x, y)` al origen está dada por: `√(x² + y²)`. Para usar la raíz cuadrada, se debe importar la librería numpy: `import numpy as np`, y luego se debe usar la función `np.sqrt`.

```python
# Importar la librería numpy (que permite calcular la raíz cuadrada)
import numpy as np

# Definición de la función
def distancia(puntos):
    ds = []  # Inicialización de una lista vacía
    for p in puntos:  # Para cada elemento de puntos (p es el elemento)
        d = np.sqrt(p[0]**2 + p[1]**2)  # Distancia euclideana del punto p actual
        ds.append(d)  # Almacenamiento de la distancia "d" en la lista "ds"
    return tuple(ds)  # Convierte la lista "ds" en tupla y retorna su valor

# Puntos de prueba
puntos_prueba = ((3,2), (1,5), (6,3), (3,4))

# Llamada a la función, con los puntos de prueba
dist = distancia(puntos_prueba)
print("Los puntos son: ", puntos_prueba)
print("Las distancias son: ", dist)
```

**Salida:**
```
Los puntos son:  ((3, 2), (1, 5), (6, 3), (3, 4))
Las distancias son:  (3.605551275463989, 5.0990195135927845, 6.708203932499369, 5.0)
```
