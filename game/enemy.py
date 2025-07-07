import pygame
import random
from game import settings
from game.enemy_shot import EnemyShot

class Enemy:
    def __init__(self, y):
        self.width = 40
        self.height = 40
        self.x = settings.LARGURA_TELA
        self.y = y
        self.speed = 2
        self.vertical_speed = 1.5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.tempo_ultimo_tiro = pygame.time.get_ticks()
        self.intervalo_tiro = random.randint(1000, 2500)

    def update(self, jogador_y, tiros_inimigos):
        self.rect.x -= self.speed

        if jogador_y < self.rect.centery:
            self.rect.y -= self.vertical_speed
        elif jogador_y > self.rect.centery:
            self.rect.y += self.vertical_speed

        agora = pygame.time.get_ticks()
        if agora - self.tempo_ultimo_tiro > self.intervalo_tiro:
            tiro = EnemyShot(self.rect.left, self.rect.centery)
            tiros_inimigos.append(tiro)
            self.tempo_ultimo_tiro = agora
            self.intervalo_tiro = random.randint(1000, 2500)

    def draw(self, tela):
        pygame.draw.rect(tela, settings.PRETO, self.rect)

    def is_off_screen(self):
        return self.rect.right < 0
