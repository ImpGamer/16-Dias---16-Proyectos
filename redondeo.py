#Funcion para redondear numeros flotantes
numFloat = 20123.4123

#En este caso me redondea la variable con un solo decimal
print(round(numFloat,1))

def suma(num1,num2):
    return num1+num2

#En este caso el numero devuelto por la funcion la redondeara con 2 digitos (si el ultimo digito es 0 lo anulara)
print(round(suma(20,40.50),2))
num = 20.40

#En el caso que no le especifiquemos cuantos decimales debera redondear, lo redondeara al numero entero mas cercano (int)
print(type(round(num)))