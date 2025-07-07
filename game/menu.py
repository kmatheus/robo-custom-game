import pygame
from game import settings

def desenhar_botao(tela, texto, rect, cor_fundo, cor_texto):
    pygame.draw.rect(tela, cor_fundo, rect, border_radius=8)
    fonte = pygame.font.SysFont(None, 36)
    texto_renderizado = fonte.render(texto, True, cor_texto)
    texto_rect = texto_renderizado.get_rect(center=rect.center)
    tela.blit(texto_renderizado, texto_rect)

def exibir_menu(tela):
    largura = settings.LARGURA_TELA
    altura = settings.ALTURA_TELA

    fonte_titulo = pygame.font.SysFont(None, 60)
    titulo = fonte_titulo.render("Robô Custom Game", True, settings.PRETO)
    titulo_rect = titulo.get_rect(center=(largura // 2, altura // 3))

    botao_jogar = pygame.Rect(largura // 2 - 100, altura // 2, 200, 50)
    botao_sair = pygame.Rect(largura // 2 - 100, altura // 2 + 70, 200, 50)

    while True:
        tela.fill(settings.BRANCO)
        tela.blit(titulo, titulo_rect)

        desenhar_botao(tela, "Jogar", botao_jogar, settings.VERDE, settings.BRANCO)
        desenhar_botao(tela, "Sair", botao_sair, settings.VERMELHO, settings.BRANCO)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if botao_jogar.collidepoint(evento.pos):
                    return  # Inicia o jogo
                if botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    exit()
