from PathLib import Path
from os import system
#Si al crear un objeto Path() le pasamos mas parametros creara un directorio en lugar de un solo archivo
guia = Path("contraseinas","contaseinas.txt")

#Podemos saber cual es el archivo raiz que toma la biblioteca
guia = Path(Path.home(),"OneDrive","Escritorio")
#Buscara incluso en las carpetas hijas del directorio, todos los archivos .txt
for txt in Path(guia).glob("**/*.txt"):
    print(txt)
#Limpiar la consola
system('cls')