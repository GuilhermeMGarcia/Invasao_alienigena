import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Uma classe que administra projeteis disparados pela espaçonave"""

    def __init__(self, ai_settings, screen, ship):
        """Cria um obejeto para o projetil na posiçao atual da espaçonave."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Cria um retangulo para o projetil em (0, 0) e, em seguida, define a
        # posiçao correta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_heigth)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Armazena a posiçao do projetil como um valor decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move o projetil para cima na tela."""
        self.y -= self.speed_factor
        # Atualiza a posiçao de rect
        self.rect.y = self.y

    def draw_bullet(self):
        """"Desenha o projetil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)