from pygame import mixer

import io
import math
import pygame
import random

# Iniciar Pygame
pygame.init()

# Establecer pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título
pygame.display.set_caption('Invasión Espacial')

# Ícono
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

# Fondo de Pantalla
fondo = pygame.image.load('fondo.jpg')

# Agregar Música
mixer.music.load('musicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Jugador
img_jugador = pygame.image.load('cohete.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

# Crear los enemigos
for individuo in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

# Bala
balas = []
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False


# Transformar Nombre de Fuente de String a Bytes
def fuente_bytes(parametro):
    # Abre el archivo TTF en modo lectura binaria
    with open(parametro, 'rb') as f:
        # Lee todos los bytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
    # Crea un objeto BytesIO a partir de los bytes del archivo TTF
    return io.BytesIO(ttf_bytes)


# Puntaje
puntaje = 0
fuente_como_bytes = fuente_bytes('fastest.ttf')
fuente = pygame.font.Font(fuente_como_bytes, 32)
texto_x = 10
texto_y = 10

# Texto final del juego
fuente_final = pygame.font.Font(fuente_como_bytes, 40)


# Mostrar puntaje en pantalla
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Coloca el jugador en la pantalla
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Coloca el enemigo en la pantalla
def enemigo(x, y, n):
    pantalla.blit(img_enemigo[n], (x, y))


# Coloca la bala en la pantalla
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Verifica si hay una colisión entre los objetos
def hay_colision(x1, y1, x2, y2):
    operacion1 = math.pow(x2 - x1, 2)
    operacion2 = math.pow(y2 - y1, 2)
    distancia = math.sqrt(operacion1 + operacion2)
    if distancia < 27:
        return True
    else:
        return False


# Dispara los eventos para el final de juego
def texto_final():
    mi_fuente_final = fuente_final.render('JUEGO TERMINADO', True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (120, 200))


# Loop del juego
se_ejecuta = True

while se_ejecuta:

    # Poniendo el fondo en la pantalla
    pantalla.blit(fondo, (0, 0))

    # Controlar el movimiento del jugador
    # Dentro de la pantalla se manejan eventos
    for evento in pygame.event.get():

        # Evento de presionar el botón X (Cerrar Ventana)
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento al pulsar una tecla
        if evento.type == pygame.KEYDOWN:
            # Flecha izquierda
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            # Flecha derecha
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            # Presionar espacio
            if evento.key == pygame.K_SPACE:
                # Sonido al disparar la bala
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.set_volume(0.3)
                sonido_bala.play()
                # Sólo aplica cuando la bala no ha sido disparada
                if not bala_visible:
                    # La bala va a mantener su posición X al ser disparada, no se va a mover como el jugador
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # Evento al soltar una tecla (flecha derecha o izquierda)
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Se modifica la posición del jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro de bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x > 736:
        jugador_x = 736

    # Este código se realiza por cada enemigo
    for individuo in range(cantidad_enemigos):
        # Fin del juego
        if enemigo_y[individuo] > 500:
            for nave in range(cantidad_enemigos):
                enemigo_y[nave] = 1000
            texto_final()
            break

        # Se modifica la posición del enemigo
        enemigo_x[individuo] += enemigo_x_cambio[individuo]

        # Mantener dentro de bordes al enemigo
        if enemigo_x[individuo] <= 0:
            enemigo_x_cambio[individuo] = 1
            enemigo_y[individuo] += enemigo_y_cambio[individuo]
        elif enemigo_x[individuo] > 736:
            enemigo_x_cambio[individuo] = -1
            enemigo_y[individuo] += enemigo_y_cambio[individuo]

        # Detectar colisión
        colision = hay_colision(enemigo_x[individuo], enemigo_y[individuo], bala_x, bala_y)
        if colision:
            # Sonido al golpear al enemigo con la bala
            sonido_colision = mixer.Sound('golpe.mp3')
            sonido_colision.set_volume(0.3)
            sonido_colision.play()
            # Se crea una nueva bala
            bala_y = 500
            bala_visible = False
            # Aumento de puntaje
            puntaje += 1
            # Se crea un nuevo enemigo
            enemigo_x[individuo] = random.randint(0, 736)
            enemigo_y[individuo] = random.randint(50, 200)

        # El enemigo se mueve
        enemigo(enemigo_x[individuo], enemigo_y[individuo], individuo)

    # La bala se mueve
    # Si la bala llega al final de la pantalla, el jugador podrá disparar la bala de nuevo
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # El jugador se mueve
    jugador(jugador_x, jugador_y)

    # Imprimir puntaje
    mostrar_puntaje(texto_x, texto_y)

    # Actualizar los cambios en pantalla
    pygame.display.update()
