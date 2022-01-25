import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import Game_Stats
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

    #Cria o botao play
    play_button = Button(ai_settings, screen, "Play")

    #Cria uma instancia para armazenar dados estatisticos do jogo
    stats = Game_Stats(ai_settings)

    #Cria uma espaçonave
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serao armazenados os projeteis
    bullets = Group()
    aliens = Group()

    # Cria a frota de alienigena
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Tela de fundo
    bg = pygame.image.load(ai_settings.image)

    # Son de tiro nave
    #son = pygame.mixer.music.load(ai_settings.sound)

    # Inicializa um laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, bg, play_button)

run_game()
