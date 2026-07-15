# Clase 1

## Tipos de Variables

Los principales tipos de variables en Python son:

- **Variables enteras (`int`).**
- **Variables de punto flotante (`float`).** Siempre tienen parte decimal.
- **Variables que contienen cadenas de caracteres (`string`).** Los valores van siempre entre comillas simples o dobles (`"` o `'`).
- **Variables Booleanas (`Bool`).** Pueden tomar dos valores: verdadero o falso (`True`/`False`).

Para asignar un valor a una variable se usa el signo `=`.

```python
variable1 = 10      # variable entera ("int")
variable2 = 2.5      # variable de punto flotante ("float")
variable3 = "hola"   # variable de cadena de caracteres ("string")
variable4 = True     # variable Booleana (True/False)

print(variable1)  # Print muestra mensajes en la pantalla
print(variable2)
print(variable3)
print(variable4)
```

**Salida:**
```
10
2.5
hola
True
```

---

## Operadores Aritméticos Básicos

Son la suma (`+`), resta (`-`), multiplicación (`*`), división (`/`), división entera (`//`), módulo o residuo (`%`), potencia (`**`).

> La división entera descarta la parte fraccional y solo muestra la parte entera del cociente.

```python
# Creación de dos variables (a y b)
a = 7; b = 2  # Para tener 2 expresiones en una misma línea se usa el ";"

print("suma: ", a+b)                  # Suma de 2 variables
print("resta:", a-b)                  # Resta de 2 variables
print("multiplicación:", a*b)         # Multiplicación de 2 variables
print("división:", a/b)               # División de 2 variables (el resultado es "float")
print("división entera:", a//b)       # División de 2 variables (solo mantiene la parte entera)
print("módulo (residuo):", a%b)       # Residuo de la división entera de a/b
print("potencia:", 2**5)              # Potencia (en el ejemplo: 2 elevado a la 5ta potencia)
```

**Salida:**
```
suma:  9
resta: 5
multiplicación: 14
división: 3.5
división entera: 3
módulo (residuo): 1
potencia: 32
```

### Operadores de asignación compuesta

```python
var = 30       # Asignación de 30 a la variable "var"
var += 20      # Equivalente a: var = var + 20 (en este caso: var = 30 + 20)
print(var)     # Imprime el valor 50

var -= 10      # Equivalente a: var = var - 10 (en este caso: var = 50 - 10)
print(var)     # Imprime el valor 40

var *= 5       # Equivalente a: var = var * 5 (en este caso: var = 40 * 5)
print(var)     # Imprime el valor 200

# Nota: se puede también usar "/=", "//=" con la misma lógica
```

**Salida:**
```
50
40
200
```

---

## Salida en Python

Para mostrar mensajes en la pantalla se utiliza el comando `print`.

```python
a = 10; b = 20  # Declaración de 2 variables: a y b

# Forma 1: La cadena de caracteres se escribe entre comillas.
# Para la separación con las variables se utiliza ",".
print("La variable a es", a, "y la variable b es", b)

# Forma 2: El lugar donde van las variables, en la cadena de caracteres,
# se indica con "{}". Luego se escribe ".format()" y dentro del paréntesis
# se escriben las variables separadas por comas.
print("La variable a es {} y la variable b es {}".format(a,b))

# Ambas formas son equivalentes
```

**Salida:**
```
La variable a es 10 y la variable b es 20
La variable a es 10 y la variable b es 20
```

---

## Entrada de Datos en Python

Para ingresar datos de manera interactiva utilizando el teclado se utiliza `input`.

```python
# Dentro de las comillas del comando input se escribe el mensaje que aparecerá en pantalla.
# Lo ingresado por teclado se almacenará en la variable "vnombre". Lo almacenado en esta
# variable se encuentra en formato de cadena de caracteres (string)
vnombre = input("Ingresar un nombre: ")

# Salida en pantalla de la variable ingresada
print("El nombre ingresado es:", vnombre)
```

**Salida:**
```
Ingresar un nombre: Juan
El nombre ingresado es: Juan
```

---

## Operaciones Básicas con "strings"

La concatenación de cadenas de caracteres (strings) utiliza el operador `+`.

Cada letra de una cadena de caracteres puede ser indexada. Por ejemplo, si la cadena es `s="python"`, se tiene lo siguiente: `s[0]` es `"p"`, `s[1]` es `"y"`, `s[2]` es `"t"`, `s[3]` es `"h"`, `s[4]` es `"o"`, `s[5]` es `"n"`. Notar que los índices siempre comienzan con 0. Una cosa importante es, que en rangos [inicio:fin] el índice final no se incluye, el inicio si cuenta pero el fin no.

```python
s1 = "Hola"       # Primera cadena de caracteres (string)
s2 = "mascotas"   # Segunda cadena de caracteres (string)
s3 = s1 + " " + s2  # La concatenación de cadenas de caracteres utiliza el operador "+"

print(s3)
print(s1[3]+s1[0])  # s1[3] es "a", s1[0] es "H", y "+" concatena ambas letras
print(s2[0:3])       # Recupera los índices 0, 1, 2 de la cadena s2; es decir "mas"
print(s2[2:5])       # Recupera los índices 2, 3, 4 de la cadena s2; es decir "sco"
```

**Salida:**
```
Hola mascotas
aH
mas
sco
```

---

## Introducción a Funciones

Para definir una función en Python se utiliza la palabra `def` seguida del nombre de la función. Luego del nombre de la función, se coloca entre paréntesis los argumentos de la función, seguidos de `:`.

Es importante que la función retorne un valor utilizando la palabra `return`.

De igual manera es importante la indentación o sangrado: todo lo que está dentro de la función debe estar indentado (con espacios del margen izquierdo, que normalmente se obtiene presionando una vez la tecla de tabulación `tab`).

```python
# Ejemplo de función llamada "funcion1".
# Esta función toma dos parámetros de entrada (a y b), y retorna la operación 2*a+5*b

# Forma 1: creando una variable temporal llamada "c"
def funcion1(a, b):
    c = 2*a + 5*b
    return c

# Forma 2: retornando directamente el resultado (el comportamiento es igual al de "funcion1")
def funcion2(a, b):
    return 2*a + 5*b

# Llamada a la función con los parámetros 10 y 20 (es decir, a=10, b=20).
# El valor retornado se almacena en la variable resultado, y luego se muestra este resultado
resultado = funcion1(10,20)
print(resultado)

# De manera equivalente, se puede mostrar el resultado sin utilizar la variable "resultado",
# ya que se muestra directamente lo que la función retorna
print(funcion1(10,20))
```

**Salida:**
```
120
120
```

---

## Sentencias Condicionales

Las sentencias condicionales utilizan las palabras `if`, `elif`, `else`.

Para la primera condición se utiliza `if(condicion1):`, para las siguientes `elif(condicion2):`, `elif(condicion3):`, ..., y para la última condición (cuando ninguna de las anteriores se ha cumplido) se utiliza `else:`. Notar que `else` no lleva asociada ninguna condición, ya que se verifica cuando ninguna de las anteriores condiciones han sido verdaderas.

Cuando se verifica una condición, puede haber varios `elif`, pero solo un `if` y solo un `else`.

```python
a = 7; b = 5  # Declaración de 2 variables a y b

if (a>b):  # Si se cumple que a>b, se imprime la línea que sigue, de lo contrario se sigue con elif
    print("{} es mayor que {}".format(a,b))
elif (a==b):  # Si no se cumple la anterior condición, se verifica si a es igual a b
    print("{} es igual a {}".format(a,b))
else:  # Si ninguna de las anteriores condiciones es verdadera, se imprime la línea que sigue
    print("{} es menor que {}".format(a,b))
```

**Salida:**
```
7 es mayor que 5
```

```python
"""
Este ejemplo es similar al anterior, pero las condiciones se verifican dentro de una función.
Notar la indentación (espaciado desde la izquierda) dentro de la función.
En este caso, la función no retorna ningún valor debido a que solo se está mostrando (con un
print) un mensaje de cuál es mayor, menor o igual.
"""
def comparar(a, b):
    if (a>b):
        print("{} es mayor que {}".format(a,b))
    elif (a==b):
        print("{} es igual a {}".format(a,b))
    else:
        print("{} es menor que {}".format(a,b))

# Llamadas a la función
comparar(7, 5)
comparar(4, 8)
comparar(3, 3)
```

**Salida:**
```
7 es mayor que 5
4 es menor que 8
3 es igual a 3
```

---

## Ejercicios

### 1. Ingresar por teclado lo siguiente: el primer número, el segundo número, el operador, y mostrar el resultado de aplicar el operador a ambos números

```python
n1 = input("Ingresar el primer número: ")
n2 = input("Ingresar el segundo número: ")
op = input("Ingresar el operador: ")
resultado = eval(n1+op+n2)
print("El resultado de {} {} {} es {}".format(n1, op, n2, resultado))
```

**Salida:**
```
Ingresar el primer número: 10
Ingresar el segundo número: 20
Ingresar el operador: *
El resultado de 10 * 20 es 200
```

### 2. Ingresar por teclado una nota (de 0 a 20) y mostrar un mensaje que muestre "desaprobado" si la nota va de 0 a 10, "regular" si va de 11 a 15, "muy bueno" si va de 16 a 17, "excelente" si va de 18 a 20

```python
nota = input("Ingresar nota: ")

# El valor retornado con "input" es una cadena de caracteres. Para que pueda ser un número
# es necesario usar "eval". Alternativamente se puede usar "int" (para convertirlo a entero)
# o "float" (para convertirlo a punto flotante)
nota = eval(nota)  # Equivalentemente se puede usar: nota=int(nota), o nota=float(nota)

if (nota<0) or (nota>20):
    print("La nota {} no es válida".format(nota))
elif (nota<=10):
    print("Desaprobado ({})".format(nota))
elif (nota<=15):
    print("Regular ({})".format(nota))
elif (nota<=17):
    print("Muy bueno ({})".format(nota))
else:
    print("Excelente ({})".format(nota))
```

**Salida:**
```
Ingresar nota: 15
Regular (15)
```

### 3. Convertir las anteriores condiciones a una función y probar todos los casos

```python
def evaluar_nota(nota):
    if (nota<0) or (nota>20):
        print("La nota {} no es válida".format(nota))
    elif (nota<=10):
        print("Desaprobado ({})".format(nota))
    elif (nota<=15):
        print("Regular ({})".format(nota))
    elif (nota<=17):
        print("Muy bueno ({})".format(nota))
    else:
        print("Excelente ({})".format(nota))

# Llamadas a la función
evaluar_nota(-2)
evaluar_nota(4)
evaluar_nota(11)
evaluar_nota(16)
evaluar_nota(19)
evaluar_nota(25)
```

**Salida:**
```
La nota -2 no es válida
Desaprobado (4)
Regular (11)
Muy bueno (16)
Excelente (19)
La nota 25 no es válida
```
