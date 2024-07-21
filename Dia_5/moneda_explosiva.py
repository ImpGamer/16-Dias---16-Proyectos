from random import randint
def lanzar_moneda():
    num_aleatorio = randint(1,2)
    return "Cara" if num_aleatorio == 1 else "Cruz"

def probar_suerte(resultado_moneda,lista):
    match resultado_moneda:
        case "Cara":
            print("La lista se autodestruira")
            return []
        case "Cruz":
            print("La lista fue salvada")
            return lista
        case _:
            print("Probabilidad no marcada. Datos invalidos")

lista = [0,29,33,10,2,30]
lista = probar_suerte(lanzar_moneda(),lista)
print(lista)