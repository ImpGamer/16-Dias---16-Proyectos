import numpy as np
import pandas
#Creacion de arreglos unidimensionales
array_unidim = np.array([1,2,3,4,5])
#Creacion de un arreglo bidimensional o matriz
array_bidim = np.array([[1,2,3],[4,5,6]])
#Creacion de arreglos tridimensionales
array_tridim = np.array([[[1,2,3],
                        [4,5,6]],
                         [[7,8,9],
                          [10,11,12]]])
#Saber datos, dimensaiones, tipo, tamanio y tipo
array_unidim.shape, array_unidim.ndim,array_unidim.dtype,array_unidim.size,type(array_unidim)
#Visualizacion de la matriz con un DataFrame de pandas
datos = pandas.DataFrame(array_bidim)
print(datos)
#Creacion de una matriz llena de valores 1
unos = np.ones((4,3))
print(unos)
#Creacion de un array de 0 a 100 que vaya salteando de 5 en 5
array_1 = np.arange(0,100,5)
print(array_1)
#Creacion de una matriz de 3 filas - 5 columnas, con valores aleatorios entre 0 y 10
array_2 = np.random.randint(0,10,(3,5))
#Extraccion de valores unicos (no repetidos) dentro del array_2
unicos_2 = np.unique(array_2)