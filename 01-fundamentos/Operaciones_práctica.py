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
