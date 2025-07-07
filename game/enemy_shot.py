import pygame
from game import settings

class EnemyShot:
    def __init__(self, x, y):
        self.width = 6
        self.height = 2
        self.speed = 7
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def update(self):
        self.rect.x -= self.speed

    def draw(self, tela):
        pygame.draw.rect(tela, settings.VERMELHO, self.rect)

    def is_off_screen(self):
        return self.rect.right < 0
