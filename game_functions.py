import sys
import pygame

from bullet import Bullet


def check_events(ship):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visivel
    pygame.display.flip()

def check_keydown_events(event, ship):
    """Responde a pressionamento de tecla."""
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """Responde a solturas de tecla."""
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
