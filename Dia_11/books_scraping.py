"""
En este modulo veremos de una pagina ficticia de libreria, veremos como extraer
libros con atributos especificos, en este caso, aquellos que tengan 4 o 5 estrellas de
calificacion.
"""
import bs4
import requests
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

titulos_alto_valor = []

#iterar paginas
for page in range(1,50):
    resultado = requests.get(url_base.format(page))
    soap = bs4.BeautifulSoup(resultado.text,'lxml')
    libros = soap.select('.product_pod') #Extraer los datos de cada libro
    for libro in libros:
        #Validar si el libro actual, posee 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) !=0:
            titulo_libro = libro.select('a')[1]['title'] #Como nos trae varias etiquetas <a> nosotros queremos acceder al que se encuentra en la posicion 1 del arreglo
            titulos_alto_valor.append(titulo_libro)

print("Libros con 4 o 5 estrellas de Calificacion: ")
for titulo in titulos_alto_valor:
    print(titulo)
