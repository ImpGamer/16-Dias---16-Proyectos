import datetime
from datetime import date

fechaActual = datetime.date(2024,11,20)
print(fechaActual.year)

otra_fecha = datetime.date(2024,10,1)
if fechaActual.year == otra_fecha.year:
    print("Es el mismo anio")


nacimiento = date(1995,3,5)
defuncion = date(2094,6,19)

vida = defuncion - nacimiento
print(vida)

# hoy = date.today()
# print(hoy)

min_actual = datetime.datetime.today()
print(min_actual.minute)