"""
Programa que permita determinar el salario a pagar a un empleado, teniendo como entradas el 
 salario diario y el número de días trabajados. Tenga en cuenta que al empleado se le debe
 descontar el 10% por concepto de pensión y 15% por concepto de salud.

"""
salario_diario = float(input("Ingrese el salario diario del empleado: "))
dias_trabajados = int(input("Ingrese el número de días trabajados: "))

salario_basico = salario_diario * dias_trabajados
descuento_pension = salario_basico * 0.10
descuento_salud = salario_basico * 0.15
salario_neto = salario_basico - (descuento_pension + descuento_salud)

print(f"Salario basico: {salario_basico}")
print(f"Descuento pensión: {descuento_pension}")
print(f"Descuento salud: {descuento_salud}")
print(f"Salario neto: {salario_neto}")