# Programa para calcular la distancia recorrida en un movimiento rectilíneo. Recuerde $x=v*t$ 
# donde $v$ es velocidad y $t$ es tiempo. Solicitar al usuario velocidad en kilómetros por hora (Km/h)
# y tiempo en horas (h) para obtener la distancia en kilómetros (Km).
v = float(input("ingrese la velocidad ,km x hora: "))
t = float(input("ingrese el tiempo de recorrido: "))
x =  v * t
print(input(f"su distancia recorrida es: {x}km"))

