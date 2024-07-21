from pathlib import Path
class Menu:
    @staticmethod
    def main():
        print("""
1. Leer Receta
2. Crear Receta
3. Editar Receta
4. Eliminar Receta
5. Eliminar Categoria
6. Crear Categoria
7. Terminar programa
              """)
        respuesta = input("Ingrese el numero de lo que desea realizar: ")
        return int(respuesta)
    
    @staticmethod
    def categorias(categorias):
        print("\t|Categorias almacendas|")
        for index,categoria in enumerate(categorias):
            print(f"{index+1}. {categoria.name}")
        print(f"{len(categorias)+1}. Regresar")
        respuesta = input("Ingrese el numero de la categoria que desea acceder: ")
        return int(respuesta)-1
    
    @staticmethod
    def recetas(categoria):
        print(f"\t|Recetas Almacenadas en '{categoria.name}'|")
        recetasTxt = list(Path(categoria).glob('*.txt'))

        for index,receta in enumerate(recetasTxt):
            print(f"{index+1}. {receta.name}")
        print(f"{len(recetasTxt)+1}. Regresar")
        receta = input("Ingrese el numero de la categoria que deseas acceder: ")
        return int(receta)-1,recetasTxt
