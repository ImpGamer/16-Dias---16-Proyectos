#La funcion zip() de python nos permite unir valores de dos o mas listas a 1 sola

nombres = ["Mario","Alejandro","Rodrigo"]
edades = [20,30,21]
ciudades = ['Lima','Madrid','Barcelona']

datos = list(zip(nombres,edades,ciudades))

for nombre,edad,ciudad in datos:
    print(f"{nombre} tiene {edad} anios y vive en {ciudad}")
