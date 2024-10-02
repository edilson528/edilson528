# Solicitar tiempo en segundos y transformar a horas y minutos. 
segundos = int(input("ingresar el tiempo solo en segundos: "))
horas = segundos//3600
segundos1 = segundos%3600
minutos = segundos1//60
segundos2 = segundos1%60
print(f"horas: {horas}")
print(f"munutos: {minutos}")
print(f"segundos: {segundos2}")
