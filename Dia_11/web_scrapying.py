import bs4
import requests

#Manera de interceptar metodos GET de una pagina
resultado = requests.get("https://assetstore.unity.com")
soap = bs4.BeautifulSoup(resultado.text,'lxml')

#Seleccionar el tipo de etiqueta HTML que deseamos extraer
imagenes = soap.select('img')
"""
Para extraer aspectos mas especificos del HTML, podemos utilizar los selectores de grupo CSS
# -> ID
. -> Clase
Y otros mas que se utilizan normalmente en CSS para capturar elementos especificos
"""
#print(soap.select('div span')) #En este caso capturaremos todos los span que sean hijos de una <div>
print(soap.select('.px-4')) #Oh aqui capturaremos todos los elemetos o etiquetas con la clase "px-4"

print(soap.select('div span')[0].getText()) #Obtenemos solamente el texto del primer elemento del Array

imagen_asset_store = requests.get(imagenes[0])

#Guardar una imagen en el ordenador
asset_store = open('asset_store.svg','wb')
asset_store.write(imagen_asset_store.content)
asset_store.close()