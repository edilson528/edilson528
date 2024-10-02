"""
Programa que permita calcular la edad de una persona conociendo el año actual y el usuario digita su año de nacimiento.
"""
año = int(input("ingrese su año de nacimiento: "))
año_actual = int(input("ingrese el año actual: "))
edad = año_actual - año
print(f"su edad es {edad} años")
