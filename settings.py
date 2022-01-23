class Settings():
    """Uma classe para armazenar todas as configuraçoes da Invasao Alienigena."""

    def __init__(self):
        """Inicializa as configuraçoes do jogo."""
        # Configuraçoes da tela
        self.screen_width = 1200
        self.screen_height = 680
        self.bg_color = (230, 230, 230)
        self.image = "images/bg.bmp"

        # Configuraçao da espaçonave
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Configuraçao do projeteis
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 0, 0)
        self.bullets_allowed = 3
        self.sound = "sound/sounds_shoot.wav"

        # Configuraçao dos alienigena
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1
        self.sound_explosion = "sound/sounds_shipexplosion.wav"
