from tkinter import *
import random
import datetime
from tkinter import filedialog,messagebox

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_button(numero):
    global operador
    operador = operador+numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)

def reset():
    texto_recibo.delete(1.0,END)
    for texto in texto_comida:
        texto.set(0)
    for texto in texto_bebidas:
        texto.set(0)
    for texto in texto_postres:
        texto.set(0)

    for cuadro_comida, cuadro_bebida, cuadro_postre in zip(cuadros_comida, cuadros_bebidas, cuadros_postres):
        cuadro_comida.config(state=DISABLED)
        cuadro_bebida.config(state=DISABLED)
        cuadro_postre.config(state=DISABLED)

    for comida,bebida,postre in zip(checkButtons_comida,checkButtons_bebidas,checkButtons_postres):
        comida.set(False)
        bebida.set(False)
        postre.set(False)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_impuesto.set('')
    var_subtotal.set('')

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador = ''

def total():
    sub_total_comida =0
    index = 0
    for cantidad in texto_comida:
        sub_total_comida += float((cantidad.get()*precios_comida[index]))
        index+=1
    
    sub_total_bebidas = 0
    index = 0
    for cantidad in texto_bebidas:
        sub_total_bebidas += float((cantidad.get()*precios_bebida[index]))
        index+=1

    sub_total_postres = 0
    index = 0
    for cantidad in texto_postres:
        sub_total_postres += float((cantidad.get()*precios_postres[index]))
        index+=1
    
    var_costo_comida.set(sub_total_comida)
    var_costo_bebida.set(sub_total_bebidas)
    var_costo_postre.set(sub_total_postres)
    var_subtotal.set(round(sub_total_comida+sub_total_postres+sub_total_bebidas))
    impuestos = round(float(var_subtotal.get()) * 0.07,2)
    var_impuesto.set(str(impuestos))

def recibo():
    texto_recibo.delete(1.0,END)
    num_recibo = f'N# - {random.randint(1,9999)}'
    fecha = datetime.datetime.now()
    fecha = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END,f'{num_recibo}\tFecha:{fecha}\n')
    texto_recibo.insert(END,f'*'*50+'\n')
    texto_recibo.insert(END,'Items\t\tCant.\tCosto Total\n')
    texto_recibo.insert(END,f'*'*50+'\n')
    costo_total = 0
    x=0
    for comida in texto_comida:
        if comida.get() != 0:
            costo_total += round(comida.get()*precios_comida[x],2)
            texto_recibo.insert(END,f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                f'${round(comida.get()*precios_comida[x],2)}\n')
        x+=1

    x=0
    for postre in texto_postres:
        if postre.get() != 0:
            costo_total += round(postre.get()*precios_postres[x],2)
            texto_recibo.insert(END,f'{lista_postres[x]}\t\t{postre.get()}\t'
                                f'${round(postre.get()*precios_postres[x],2)}\n')
        x+=1
        x=0
    for bebida in texto_bebidas:
        if bebida.get() != 0:
            costo_total += round(bebida.get()*precios_bebida[x],2)
            texto_recibo.insert(END,f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                f'${round(bebida.get()*precios_bebida[x],2)}\n')
        x+=1
    
    texto_recibo.insert(END,f'\nCosto Total:\t\t${round(costo_total,2)}')

def guardar():
    info_recibo = texto_recibo.get(1.0,END)
    #Abre una ventana emergente al usuario donde desea guardar su archivo
    archivo = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Archivo guardado","El recibo se a guardado correctamente")


#Cada vez que se detecte un evento de click sobre un checkbutton se ejecutara esta funcion
#Buscando todos aquellos que tengan valores verdaderos y poniendolos disponibles
def revisar_check():
    x=0
    for c in cuadros_comida:
        if checkButtons_comida[x].get() == True:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == 0:
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set(0)
        x+=1
    x=0
    for c in cuadros_bebidas:
        if checkButtons_bebidas[x].get() == True:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == 0:
                cuadros_bebidas[x].delete(0,END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set(0)
        x+=1
    x=0
    for c in cuadros_postres:
        if checkButtons_postres[x].get() == True:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == 0:
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set(0)
        x+=1

#iniciar la aplicacion
aplicacion = Tk()

aplicacion.geometry('1280x630+120+100')
#evitar redimensionar la ventana
aplicacion.resizable(0,0)
aplicacion.title("Sistema de Facturacion - Restaurante")
aplicacion.config(bg='burlywood')

panel_superior = Frame(aplicacion,bd=2,relief=FLAT)
panel_superior.pack(side=TOP)

etiqueta_titulo = Label(panel_superior,text="Sistema de Facturacion",fg='azure4',font=('Dosis',50)
                        ,bg='burlywood',width=27)
etiqueta_titulo.grid(row=0,column=0)

#Panel izquierdo
panel_izquierdo = Frame(aplicacion,bd=2,relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#Panel de costos (abajo en panel izquierdo)
panel_costos = Frame(panel_izquierdo,bd=1,relief=FLAT,bg='azure4')
panel_costos.pack(side=BOTTOM)

#Panel comidas
panel_comidas = LabelFrame(panel_izquierdo,text="Comidas",font=('Dosis',19,'bold'),
                           bd=1,relief=FLAT,fg='azure4')
panel_comidas.pack(side=LEFT)

#Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo,text="Bebidas",font=('Dosis',19,'bold'),
                           bd=1,relief=FLAT,fg='azure4')
panel_bebidas.pack(side=LEFT)

#Panel postres
panel_postres = LabelFrame(panel_izquierdo,text="Postres",font=('Dosis',19,'bold'),
                           bd=1,relief=FLAT,fg='azure4')
panel_postres.pack(side=LEFT)

panel_derecho = Frame(aplicacion,bd=2,relief=FLAT)
panel_derecho.pack(side=RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecho,bd=1,relief=FLAT,bg='burlywood')
panel_calculadora.pack() #Por defecto se coloca hasta arriba del frame

panel_recibo = Frame(panel_derecho,bd=1,relief=FLAT,bg='burlywood')
panel_recibo.pack()

panel_botones = Frame(panel_derecho,bd=1,relief=FLAT,bg='burlywood')
panel_botones.pack()

lista_comidas = ['Pollo','Pescado','Pizza Pepperonni','Spaguetti','Ensalada','Sandwich','Kebab']
lista_bebidas = ['Agua','Vino','Cerveza','Coca Cola','Jugo Manzana','Naranjada','Limonada']
lista_postres = ['Pastel','Helado','Fruta','Brownies','Flan','Chocolate','Pay de Limon']

checkButtons_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    #Crear checkbuttons
    checkButtons_comida.append('')
    checkButtons_comida[contador] = BooleanVar()
    comida = Checkbutton(panel_comidas,text=comida.title(),font=('Dosis',18,'bold'),
                         onvalue=True,offvalue=False,variable=checkButtons_comida[contador]
                         ,command=revisar_check)
    comida.grid(row=contador,column=0,sticky=W)

    #Crear inputs de cada comida
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = IntVar()
    texto_comida[contador].set(0)
    cuadros_comida[contador] = Entry(panel_comidas,font=('Dosis',17,'bold'),bd=1,width=6
                                     ,state=DISABLED,textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,column=1)

    contador+=1

checkButtons_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for bebida in lista_bebidas:
    checkButtons_bebidas.append('')
    checkButtons_bebidas[contador] = BooleanVar()
    bebida = Checkbutton(panel_bebidas,text=bebida.title(),font=('Dosis',18,'bold'),
                         onvalue=True,offvalue=False,variable=checkButtons_bebidas[contador]
                         ,command=revisar_check)
    bebida.grid(row=contador,column=0,sticky=W)

    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = IntVar()
    texto_bebidas[contador].set(0)
    cuadros_bebidas[contador] = Entry(panel_bebidas,font=('Dosis',17,'bold'),bd=1,width=6
                                     ,state=DISABLED,textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador,column=1)
    contador+=1

checkButtons_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:

    checkButtons_postres.append('')
    checkButtons_postres[contador] = BooleanVar()
    postre = Checkbutton(panel_postres,text=postre.title(),font=('Dosis',18,'bold'),
                         onvalue=True,offvalue=False,variable=checkButtons_postres[contador]
                         ,command=revisar_check)
    postre.grid(row=contador,column=0,sticky=W)

    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = IntVar()
    texto_postres[contador].set(0)
    cuadros_postres[contador] = Entry(panel_postres,font=('Dosis',17,'bold'),bd=1,width=6
                                     ,state=DISABLED,textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,column=1)
    contador+=1

var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

etiqueta_costo_comida = Label(panel_costos,text="Costos Comida",font=('Dosis',12,'bold'),bg='azure4',fg='white')
etiqueta_costo_comida.grid(row=0,column=0)

text_costo_comida = Entry(panel_costos,font=('Dosis',12,'bold'),bd=1,width=10,state='readonly',textvariable=var_costo_comida)
text_costo_comida.grid(row=0,column=1)

etiqueta_costo_bebida = Label(panel_costos,text="Costos Bebida",font=('Dosis',12,'bold'),bg='azure4',fg='white')
etiqueta_costo_bebida.grid(row=0,column=2)

text_costo_bebida = Entry(panel_costos,font=('Dosis',12,'bold'),bd=1,width=10,state='readonly',textvariable=var_costo_bebida)
text_costo_bebida.grid(row=0,column=3)

etiqueta_costo_postres = Label(panel_costos,text="Costos Postres",font=('Dosis',12,'bold'),bg='azure4',fg='white')
etiqueta_costo_postres.grid(row=0,column=4)

text_costo_postres = Entry(panel_costos,font=('Dosis',12,'bold'),bd=1,width=10,state='readonly',textvariable=var_costo_postre)
text_costo_postres.grid(row=0,column=5,padx=5,pady=4)

etiqueta_impuestos = Label(panel_costos,text="Impuestos",font=('Dosis',12,'bold'),bg='azure4',fg='white')
etiqueta_impuestos.grid(row=1,column=0)

text_impuestos = Entry(panel_costos,font=('Dosis',12,'bold'),bd=1,width=10,state='readonly',textvariable=var_impuesto)
text_impuestos.grid(row=1,column=1,padx=5,pady=4)

etiqueta_subtotal = Label(panel_costos,text="Subtotal",font=('Dosis',12,'bold'),bg='azure4',fg='white')
etiqueta_subtotal.grid(row=1,column=2)

text_subtotal = Entry(panel_costos,font=('Dosis',12,'bold'),bd=1,width=10,state='readonly',textvariable=var_subtotal)
text_subtotal.grid(row=1,column=3,padx=5,pady=4)

#Creacion botones
botones = ['total','recibo','guardar','resetear']
botones_creados = []
columna = 0
for boton in botones:
    boton = Button(panel_botones,text=boton.title(),font=('Dosis',14,'bold'),fg='white',bg='azure4',bd=1,width=8)
    botones_creados.append(boton)

    boton.grid(row=0,column=columna)
    columna+=1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=reset)
#Recibo
texto_recibo = Text(panel_recibo,font=('Dosis',14,'bold'),bd=1,width=42,height=10)
texto_recibo.grid(row=0,column=0)

#Calculadora
visor_calculadora = Entry(panel_calculadora,font=('Dosis',14,'bold'),width=32,bd=1)
visor_calculadora.grid(row=0,column=0,columnspan=4)
botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','x','=','DEL','0','/']
botones_guardados = []

fila = 1
columna =0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,text=boton.title(),font=('Dosis',13,'bold'),fg='white',bg='azure4',bd=1,width=8)
    boton.grid(row=fila,column=columna)
    if columna == 3:
        fila += 1
        columna = 0
    else:
        columna+=1
    botones_guardados.append(boton)

for i in range(len(botones_calculadora)):
    botones_guardados[i].config(command=lambda valor=botones_calculadora[i]: click_button(valor))

botones_guardados[11].config(command=lambda: click_button('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)

#mantener la aplicacion corriendo sin cerrarse
aplicacion.mainloop()