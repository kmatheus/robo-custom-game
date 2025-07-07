import pygame
import sys
import random

from game import settings
from game.game_over import mostrar_game_over
from game.settings import *
from game.menu import exibir_menu
from game.player import Player
from game.bullet import Bullet
from game.enemy import Enemy
from game.explosion import Explosion
from game.hud import draw_hud

pygame.init()
pygame.mixer.init()

TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Protótipo: Robô no Campo de Batalha")

exibir_menu(TELA)

# Carregamento de sons
som_tiro = pygame.mixer.Sound("assets/sounds/tiro.wav")
som_explosao = pygame.mixer.Sound("assets/sounds/explosao.wav")
pygame.mixer.music.load("assets/sounds/musica_fundo.mp3")
pygame.mixer.music.set_volume(0.3)  # volume da música de fundo
pygame.mixer.music.play(-1)  # toca em loop infinito


RELOGIO = pygame.time.Clock()

jogador = Player()
recarga = 40

tiros = []
inimigos = []
tiros_inimigos = []
explosoes = []
pontos = 0

pilha_largura, pilha_altura = 30, 30
x_pilha = random.randint(0, LARGURA_TELA - pilha_largura)
y_pilha = random.randint(0, ALTURA_TELA - pilha_altura)
pilha_rect = pygame.Rect(x_pilha, y_pilha, pilha_largura, pilha_altura)

contador_spawn = 0
spawn_intervalo = 90

game_rodando = True
while game_rodando:
    RELOGIO.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and jogador.can_shoot():
                tiro = Bullet(
                    jogador.rect.right,
                    jogador.rect.top + jogador.height // 2 - 2
                )
                tiros.append(tiro)
                jogador.shoot()
                som_tiro.play()

    teclas = pygame.key.get_pressed()
    jogador.update(teclas)

    for tiro in tiros:
        tiro.update()
    tiros = [t for t in tiros if not t.is_off_screen()]

    for inimigo in inimigos[:]:
        inimigo.update(jogador.rect.centery, tiros_inimigos)
        if inimigo.rect.colliderect(jogador.rect):
            som_explosao.play()
            jogador.levar_dano(20)
            explosoes.append(Explosion(jogador.rect.inflate(0, 0), cor=settings.VERMELHO))
            explosoes.append(Explosion(inimigo.rect.inflate(20, 20), cor=settings.LARANJA))
            inimigos.remove(inimigo)
    inimigos = [i for i in inimigos if not i.is_off_screen()]

    for tiro in tiros_inimigos[:]:
        tiro.update()
        if tiro.rect.colliderect(jogador.rect):
            jogador.levar_dano(10)
            explosoes.append(Explosion(jogador.rect.inflate(0, 0), cor=(255, 0, 0)))
            tiros_inimigos.remove(tiro)
    tiros_inimigos = [t for t in tiros_inimigos if not t.is_off_screen()]

    contador_spawn += 1
    if contador_spawn >= spawn_intervalo:
        y_pos = random.randint(0, LARGURA_TELA - 40)
        inimigos.append(Enemy(y=y_pos))
        contador_spawn = 0

    novos_tiros = []
    for tiro in tiros:
        acertou = False
        for inimigo in inimigos:
            if tiro.rect.colliderect(inimigo.rect):
                explosoes.append(Explosion(inimigo.rect.inflate(20, 20), cor=settings.LARANJA))
                inimigos.remove(inimigo)
                pontos += 1
                som_explosao.play()
                acertou = True
                break
        if not acertou:
            novos_tiros.append(tiro)
    tiros = novos_tiros

    for explosao in explosoes[:]:
        explosao.draw(TELA)
        if explosao.acabou():
            explosoes.remove(explosao)
    explosoes = [e for e in explosoes if not e.acabou()]

    if jogador.rect.colliderect(pilha_rect):
        jogador.recharge(recarga)
        x_pilha = random.randint(0, LARGURA_TELA - pilha_largura)
        y_pilha = random.randint(0, ALTURA_TELA - pilha_altura)
        pilha_rect = pygame.Rect(x_pilha, y_pilha, pilha_largura, pilha_altura)

    TELA.fill(BRANCO)
    jogador.draw(TELA)
    for tiro in tiros:
        tiro.draw(TELA)
    for tiro in tiros_inimigos:
        tiro.draw(TELA)
    for inimigo in inimigos:
        inimigo.draw(TELA)
    for explosao in explosoes:
        explosao.draw(TELA)
    pygame.draw.rect(TELA, VERDE, pilha_rect)
    draw_hud(TELA, jogador.energia, jogador.energia_max, jogador.vida, jogador.vida_max, pontos)

    pygame.display.update()

    if not jogador.esta_vivo():
        mostrar_game_over(TELA)
        jogador = Player()
        tiros = []
        inimigos = []
        explosoes = []
        pontuacao = 0
        tempo_ultimo_inimigo = pygame.time.get_ticks()


pygame.quit()
sys.exit()
