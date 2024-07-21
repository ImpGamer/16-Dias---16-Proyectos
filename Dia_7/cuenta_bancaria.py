class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido,numero_cuenta,saldo):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    
    def __str__(self):
        return f"Datos del cliente:\nNombre: {self.nombre}\nApellido: {self.apellido}\nNumero de Cuenta: {self.numero_cuenta}\nSaldo Actual {self.saldo}"
    
    def depositar(self,deposito):
        self.saldo += deposito
        print("Deposito realizado con exito\n")

    def retirar(self,retiro):
        if retiro > self.saldo:
            print("No se puede realizar el retiro. El monto deseado es mayor al saldo actual.\n")
            return
        self.saldo -= retiro
        print(f"Retirlo realizado con exito.\nSaldo actual: {self.saldo}\n")


def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    valido = False
    while not valido:
        numero_cuenta = input("Ingrese un numero cuenta: (4 numeros): ")
        if len(numero_cuenta) == 4:
            valido = True
            nuevo_cliente = Cliente(nombre,apellido,numero_cuenta,0)
            print("Cliente guardado correctamente!\n")
            return nuevo_cliente

def main():
    cliente = crear_cliente()
    opcion = 0
    while opcion != 3:
        try:
            print(f"""
Bienvenido {cliente.nombre}! a tu Banca Automatica que realizaremos el dia de hoy!
                  1. Depositar
                  2. Retirar
                  3. Salir del programa 
""")
            opcion = int(input("Presione el numero de lo que desea realizar: "))    
        except ValueError:
            print("Valor no permitido. Intentelo de nuevo")
            continue
        
        match opcion:
            case 1:
                deposito = float(input("Ingrese la cantidad que desea depositar (Se permite decimales): "))
                cliente.depositar(deposito)
                print(f"Saldo Actual: {cliente.saldo}")
            case 2:
                retiro = float(input(f"Saldo Actual: {cliente.saldo}\nIngrese la cantidad que desea retirar (Se permite decimales): "))
                cliente.retirar(retiro)
                print(f"Saldo Actual: {cliente.saldo}")
            case 3:
                print(f"Hasta luego! {cliente.nombre}")
                del cliente
            case _:
                print("Opcion no valida. Intente de nuevo")

main()