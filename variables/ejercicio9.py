"""
Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios elementos de la misma referencia. .

 Debe tener como entradas el valor unitario, la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.
"""
valor_unitario = float(input("ingrese el valor del producto: "))
unidades = int(input("ingrese el numero de productos: "))

valor_total_sin_iva = valor_unitario * unidades
iva = valor_total_sin_iva * 0.16
valor_total_con_iva = valor_total_sin_iva + iva

print(f"Valor total sin IVA: {valor_total_sin_iva}")
print(f"IVA (16%): {iva}")
print(f"Valor total con IVA: {valor_total_con_iva}")
