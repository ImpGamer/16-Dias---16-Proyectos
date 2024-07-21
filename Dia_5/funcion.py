def invertir_palabra(palabra):
    caracteres = list(palabra)
    palabra_invertida = caracteres[::-1]
    palabra_invertida = ''.join(palabra_invertida)
    return palabra_invertida.upper()

print(invertir_palabra("Python"))