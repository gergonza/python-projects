from subprocess import call

import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar nuestro micrófono y devolver el audio como texto
def transformar_audio_en_texto():
    # Almacenar recognizer en una variable
    r = sr.Recognizer()

    # Configurar el micrófono
    with sr.Microphone() as origen:
        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzó la grabación
        print('ya puedes hablar')

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en Google
            pedido = r.recognize_google(audio, language='es-ve')

            # Prueba de que pudo ingresar
            print(f'Dijiste: {pedido}')

            # Devolver pedido
            return pedido

        # En caso de que no comprenda el audio
        except sr.UnknownValueError:
            # Prueba de que no comprendió el audio
            print('Ups, no entendí')

            return 'Sigo esperando'

        # En caso de no resolver el pedido
        except sr.RequestError:
            # Prueba de que no comprendió el audio
            print('Ups, no hay servicio')

            return 'Sigo esperando'

        # Error inesperado
        except:

            # Prueba de que no comprendió el audio
            print('Ups, algo ha salido mal')

            return 'Sigo esperando'


# Función para que el asistente pueda ser escuchado
def hablar(mensaje):
    # Se invoca al Motor para que pronuncia el mensaje solicitado
    call(["python3", "hablar.py", mensaje])


# Informar el día de la semana
def pedir_dia():
    # Crear Variable con datos de hoy
    dia = datetime.datetime.today()

    # Crea Variable para el día de Semana
    dia_semana = dia.weekday()

    # Diccionario con nombres de días
    calendario = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    hablar(f'Today is {calendario[dia_semana]}')


# Informa la hora del día
def pedir_hora():
    # Crear Variable con datos de la hora
    hora = datetime.datetime.now()

    # Crea Variable para decir la hora
    hora = f'In this moment, they are {hora.hour} hours with {hora.minute} minutes and {hora.second} seconds'

    hablar(hora)


# Función para saludo inicial
def saludo_inicial():
    # Crear variable con datos de hora
    hora = datetime.datetime.now()

    # Segun la hora, el saludo
    if hora.hour < 6 or hora.hour > 19:
        momento = 'Good evening'
    elif 6 <= hora.hour < 12:
        momento = 'Good morning'
    else:
        momento = 'Good afternoon'

    # Decir el saludo
    hablar(f'{momento}, I am Eric, your personal assistant, please tell me how I can help you')


# Función Central del Asistente
def pedir_cosas():
    # Activar saludo inicial
    saludo_inicial()

    # Variable de corte
    comenzar = True

    # Loop Central
    while comenzar:
        # Activar el micrófono y guardar el pedido
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Perfect, I am opening Youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Sure, I already do it')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Searching it in wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('en')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar(f'Wikipedia says {resultado}')
            continue
        elif 'busca en internet' in pedido:
            hablar('In this moment')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('This is I have found')
            continue
        elif 'reproducir' in pedido:
            hablar('Good idea, I already play it')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('en'))
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL', 'amazon': 'AMZN', 'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'I found, the price of the {accion} is {precio_actual}')
                continue
            except:
                hablar('Sorry, I have not found it')
                continue
        elif 'adiós' in pedido:
            hablar('I go to rest, notify me if you need something')
            break


pedir_cosas()
