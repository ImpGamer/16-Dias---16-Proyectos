nombre = input("Ingrese su nombre: ")
venta_total = float(input("Ingresa la ventas totales del mes: "))

ganancia = venta_total*0.13

print(f"Ok {nombre} este mes ganaste: ${round(ganancia,2)}")