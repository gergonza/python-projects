from tkinter import filedialog, Frame, Label, Tk, LabelFrame, IntVar, Checkbutton, StringVar, Entry, Button, Text, messagebox
from tkinter.constants import END, NORMAL, DISABLED, FLAT, TOP, LEFT, BOTTOM, RIGHT, W

import random
import datetime

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postre = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton_calculadora(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar_calculadora():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado_calculadora():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    # Comidas
    x = 0
    for _ in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            cuadros_comida[x].delete(0, END)
            texto_comida[x].set('0')
        x += 1

    # Bebidas
    x = 0
    for _ in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            cuadros_bebida[x].delete(0, END)
            texto_bebida[x].set('0')
        x += 1

    # Postre
    x = 0
    for _ in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            cuadros_postre[x].delete(0, END)
            texto_postre[x].set('0')
        x += 1


def total():
    # Comida
    subtotal_comida = 0
    p = 0
    for cantidad in texto_comida:
        subtotal_comida += (float(cantidad.get()) * precios_comida[p])
        p += 1

    # Bebida
    subtotal_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebida += (float(cantidad.get()) * precios_bebida[p])
        p += 1

    # Postre
    subtotal_postre = 0
    p = 0
    for cantidad in texto_postre:
        subtotal_postre += (float(cantidad.get()) * precios_postre[p])
        p += 1

    # Cálculos
    sub_total = subtotal_comida + subtotal_bebida + subtotal_postre
    impuestos = sub_total * 0.07
    total_pagar = sub_total + impuestos

    # Asignación para Campos
    var_costo_comida.set(f'${round(subtotal_comida, 2)}')
    var_costo_bebida.set(f'${round(subtotal_bebida, 2)}')
    var_costo_postre.set(f'${round(subtotal_postre, 2)}')
    var_subtotal.set(f'${round(sub_total, 2)}')
    var_impuesto.set(f'${round(impuestos, 2)}')
    var_total.set(f'${round(total_pagar, 2)}')


def recibo():
    # Inicialización
    texto_recibo.delete(1.0, END)

    numero_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}:{fecha.second}'

    # Encabezado
    texto_recibo.insert(END, f'Datos:\t{numero_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    # Comida
    x = 0
    for comida_elegida in texto_comida:
        if comida_elegida.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_comidas[x]}\t\t{comida_elegida.get()}\t$ {int(comida_elegida.get()) * precios_comida[x]}\n')
            x += 1

    # Bebida
    x = 0
    for bebida_elegida in texto_bebida:
        if bebida_elegida.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_bebidas[x]}\t\t{bebida_elegida.get()}\t$ {int(bebida_elegida.get()) * precios_bebida[x]}\n')
            x += 1

    # Postre
    x = 0
    for postre_elegido in texto_postre:
        if postre_elegido.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_postres[x]}\t\t{postre_elegido.get()}\t$ {int(postre_elegido.get()) * precios_postre[x]}\n')
            x += 1

    # Pie de Página
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo del Postre: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto\n')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo ha sido guardado')


def resetear():
    # Borro recibo
    texto_recibo.delete(0.1, END)

    # Comida
    for texto in texto_comida:
        texto.set('0')
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for variable in variables_comida:
        variable.set(0)

    # Bebida
    for texto in texto_bebida:
        texto.set('0')
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for variable in variables_bebida:
        variable.set(0)

    # Postre
    for texto in texto_postre:
        texto.set('0')
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)
    for variable in variables_postre:
        variable.set(0)

    # Cálculos
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


# Iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

# Evitar maximizar
aplicacion.resizable(False, False)

# Título de la Ventana
aplicacion.title('Mi Restaurante - Sistema de Facturación')

# Color de Fondo de la Pantalla
aplicacion.config(bg='burlywood')

# Panel Superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Título del panel superior
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='azure4', font=('Dosis', 58), bg='burlywood',
                        width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel Izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel de Costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=90)
panel_costos.pack(side=BOTTOM)

# Panel de Comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel de Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel de Postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel Derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel Calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack(side=TOP)

# Panel de Recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack(side=TOP)

# Panel de los Botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack(side=TOP)

# Lista de Productos
lista_comidas = ['Pollo', 'Cordero', 'Salmón', 'Merluza', 'Kebab', 'Pizza Margherita', 'Pizza Napoletana',
                 'Pizza 4 Quesos']
lista_bebidas = ['Agua', 'Soda', 'Jugo', 'Coca Cola', 'Vino Blanco', 'Vino Tinto', 'Cerveza Heineken', 'Cerveza Mahou']
lista_postres = ['Helado', 'Fruta', 'Brownie', 'Flan', 'Mousse', 'Torta', 'Gelatina', 'Quesillo']

# CheckButtons de Comidas
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # Crear los checkbuttons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida_button = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0,
                                variable=variables_comida[contador], command=revisar_check)
    comida_button.grid(row=contador, column=0, sticky=W)

    # Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=+1)

    # Aumentar el contador
    contador += 1

# CheckButtons de Bebidas
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    # Crear los checkbuttons
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida_button = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0,
                                variable=variables_bebida[contador], command=revisar_check)
    bebida_button.grid(row=contador, column=0, sticky=W)

    # Crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=+1)

    # Aumentar el contador
    contador += 1

# CheckButtons de Postres
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    # Crear los checkbuttons
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre_button = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0,
                                variable=variables_postre[contador], command=revisar_check)
    postre_button.grid(row=contador, column=0, sticky=W)

    # Crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=+1)

    # Aumentar el contador
    contador += 1

# Establecer Etiquetas de Costo y Campos de Entrada
# Costo de Comida
var_costo_comida = StringVar()

etiqueta_costo_comida = Label(panel_costos, text='Costo de Comida', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# Costo de Bebida
var_costo_bebida = StringVar()

etiqueta_costo_bebida = Label(panel_costos, text='Costo de Bebida', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# Costo de Postre
var_costo_postre = StringVar()

etiqueta_costo_postre = Label(panel_costos, text='Costo de Postre', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

# Subtotal
var_subtotal = StringVar()

etiqueta_subtotal = Label(panel_costos, text='Subtotal', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# Impuestos
var_impuesto = StringVar()

etiqueta_impuesto = Label(panel_costos, text='Impuestos', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                       textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

# Total
var_total = StringVar()

etiqueta_total = Label(panel_costos, text='Total', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# Botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton_objeto = Button(panel_botones, text=boton.title(), font=('Dosis', 14, 'bold'), fg='white', bg='azure4', bd=1,
                          width=9)
    botones_creados.append(boton_objeto)
    boton_objeto.grid(row=0, column=columnas)
    columnas += 1

botones_creados[0].config(command=lambda: total())
botones_creados[1].config(command=lambda: recibo())
botones_creados[2].config(command=lambda: guardar())
botones_creados[3].config(command=lambda: resetear())

# Recibo
texto_recibo = Text(panel_recibo, font=('Dosis', 12, 'bold'), bd=1, width=42, height=10)
texto_recibo.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora, font=('Dosis', 16, 'bold'), width=32, bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', 'CE', 'Borrar', '0', '/']
botones_guardados = []
fila = 1
columna = 0

for boton in botones_calculadora:
    boton_objeto = Button(panel_calculadora, text=boton.title(), font=('Dosis', 16, 'bold'), fg='white', bg='azure4',
                          bd=1, width=8)
    boton_objeto.grid(row=fila, column=columna)
    botones_guardados.append(boton_objeto)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click_boton_calculadora('7'))
botones_guardados[1].config(command=lambda: click_boton_calculadora('8'))
botones_guardados[2].config(command=lambda: click_boton_calculadora('9'))
botones_guardados[3].config(command=lambda: click_boton_calculadora('+'))
botones_guardados[4].config(command=lambda: click_boton_calculadora('4'))
botones_guardados[5].config(command=lambda: click_boton_calculadora('5'))
botones_guardados[6].config(command=lambda: click_boton_calculadora('6'))
botones_guardados[7].config(command=lambda: click_boton_calculadora('-'))
botones_guardados[8].config(command=lambda: click_boton_calculadora('1'))
botones_guardados[9].config(command=lambda: click_boton_calculadora('2'))
botones_guardados[10].config(command=lambda: click_boton_calculadora('3'))
botones_guardados[11].config(command=lambda: click_boton_calculadora('*'))
botones_guardados[12].config(command=lambda: obtener_resultado_calculadora())
botones_guardados[13].config(command=lambda: borrar_calculadora())
botones_guardados[14].config(command=lambda: click_boton_calculadora('0'))
botones_guardados[15].config(command=lambda: click_boton_calculadora('/'))

# Evitar que la pantalla se cierre
aplicacion.mainloop()
