from menu import Menu
from pathlib import Path
import os
from receta import Receta
import keyboard
import shutil

directorioRaiz = Path('c:\\Users\\user\\OneDrive\\Escritorio\\SCP_txt\\Recetario')
#Creara una ruta relativa desde el directorio que el programa se encuentra hasta el directorio pasado (raiz)
rutaRelativa = os.path.relpath(directorioRaiz, start=os.getcwd())
rutaRelativa = Path(rutaRelativa)

"""
TODO: Agregar una categoria y eliminarlas tambien y Eliminar una receta
"""

def main():
    print("Bienvenido a tu recetario! Que vamos hacer hoy?")
    respuesta = 0
    while respuesta != 7:
        respuesta = Menu.main()
        realizarAccion(respuesta)

def realizarAccion(respuesta):
    match(respuesta):
        case 1:
            leerReceta()
        case 2:
            categoria = obtenerCategoria()
            crearReceta(categoria)
        case 3:
            editarReceta()
        case 4:
            eliminarReceta()
        case 5:
            eliminarCategoria()
        case 6:
            crearCategoria()
        case 7:
            print("Gracias por usar el programa :)")
        case _:
            print("Opcion invalida. Intente de nuevo\n")

def leerReceta():
    rutaCategoria = obtenerCategoria()
    receta,recetas_txt = Menu.recetas(rutaCategoria)
    
    if receta == len(recetas_txt):
        main()
    elif len(recetas_txt) == 0:
        respuesta = input("No tienes recetas creadas aun. Deseas crear una? (y/n)")
        if respuesta.lower() == 'y':
            crearReceta(rutaCategoria)
        else:
            return
    os.system('cls')
    receta = recetas_txt[receta].resolve()
    receta = open(receta,'r',encoding='utf-8')
    print(receta.read())
    input("\nPresione Enter para salir del modo lectura")

def crearReceta(categoria):
    tituloReceta = input("Ingrese el titulo de la nueva receta: ")

    nuevaReceta = Receta(tituloReceta,texto="",ruta="")
    nuevaReceta.guardar(categoria)

def eliminarReceta():
    categoria = obtenerCategoria()
    receta,recetas_txt = Menu.recetas(categoria)

    receta = recetas_txt[receta].resolve()
    receta = Receta(ruta=receta,titulo=receta.name,texto=receta.read_text())
    receta.eliminar()

def eliminarCategoria():
    categoria = obtenerCategoria()
    categoria = Path(categoria).resolve()
    respuesta = input("Estas seguro que deseas eliminar esta categoria? (y/n)")
    if respuesta.lower() == 'y' and categoria.is_dir:
        shutil.rmtree(categoria)
        print("Categoria eliminada correctamente")

def crearCategoria():
    nombre_categoria = input("Ingrese el nombre de la nueva categoria: ")
    categoria = Path(rutaRelativa)/nombre_categoria
    categoria.mkdir(parents=True,exist_ok=True)
    print(f"La categoria '{nombre_categoria}' fue creada exitosamente!")

def editarReceta():
    categoria = obtenerCategoria()
    receta,recetas_txt = Menu.recetas(categoria)

    receta = recetas_txt[receta].resolve()
    receta = open(receta,'a',encoding='utf-8')

    textoReceta = []
    os.system('cls')
    print("Presiona F1 al iniciar una linea para salir del modo edicion")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'f1':
                break
            else:
                linea = input()
                textoReceta.append(f"\n{linea}")
    receta.writelines(textoReceta)
    receta.close()
    print("Cambios guardados")
    
def mostrarCategorias(categorias):
    if len(categorias) == 0:
        respuesta = input("No tienes ninguna categoria creada. Deseas crear una? (y/n): ")
        if respuesta.lower() == 'y':
            crearCategoria()
        else: main()
    else:
        return Menu.categorias(categorias)
        
def obtenerCategoria():
    categorias = [entrada for entrada in rutaRelativa.iterdir() if entrada.is_dir()]
    if len(categorias) == 0 or categorias == None:
        print("No tiene categorias registradas\n")
        main()
    categoria = mostrarCategorias(categorias)
    try:
        if categoria == len(categorias):
            main()
        categoria = Path(rutaRelativa)/categorias[categoria].name
        return categoria
    except IndexError:
        print("Valor no reconocido. Categoria Inexistente\n")
        main()
main()