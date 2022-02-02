import pygame.font


class Scoreboard():
    """Uma classe para mostrar informaçoes sobre pontuaçao."""

    def __init__(self, ai_settings, screen, stats):
        """Incializa os atributos da pontuaçao."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Configuraçoes de fonte para as inforaçoes de pontuaçao
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara a imagem da pontuaçao inicial
        self.prep_score()
        self.prep_high_score()

    def prep_high_score(self):
        """Transforma a pontuaçao maxima em uma imagem renderiada."""
        high_score = int(round(self.stats.score, -1))
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.ai_settings.bg_color)

        # Centraliza a pontuaçao maxima na parte superior da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_score(self):
        """Transforma a pontuaçao em uma imagem renderiada."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.ai_settings.bg_color)

        # Exibe a pontuaçao na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """"Desenha a pontuaçao na tela."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
