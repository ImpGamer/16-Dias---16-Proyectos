fraseUsuario = input("Ingrese una frase, palabra o cualquier texto: ")
caracteres = []

for i in range(3):
    caracteres.append(input("Ingrese un caracter: "))

print(f"La {caracteres[0]} aparece en la frase: {fraseUsuario.count(caracteres[0])} veces")
print(f"La {caracteres[1]} aparece en la frase: {fraseUsuario.count(caracteres[1])} veces")
print(f"La {caracteres[2]} aparece en la frase: {fraseUsuario.count(caracteres[2])} veces")

palabrasTotal = fraseUsuario.split()
print(f"La frase posee un total de: {len(palabrasTotal)} palabras")

print(f"Primera letra del texto: {fraseUsuario[0]}\nUltima letra del texto: {fraseUsuario[-1]}")
print(f"Texto inverso: {fraseUsuario[::-1]}")
palabra = "python"

print(f"La frase contiene 'python'? {palabra in fraseUsuario}")