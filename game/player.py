import pygame
from game import settings

class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = settings.LARGURA_TELA // 2 - self.width // 2
        self.y = settings.ALTURA_TELA // 2 - self.height // 2
        self.vel = 5
        self.energia_max = 100
        self.energia = self.energia_max
        self.energia_use = 10
        self.vida_max = 100
        self.vida = self.vida_max
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        # Limites da tela
        self.x = max(0, min(self.x, settings.LARGURA_TELA - self.width))
        self.y = max(0, min(self.y, settings.ALTURA_TELA - self.height))

        # Atualiza o retângulo
        self.rect.topleft = (self.x, self.y)

    def draw(self, tela):
        pygame.draw.rect(tela, settings.AZUL, self.rect)

    def can_shoot(self):
        return self.energia >= self.energia_use

    def shoot(self):
        self.energia -= self.energia_use

    def recharge(self, valor):
        self.energia = min(self.energia_max, self.energia + valor)

    def levar_dano(self, valor):
        self.vida -= valor
        if self.vida < 0:
            self.vida = 0

    def esta_vivo(self):
        return self.vida > 0
    
