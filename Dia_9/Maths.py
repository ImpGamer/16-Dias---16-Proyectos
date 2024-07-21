import math
import re

resultado = math.log(10*200,5)

clave = input("Clave: ")
patron = r'\D{1}\w{7}'

def validar_correo(correo):
    # Expresión regular para validar el correo electrónico
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[cC][oO][mM]$'
    
    if re.match(regex, correo):
        return True
    else:
        return False
    
print(validar_correo("miCorreo@gmail.com"))