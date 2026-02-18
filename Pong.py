import pygame
from Model.Ball import Ball
from Model.Text import Texto
from Model.Barras import Stick
# CONSTANTES
WIDTH = 1200
HEIGHT = 800
FPS = 20
ESPACIO_MARCADOR = ' '
VELOCIDAD_BALL = 20
VELOCIDAD_STICKS = 20
# COLORES
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FUCSIA = (255,0,255)

# inicio pygame
pygame.init()
CLOCK = pygame.time.Clock()

# defino el tamaño de mi pantalla
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
Ball.screen = screen
Texto.screen = screen
Stick.screen = screen


circulo_out=Ball(75,WIDTH/2,HEIGHT/2, WHITE)
circulo_in = Ball(60,WIDTH/2,HEIGHT/2, BLACK)
barra_centro_arriba = Stick(0,0,25,HEIGHT, WHITE)
pelota = Ball(10, 100, 100, FUCSIA)
marcador =Texto(WIDTH/2, 20, WHITE, "Muertes = 0", "Arial", 15)
Stick1 = Stick(15,300,15,100, WHITE)
Stick2 = Stick(WIDTH-15,300,15,100, WHITE)
ESPACIO_MARCADOR*=barra_centro_arriba.width//2
ok = True

ir_derecha = 1
ir_arriba = 1

contadorLocal = 0
contadorVisitante =0
while ok:
    # reinicio la pantalla a default
    screen.fill(BLACK)
    mi_x = pelota.pos_x
    mi_y = pelota.pos_y
    y_Stick1 = Stick1.y
    y_Stick2 = Stick2.y
    # controlo los eventos entre frames
    for event in pygame.event.get():
        # boton de cerrar
        if event.type == pygame.QUIT:
            ok = False
        # pulsar botones de teclado
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         ir_arriba = 0
        #         ir_derecha = 1
        #     if event.key == pygame.K_LEFT:
        #         ir_arriba = 0
        #         ir_derecha = -1
        #     if event.key == pygame.K_UP:
        #         ir_arriba = -1
        #     if event.key == pygame.K_DOWN:
        #         ir_arriba = 1
        #     if event.key == pygame.K_KP_3:
        #         ir_arriba = 1
        #     if event.key == pygame.K_KP_7:
        #         ir_arriba = -1

    tecla = pygame.key.get_pressed()

    if tecla[pygame.K_w] and y_Stick1>=Stick1.heigh/2:
        y_Stick1 = Stick1.y - VELOCIDAD_STICKS
    elif tecla[pygame.K_s] and y_Stick1<HEIGHT - Stick1.heigh/2:
        y_Stick1 = Stick1.y + VELOCIDAD_STICKS

    if tecla[pygame.K_UP] and y_Stick2>=Stick2.heigh/2:
        y_Stick2 = Stick2.y - VELOCIDAD_STICKS
    elif tecla[pygame.K_DOWN] and y_Stick2<HEIGHT - Stick2.heigh/2:
        y_Stick2 = Stick2.y + VELOCIDAD_STICKS

    #Colisión
    if pygame.Rect.colliderect(pelota.draw, Stick1.draw):
        ir_derecha *= -1
        VELOCIDAD_BALL+=3
        VELOCIDAD_STICKS+=4

    if pygame.Rect.colliderect(pelota.draw, Stick2.draw):
        ir_derecha *= -1
        VELOCIDAD_BALL += 3
        VELOCIDAD_STICKS += 4
    #
    # if pygame.Rect.colliderect(pelota.draw, Stick2.draw):
    #     ir_derecha *= -1
    #     VELOCIDAD_BALL += 5
    #     VELOCIDAD_STICKS += 5


    if ir_arriba == -1:
        mi_y = pelota.pos_y - VELOCIDAD_BALL
    elif ir_arriba == 1:
        mi_y = pelota.pos_y + VELOCIDAD_BALL

    if ir_derecha == -1:
        mi_x = pelota.pos_x - VELOCIDAD_BALL
    elif ir_derecha == 1:
        mi_x = pelota.pos_x + VELOCIDAD_BALL

    if mi_x >= WIDTH:
        ir_derecha = -1
        contadorLocal+=1
        VELOCIDAD_BALL = 20
        VELOCIDAD_STICKS = 20
    if mi_x <= 0:
        ir_derecha = 1
        contadorVisitante += 1
        VELOCIDAD_BALL = 20
        VELOCIDAD_STICKS = 20

    if mi_y >= HEIGHT:
        ir_arriba = -1
        VELOCIDAD_BALL += 2
        VELOCIDAD_STICKS += 3
    if mi_y <= 0:
        ir_arriba = 1
        VELOCIDAD_BALL += 2
        VELOCIDAD_STICKS += 3

    circulo_out.update(WIDTH / 2, HEIGHT / 2)
    barra_centro_arriba.update(WIDTH/2,HEIGHT/2)
    circulo_in.update(WIDTH/2,HEIGHT/2)
    Stick1.update(Stick1.x, y_Stick1)
    Stick2.update(Stick2.x, y_Stick2)
    pelota.update(mi_x, mi_y)
    marcador.update(f"{contadorLocal}{ESPACIO_MARCADOR}{contadorVisitante}")


    # actualizo al siguiente frame
    CLOCK.tick(FPS)
    pygame.display.update()

    if mi_x <= 0 or mi_x >= WIDTH:
        pelota.pos_x = WIDTH/2
        pelota.pos_y = HEIGHT/2