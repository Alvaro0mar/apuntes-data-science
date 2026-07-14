import numpy as np
import pandas as pd

a = 1000
print(a)
b = 8
print(b)
c = a + b
print(c)

arreglo = np.array([1, 2, 3, 4, 5])
print(arreglo)
print("Suma con numpy:", arreglo.sum())

datos = pd.DataFrame({"nombre": ["Ana", "Luis"], "edad": [23, 30]})
print(datos)
aa = True

print("suma: ", a + b)
print("resta: ", a-b)
print("multiplicación: ", a*b)
print("división: ", a/b)
print("potencia: ", a**b)
print("módulo: ", a % b)
print("división entera: ", a//b)
print("división: ", a/b)
