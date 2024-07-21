def reducir_lista(lista):
    lista_sin_duplicados = list(set(lista))
    
    valor_mas_alto = max(lista_sin_duplicados)
    lista_sin_duplicados.remove(valor_mas_alto)
    
    return lista_sin_duplicados

def promedio(lista_reducida):
    promedio = 0
    for number in lista_reducida:
        promedio += number
    
    return promedio / len(lista_reducida)

print(reducir_lista([20,1,4,30,22]))