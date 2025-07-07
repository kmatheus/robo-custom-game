import pygame
from game import settings

class Enemy:
    def __init__(self, y):
        self.width = 40
        self.height = 40
        self.x = settings.LARGURA_TELA
        self.y = y
        self.speed = 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.rect.x -= self.speed

    def draw(self, tela):
        pygame.draw.rect(tela, settings.PRETO, self.rect)

    def is_off_screen(self):
        return self.rect.right < 0
