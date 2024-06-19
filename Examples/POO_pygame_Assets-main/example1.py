# Pygame demo 2 - una imagen, clic y movimiento en diagonal
# 1 - Importar paquetes
import pygame
from pygame.locals import *
import sys

# 2 - Definir constantes
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 200

# 3 - Inicializar el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Cargar activos: imagen(es), sonido(s), etc.
ballImage = pygame.image.load('images/ball.png')

# 5 - Inicializar variables
ballX = 0  # Comenzar en la esquina superior izquierda
ballY = 0
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

# Incremento para el movimiento en diagonal
moveX = 100
moveY = 100

# 6 - Bucle infinito
while True:
    # 7 - Comprobar y manejar eventos
    for event in pygame.event.get():
        # ¿Se hizo clic en el botón de cierre? Salir de pygame y terminar el programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Verificar si el usuario hizo clic
        if event.type == pygame.MOUSEBUTTONUP:
            # Verificar si el clic fue dentro del rectángulo de la bola
            if ballRect.collidepoint(event.pos):
                # Mover la bola en una línea diagonal
                ballX=  ballX + moveX
                ballY = ballY + moveY

                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    # 8 - Limpiar la ventana
    window.fill(BLACK)

    # 9 - Dibujar todos los elementos de la ventana
    # Dibujar la bola en la ubicación actual
    window.blit(ballImage, (ballX, ballY))

    # 10 - Actualizar la ventana
    pygame.display.update()

    # 11 - Reducir la velocidad un poco
    clock.tick(FRAMES_PER_SECOND)
