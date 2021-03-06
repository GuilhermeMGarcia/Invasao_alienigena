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
        self.ship_limit = 3

        # Configuraçao do projeteis
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 0, 0)
        self.bullets_allowed = 3
        self.sound = "sound/sounds_shoot.wav"

        # Configuraçao dos alienigena
        self.fleet_drop_speed = 10
        self.sound_explosion = "sound/sounds_shipexplosion.wav"

        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1

        # A taxa com que os pontos para cada alienigena aumentam
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa as configuraçoes que mudam no decorrer do jogo."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction igual a 1 representa a diereita; -1 representa a esquerda
        self.fleet_direction = 1

        # Pontuaçao
        self.alien_points = 50

    def increase_speed(self):
        """Aumenta as configuraçoes de velocidade e os pontos para cada alienigena."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor += self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
