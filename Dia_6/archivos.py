#Las operaciones que podemos hacer a un archivo son:
#Leer, escribir, borrar y remplazar

try:
    #Aqui extraemos los datos pero no midifcamos nada el archivo original
    mi_archivo = open("./Dia_6/prueba.txt",'r') #Se especifica que solo lo abriremos en modo lectura
    #print(mi_archivo.read())
    mi_archivo.close()

except FileNotFoundError:
    print("No se pudo encontrar el archivo")

#Modificar el archivo original abierto
try:
    """
    Hay 2 modos para escribir en un texto ('a','w')
    'a' => En este modo podremos continuar con la escritura habitual de una archivo, es decir todo el contenido que ya estaba establecido
    anteriormente seguira ahi.
    'w' => En el caso de 'w' sobreescribira todo lo que se encuentra en el archivo, es decir lo que agreguemos al archivo borrara todo lo
    antes almacenado y pondra lo insertado.
    """
    archivo = open('./Dia_6/prueba.txt','a') #"Write" es decir que escribiremos sobre el (si no existe lo crea)
    archivo.write("Soy una nueva linea!\n")

    #Escribir varias lineas (recibe una lista de strings)
    archivo.writelines(['Nueva linea','Y otra mas','Creo que ya es la ultima','Ahora si es la ultima'])
    archivo.close()

except FileExistsError:
    print("Archivo no encontrado")