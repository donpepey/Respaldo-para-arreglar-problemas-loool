import pygame
import sys

# Configuración ventana lol
ANCHO = 600
ALTO = 400
FPS = 60

# Configuración de la bola jaja lol xd
DIAMETRO = 20

# Colores RGB
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

class Bola:
    def __init__(self, pantalla, color, VELOCIDAD_X,VELOCIDAD_Y):

        self.pantalla = pantalla
        self.color = color
        self.x = ANCHO // 2
        self.y = ALTO // 2
        self.velocidad_x = VELOCIDAD_X
        self.velocidad_y = VELOCIDAD_Y

        def actualizar(self):
            self.x += self.velocidad_x
            self.y += self.velocidad_y

            if self.x-DIAMETRO <= 0 or self.x + DIAMETRO >= ANCHO:
                self.velocidad_x *= -1
            if self.y-DIAMETRO <= 0 or self.y + DIAMETRO >= ALTO:
                self.velocidad_y *= -1

        def dibujar(self):
            pygame.draw.circle(self.pantalla, self.color, (self.x, self.y), DIAMETRO)

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Bola rebotando lool")
reloj = pygame.time.Clock()

# Crear la bola
bola = Bola(pantalla, ROJO,7,4)
bola2 = Bola(pantalla, VERDE,3,5)

# Bucle principal lol
terminado = False
while not terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado= True

    # Actualizar la bola
    bola.actualizar()
    bola2.actualzar()

    # Limpiar la pantalla lol
    pantalla.fill(BLANCO)

    # Dibujar la bolaaaa
    bola.dibujar()
    bola2.dibujar()

    # Actualizar la pantalla
    pygame.display.flip()

    # Control de FPS
    reloj.tick(60)

pygame.quit()
sys.exit()
