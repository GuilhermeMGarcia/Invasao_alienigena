class Settings():
    """Uma classe para armazenar todas as configuraçoes da Invasao Alienigena."""

    def __init__(self):
        """Inicializa as configuraçoes do jogo."""
        # Configuraçoes da tela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Configuraçao da espaçonave
        self.ship_speed_factor = 1.5

        # Configuraçao do projeteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)