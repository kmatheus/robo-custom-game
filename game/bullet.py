import pygame
from game import settings

class Bullet:
    def __init__(self, x, y):
        self.width = 10
        self.height = 4
        self.color = settings.VERMELHO
        self.speed = 10
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def update(self):
        self.rect.x += self.speed

    def draw(self, tela):
        pygame.draw.rect(tela, self.color, self.rect)

    def is_off_screen(self):
        return self.rect.x > settings.LARGURA_TELA
