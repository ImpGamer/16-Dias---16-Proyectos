from collections import Counter
from collections import defaultdict
"""
El objeto Counter() de collections, nos permite hacer de una manera mas sencilla,
saber cuantos elementos repetidos hay en un objeto que posee indices o muchos valores
"""

numeros = [2,4,15,16,23,2,1,3,3,4,0,1]
print(Counter(numeros))

texto = "mi_String"
print(Counter(texto))
#Imprime los 2 valores mas repetidos
print(Counter(numeros).most_common(2))

#En caso que accedamos a un valor nulo de una key en un diccionario, se le asignara como 'nada'
mi_dic = defaultdict(lambda: 'nada')    
mi_dic['color'] = 'verde'

"""
Existen muchos mas metodos y objetos de este directorio, pero son inmensos,
y este archivo se haria muy largo
"""