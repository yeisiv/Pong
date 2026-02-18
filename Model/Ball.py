import pygame

class Ball:
    # pantalla como variable de clase
    global screen

    def __init__(self, radius, pos_x, pos_y, color):
        self.radius = radius
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.draw = pygame.draw.circle(
            surface= Ball.screen,
            color= color,
            center= (pos_x, pos_y),
            radius= radius
        )

    # vuelvo a dibujar mi pelota
    def update(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.draw = pygame.draw.circle(
            Ball.screen,
            self.color,
            (pos_x, pos_y),
            self.radius
        )

    