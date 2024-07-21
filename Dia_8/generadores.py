# def funcion():
#     lista = []
#     for x in range(1,5):
#         lista.append(x*10)
#     return lista

# def generador():
#     for x in range(1,5):
#         yield x*10

# print(funcion())
# print(generador())


def generador():
    n = 1
    while True:
        yield n
        n += 1

# Crear una instancia del generador
gen = generador()

# Ejemplo de uso: Obtener los primeros 10 números de la secuencia
for _ in range(10):
    print(next(gen))