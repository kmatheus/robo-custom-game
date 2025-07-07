import pygame

class Explosion:
    def __init__(self, rect, cor=(255, 140, 0), tamanho=40):
        self.rect = rect
        self.cor = cor
        self.tamanho = tamanho
        self.tempo_inicio = pygame.time.get_ticks()
        self.duracao = 300

    def draw(self, tela):
        tempo_decorrido = pygame.time.get_ticks() - self.tempo_inicio
        if tempo_decorrido < self.duracao:
            alpha = 255 - int((tempo_decorrido / self.duracao) * 255)
            superficie = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            superficie.fill((*self.cor, alpha))
            tela.blit(superficie, self.rect.topleft)

    def acabou(self):
        return pygame.time.get_ticks() - self.tempo_inicio > self.duracao
