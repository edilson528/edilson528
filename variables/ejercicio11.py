# Programa que solicite un número al usuario y permita calcular la raíz cuadrada del mismo (sin usar función). 
from cmath import sqrt
import math

numero = float(input("digite el numero para calcular: "))
raiz = math.sqrt(numero)
print( "la raiz cuadrada es:", raiz)

