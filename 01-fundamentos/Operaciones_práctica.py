import numpy as np
import pandas as pd

a = 1000
print(a)
b = 8
print(b)
c = a + b
print(c)

print("suma: ", a + b)
print("resta: ", a-b)
print("multiplicación: ", a*b)
print("división: ", a/b)
print("potencia: ", a**b)
print("módulo: ", a % b)
print("división entera: ", a//b)

a += 2000
print(a)
a -= 2000
print(a)
a **= 2
print(a)

a = 1000
print(a)

print("la variable a es ", a, "y la variable b es ", b)
print(f"la variable a es {a} y la variable b es {b}")
print("la variable a es {} y la variable b es {}".format(a, b))

vnombre = input("Ingrese su nombre: ")
print("Hola", vnombre, "bienvenido a la clase")

s1 = "Hola"
s2 = "Mundo"
s3 = s1 + s2
print(s3)
print(s1[0]+s2[0])
print(s1[0:2]+s2[3:5])


def funcion1(a, b):
    c = 5*a + 10*b
    return c
    return 5*a + 10*b


print(funcion1(2, 3))


def funcion1(a, b):
    c = 5*a + 10*b
    return c
    return 5*a + 10*b


resultado = funcion1(2, 3)
print("resultado:", resultado)


a = 50
b = 80

if (a > b):
    print("a es mayor que b")
elif (a < b):
    print("a es menor que b")
else:
    print("a es igual que b")
