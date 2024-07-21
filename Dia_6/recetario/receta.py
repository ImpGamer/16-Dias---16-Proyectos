from pathlib import Path
class Receta():
    def __init__(self,titulo,texto,ruta):
        self.titulo = titulo
        self.texto = texto
        self.ruta = ruta
    
    def getTitulo(self): return self.titulo
    def getTexto(self): return self.texto
    def setTexto(self,texto): self.texto = texto

    def guardar(self,directorio):
        Path(directorio).mkdir(parents=True,exist_ok=True)
        archivo = Path(directorio) / (self.titulo+".txt")
        if archivo.exists():
            respuesta = input(f"El archivo '{self.titulo}.txt' ya existe en este directorio. Deseas remplazarlo? (y/n): ")
            match respuesta.lower():
                case 'y':
                    archivoNuevo = open(archivo,'w',encoding='utf-8')
                    archivoNuevo.write(self.texto)
                    print("El contenido del archivo fue reseteado")
                case 'n':
                    print("El contenido de la receta sigue en su estado original")
                case _:
                    print("Caracter no valido.")
                    self.guardar(directorio)
        else:
            nuevaReceta = open(archivo,'w',encoding='utf-8')
            nuevaReceta.write(self.texto)
            nuevaReceta.close()
            print(f"\nLa receta '{self.titulo}.txt' se ha guardado correctamente!")

    def eliminar(self):
        archivo = Path(self.ruta)
        if archivo.exists() and archivo.is_file:
            respuesta = input(f"Estas seguro que deseas eliminar la receta '{archivo.name}'? (y/n)")
            if respuesta.lower() == 'y':
                archivo.unlink()
                print("La receta fue eliminada correctamente")