import pygame
from game import settings

def draw_hud(tela, energia, energia_max, pontos):
    largura_barra = 200
    altura_barra = 20
    x_barra = 10
    y_barra = 10

    pygame.draw.rect(tela, settings.CINZA, (x_barra, y_barra, largura_barra, altura_barra))
    largura_energia = int((energia / energia_max) * largura_barra)
    pygame.draw.rect(tela, settings.VERMELHO, (x_barra, y_barra, largura_energia, altura_barra))

    fonte = pygame.font.SysFont(None, 28)
    texto = fonte.render(f"Pontos: {pontos}", True, settings.PRETO)
    tela.blit(texto, (x_barra, y_barra + altura_barra + 5))
