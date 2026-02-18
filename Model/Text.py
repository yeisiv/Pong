import pygame

class Texto:
    global screen

    def __init__(self, x, y, colour, content, tipo, size):
        self.x = x
        self.y = y
        self.colour = colour
        self.content = content
        self.tipo = tipo
        self.size = size

        fontWidth = pygame.font.SysFont(tipo, size)
        render = fontWidth.render(content, True, colour)
        cuadrado = render.get_rect()
        cuadrado.center = (x,y)
        Texto.screen.blit(render, cuadrado)

    def update(self, content):
        self.content = content
        fontWidth = pygame.font.SysFont(self.tipo, self.size)
        render = fontWidth.render(content, True, self.colour)
        cuadrado = render.get_rect()
        cuadrado.center = (self.x, self.y)
        Texto.screen.blit(render, cuadrado)