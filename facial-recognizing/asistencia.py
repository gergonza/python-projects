from cv2 import cv2
from datetime import datetime

import face_recognition as fr
import os
import numpy


# Codificar imágenes
def codificar(imagenes):
    # Crea una lista nueva
    lista_codificada = []

    # Pasar todas las imágenes a RGB
    for imagen_lista in imagenes:
        imagen_lista = cv2.cvtColor(imagen_lista, cv2.COLOR_BGR2RGB)

        # Codificar
        codificado = fr.face_encodings(imagen_lista)[0]

        # Agregar a la lista
        lista_codificada.append(codificado)

    # Devolver lista codificada
    return lista_codificada


# Registrar los ingresos
def registrar_ingresos(persona):
    file = open('registro.csv', 'r+')
    lista_datos = file.readlines()
    nombres_registro = []

    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        file.writelines(f'\n{persona}, {string_ahora}')


# Crear Base de Datos
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)

lista_empleados_codificada = codificar(mis_imagenes)

# Tomar imagen de una cámara web
captura = cv2.VideoCapture(0, cv2.CAP_ANY)

# Se agrega un tiempo para realizar la captura (esto aplica en Mac porque de lo contrario no captura la pantalla)
tiempo_captura = 0
exito = True
imagen = ''

while tiempo_captura < 15:
    tiempo_captura += 1
    exito, imagen = captura.read()
    cv2.imshow("Capturando", imagen)

if not exito:
    print('No se ha podido tomar la captura')
else:
    # Reconocer cara en captura
    cara_captura = fr.face_locations(imagen)

    # Codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # Buscar coincidencias con la lista de imágenes
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        indice_coincidencia = numpy.argmin(distancias)

        # Mostrar coincidencias
        if distancias[indice_coincidencia] > 0.6:
            print('No coincide con ninguno de nuestros empleados')
        else:
            # Buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]

            # Ubicar la cara en imagen captura
            y1, x2, y2, x1 = caraubic

            # Rectángulo para cara
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Rectángulo para Texto
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            # Registrar ingreso
            registrar_ingresos(nombre)

            # Mostrar la imagen obtenida
            cv2.imshow('Imagen Web', imagen)

            # Mantener ventana abierta
            cv2.waitKey(0)
