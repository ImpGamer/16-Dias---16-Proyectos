def suma(*args):
    return sum(args)

def suma_cuadrados(*args):
    resultado =0
    for num in args:
        cuadrado = num**2
        resultado += cuadrado
    
    return resultado

def suma_absolutos(*args):
    resultado  =0
    for num in args:
        if num < 0:
            num = num * -1
            resultado += num
        else:
            resultado += num
    return resultado

def numeros_persona(nombre,*args):
    return f"{nombre} la suma de tus numeros es {sum(args)}"

#Tambien existe la indefinicion de argumentos "**kwargs"
"""
Los kwargs son un tipo de parametro que son indefinidos, pero no son variables independientes, se
trataran de diccionarios (clave,valor)
"""
def resta(**kwargs):
    valores = list(kwargs.values())
    resultado = valores[0]
    for valor in valores[1:]:
        resultado -= valor
    return resultado


print(resta(x=20,y=30,z=-22))
def describir_personsa(nombre,**caracteristicas):
    print(f"Caracteristicas de {nombre}")
    for clave,valor in caracteristicas.items():
        print(f"{clave}: {valor}")