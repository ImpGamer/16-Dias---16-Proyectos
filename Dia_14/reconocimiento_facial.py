import cv2
import face_recognition as fr

# Cargar imágenes
foto_control = fr.load_image_file('./Dia_14/FotoA.jpg')
foto_comparador = fr.load_image_file('./Dia_14/FotoB.jpg')

# Cambio de composición de color de BGR a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_comparador = cv2.cvtColor(foto_comparador, cv2.COLOR_BGR2RGB)

try:
# Localizar caras de la imagen
    #Da la posicion del rostro(y1,x2,y2,x1)
    posicion_cara_A = fr.face_locations(foto_control)[0]
    #Codificacion de la imagen a un entorno mas computable (asbtraccion del valor de los bytes)
    cara_codificada_A = fr.face_encodings(foto_control)[0]
    """
    Creacion de un rectangulo que marque la posicion donde se encuentra
    el rostro, pasando los siguiente parametros:
    1. Imagen donde se dibujara el rectangulo
    2. Posicion (x,y) superior izquierda inicial de la deteccion de rostro
    3. Posicion (x,y) inferior derecho final de la deteccion del rostro
    4. Espectro (BGR) con que color se dibujara el recuadro
    5. Grosor del rectangulo
    """
    cv2.rectangle(foto_control,
                  (posicion_cara_A[3],posicion_cara_A[0]),
                  (posicion_cara_A[1],posicion_cara_A[2]),
                  (255,0,0),2)
    
    posicion_cara_B = fr.face_locations(foto_comparador)[0]
    cara_codificada_B = fr.face_encodings(foto_comparador)[0]
    cv2.rectangle(foto_comparador,
                  (posicion_cara_B[3],posicion_cara_B[0]),
                  (posicion_cara_B[1],posicion_cara_B[2]),
                  (255,0,0),2)
    
    #Una lista de rostros debe comparar contra una sola
    resultado = fr.compare_faces([cara_codificada_A],cara_codificada_B,1)
    print(resultado)

    #Establecer una distancia de tolrencia (entre mayor sea mayor tolerancia de no coincidencia)
    distancia = fr.face_distance([cara_codificada_A],cara_codificada_B)
    print(distancia)

    color = (0,255,0) if resultado[0] else (0,0,255)

    #Mostrar resultados de distancia y coincidencia en la imagen
    cv2.putText(foto_comparador,f"{'Hay coincidencias' if resultado[0] == True else 'No hay coincidencias'} {distancia.round(2)}"
                ,(50,50),cv2.FONT_HERSHEY_COMPLEX,1
                ,color,2)
    
    # Mostrar imágenes
    cv2.imshow('Foto Control', foto_control)
    cv2.imshow('Foto Comparadora', foto_comparador)

    # Mantener el programa abierto
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except IndexError:
    print("No se encontraron caras en la imagen de control.")
except RuntimeError as e:
    print(f"Error en la detección de caras: {e}")
