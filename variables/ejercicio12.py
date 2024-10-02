# Calcular la hipotenusa con el Teorema de Pitágoras (sin usar funciones).
from math import sqrt

a = float(input("ingrese el valor de cateto a: "))
b = float(input("ingrese el valor de cateto b: "))
c = sqrt((a**2) +(b**2))
print(f"la hipotenusa del triangulo es: {c}")
