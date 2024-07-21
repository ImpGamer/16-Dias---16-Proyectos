import numeros

def main():
    while True:
        print("Bienvenido! a supermercado!")
        print("""
                      [P] - Perfumeria
                      [F] - Farmacia
                      [C] - Cosmeticos
                      """)
        valor = input("Ingrese el caracter donde desea registrar turno: ")
        numeros.decorador(valor.upper())
main()