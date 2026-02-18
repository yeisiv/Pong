import pygame

class Stick:
    global screen

    def __init__(self, x, y, width, heigh, colour):
        self.x = x
        self.y = y
        self.width = width
        self.heigh = heigh
        self.colour = colour
        self.rect = pygame.Rect(x,y,width, heigh)
        self.draw = pygame.draw.rect(Stick.screen, colour, self.rect)

    def update (self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.draw = pygame.draw.rect(Stick.screen, self.colour, self.rect)