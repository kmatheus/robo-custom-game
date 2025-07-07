import pygame
from game import settings

def mostrar_game_over(tela):
    tela.fill(settings.PRETO)
    fonte = pygame.font.SysFont(None, 64)
    texto = fonte.render("GAME OVER", True, settings.VERMELHO)
    tela.blit(texto, (settings.LARGURA_TELA // 2 - texto.get_width() // 2, 200))

    fonte_menor = pygame.font.SysFont(None, 36)
    instrucoes = fonte_menor.render("Pressione ENTER para reiniciar", True, settings.BRANCO)
    tela.blit(instrucoes, (settings.LARGURA_TELA // 2 - instrucoes.get_width() // 2, 300))

    pygame.display.update()

    esperando_tecla = True
    while esperando_tecla:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    esperando_tecla = False
