# Solicitar al usuario una distancia en metros y transformar a km., cm. y mm. 
metros = float(input("ingrese la cantidad de metros: "))
Km = metros/1000
metros1 = metros%1000
cm = metros1/100
metros2 = metros1%100
mm = metros2/10
metros3 = metros2%10
print(f"Km {Km}")
print(f"cm {cm}")
print(f"mm {metros2}")
