import sys
import pygame

from bullet import Bullet


def check_keydown_events(event,ai_settings, screen, ship, bullets):
    """Responde a pressionamento de tecla."""
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Responde a solturas de tecla."""
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_q:
        sys.exit()


def check_events(ai_settings, screen, ship, bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    # Redesenha todos os projeteis atras da espaçonave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Deixa a tela mais recente visivel
    pygame.display.flip()


def update_bullets(bullets):
    """Atualiza a posiçao dos projeteis e se livra dos projeteis antigo."""
    # Atualiza as posiçoes dos projeteis
    bullets.update()

    # Livra-se dos projeteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara um projetil se o limite ainda nao foi alcançado."""
    # Cria um novo projetil e o adiciona ao grupo de projeteis
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
