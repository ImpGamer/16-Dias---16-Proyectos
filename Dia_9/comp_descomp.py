"""
Con python y sus modulos podemos comprimir archivos y descomprimirlos
como si lo hicieramos manualmente o con un programa especial
"""
import zipfile
import shutil

mi_zip = zipfile.ZipFile('archivos_comprimidos.zip','w') #Creacion del archivo .zip

#Introducir archivos dentro del .zip (comprimir)
mi_zip.write('./Dia_9/mi_texto_A.txt')
mi_zip.write('./Dia_9/mi_texto_B.txt')

abrir_zip = zipfile.ZipFile('./Dia_9/archivos_comprimidos.zip','r')
#Extraera todo lo que posee el archivo zip (descompresion)
abrir_zip.extractall()

class withShutil:
    def __init__(self,carpeta_destino,archivo):
        self.carpeta_destino = carpeta_destino #Carpeta o archivo que se comprimira
        self.archivo = archivo #Nombre del archivo .zip
    
    def crear_mover(self):
        shutil.make_archive(self.archivo,'zip',self.carpeta_destino)

    def descomprimir(self):
        shutil.unpack_archive(self.archivo+".zip",self.archivo,'zip')

archivo_zip = withShutil(carpeta_destino='./Dia_9',archivo='Dia_9_comprimido')
archivo_zip.descomprimir()