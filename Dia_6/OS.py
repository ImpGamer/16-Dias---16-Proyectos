#Importaremos la biblioteca 'os' que nos permitira interactuar con el sistema operativo mas facil
import os
from pathlib import Path
#Declaramos desde que directorio se ejecutara este programa
ruta= os.chdir('C:\\Users\\user\\OneDrive\\Escritorio\\SCP_txt')
#Este nos permite interactuar con el SO sin ser especifico (WIndows,Mac,Linux)
archivo = Path('C:\\Users\\user\\OneDrive\\Escritorio\\SCP_txt') / 'NIP.txt'

abrir = open(archivo)
print(abrir.read())

archivo = open('NIP.txt')
print(archivo.read())