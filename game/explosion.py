import pygame
from game import settings

class Explosion:
    def __init__(self, rect):
        self.rect = rect
        self.duration = 20  # frames
        self.counter = 0

    def update(self):
        self.counter += 1

    def draw(self, tela):
        pygame.draw.rect(tela, settings.LARANJA, self.rect)

    def terminou(self):
        return self.counter >= self.duration
