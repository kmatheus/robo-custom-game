import pygame
from game import settings

def draw_hud(tela, energia, energia_max, vida, vida_max, pontos):
    largura_barra = 200
    altura_barra = 20
    x_barra = 10
    y_barra_energia = 10
    y_barra_vida = y_barra_energia + altura_barra + 10

    pygame.draw.rect(tela, settings.CINZA, (x_barra, y_barra_energia, largura_barra, altura_barra))
    largura_energia = int((energia / energia_max) * largura_barra)
    pygame.draw.rect(tela, settings.VERMELHO, (x_barra, y_barra_energia, largura_energia, altura_barra))

    pygame.draw.rect(tela, settings.CINZA, (x_barra, y_barra_vida, largura_barra, altura_barra))
    largura_vida = int((vida / vida_max) * largura_barra)
    pygame.draw.rect(tela, settings.VERDE, (x_barra, y_barra_vida, largura_vida, altura_barra))

    fonte = pygame.font.SysFont(None, 28)

    texto_pontos = fonte.render(f"Pontos: {pontos}", True, settings.PRETO)
    tela.blit(texto_pontos, (x_barra, y_barra_vida + altura_barra + 5))

    texto_vida = fonte.render(f"Vida: {vida}/{vida_max}", True, settings.PRETO)
    tela.blit(texto_vida, (x_barra + largura_barra + 10, y_barra_vida))

