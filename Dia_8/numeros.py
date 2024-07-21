def crearTurno_perfumeria():
    for n in range(1,10000):
        yield f"P- {n}"

def crearTurno_Farmacia():
    for n in range(1,10000):
        yield f"F- {n}"

def crearTurno_cosmetica():
    for n in range(1,10000):
        yield f"C- {n}"


p = crearTurno_perfumeria()
f = crearTurno_Farmacia()
c = crearTurno_cosmetica()


def decorador(rubro):
    print("\n"+"*"*23)
    print("Su turno es: ")
    match rubro:
        case 'P':
            print(next(p))
        case 'F':
            print(next(f))
        case 'C':
            print(next(c))
        case _:
            print("Error. Opcion no valida.")