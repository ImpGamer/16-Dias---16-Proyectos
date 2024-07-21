texto = "Este texto es parte de una frase"
#upper() -> Todos los caracteres se vuelven mayusculas
#lower() -> Todos los caracteres seran minusculas
resultado = texto.lower()
print(resultado)

a = "Python"
b = "es un"
c = "gran lenguaje"
d = "de programacion!"
e = " ".join([a,b,c,d])
print(e)

print(texto.replace("e","t"))