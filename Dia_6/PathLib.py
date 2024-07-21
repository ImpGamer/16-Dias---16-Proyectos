from pathlib import Path

#Manera mas sencilla de leer un archivo
carpeta = Path('C:/Users/user/OneDrive/Escritorio/SCP_txt/NIP.txt')
print(carpeta.read_text())

sufijoArchivo = carpeta.suffix
if sufijoArchivo == '.txt':
    print("El archivo se puede abrir en bloc de notas")

#Comprbar que el archivo existe
if not carpeta.exists:
    print("La archivo NO existe.")
else:
    print("El archivo SI existe")