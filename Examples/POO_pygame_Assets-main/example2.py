# pygame demo 2 - una imagen, clic y movimiento
# 1 - Importar paquetes
import pygame
from pygame.locals import *
import sys
import random

# 2 - Definir constantes
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

# 3 - Inicializar el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Cargar activos: imagen(es), sonido(s), etc.
ballImage = pygame.image.load('images/ball.png')
ballRect = ballImage.get_rect()
bounceSound = pygame.mixer.Sound('sounds/boing.wav')
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.set_volume(0.9) # Le bajamos el volumen
pygame.mixer.music.play(-1, 0.0)

# 5 - Inicializamos variables
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# 6 - Bucle infinito
while True:
    # 7 - Comprobar y manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Realizar acciones "por cuadro"
    if ballRect.left < 0 or ballRect.right >= WINDOW_WIDTH:
        xSpeed = -xSpeed
        bounceSound.play()
    if ballRect.top < 0 or ballRect.bottom >= WINDOW_HEIGHT:
        ySpeed = -ySpeed
        bounceSound.play()

    # Actualiza la localización de la pelota, usando la velocidad en dos direcciones
    ballRect.left += xSpeed
    ballRect.top += ySpeed

    # 9 - Limpiar la ventana
    window.fill(BLACK)

    # 10 - Dibujar todos los elementos de la ventana
    window.blit(ballImage, ballRect)

    # 11 - Actualizar la ventana
    pygame.display.update()

    # 12 - Reducir la velocidad un poco
    clock.tick(FRAMES_PER_SECOND)
