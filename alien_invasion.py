import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import Game_Stats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # Inicializa o pygame, as configuraçoes e o objeto screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Ivansion")

    # Cria o botao play
    play_button = Button(ai_settings, screen, "Play")

    # Cria instancia para armazenar estatisticas do jogo e cria painel de pontuaçao
    stats = Game_Stats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serao armazenados os projeteis
    bullets = Group()
    aliens = Group()

    # Cria a frota de alienigena
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Tela de fundo
    bg = pygame.image.load(ai_settings.image)

    # Inicializa um laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, bg, play_button)

run_game()
