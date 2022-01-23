class Game_Stats():
    """Armazena dados estatisticos da Invasao Alienigena."""

    def __init__(self, ai_settings):
        """Inicializa os dados estatisticos."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Inicia a Invasao Alienigena em um estado ativo
        self.game_active = True

    def reset_stats(self):
        """Inicializa os dados estatisticos que podem mudar durante o jogo."""
        self.ships_left = self.ai_settings.ship_limit
