import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event,ai_settings, screen, stats, ship, bullets):
    """Responde a pressionamento de tecla."""
    if stats.game_active:
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


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_play_button(ai_settings, screen, stats, sb,play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    """Inicia um novo jogo quando o jogador clicar em Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Renicia as configuraçoes do jogo
        ai_settings.initialize_dynamic_settings()

        # Oculta o cursor do mouse
        pygame.mouse.set_visible(False)

        # Renicia os dados estatisticos do jogo
        stats.reset_stats()
        stats.game_active = True

        # Reinicia as imagens do painel de pontuaçao
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ship()

        # Esvazia a lista de alienigenas e de projeteis
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota e centraliza a espaçonave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, bg, play_button):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    screen.blit(bg, (0, 0))

    # Redesenha todos os projeteis atras da espaçonave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Desenha a informaçao sobre pontuaçao
    sb.show_score()

    # Desenha o botao Play se o jogo estiver inativo
    if not stats.game_active:
        play_button.draw_button()

    # Deixa a tela mais recente visivel
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Atualiza a posiçao dos projeteis e se livra dos projeteis antigo."""
    # Atualiza as posiçoes dos projeteis
    bullets.update()

    # Livra-se dos projeteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde a colisoes entre porjeteis e alienigenas."""
    # Remove qualquer projetil e alienigena que tenham colidido
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # Em caso afirmativo, carrega-ra um som de explosao
    if collisions:
        son_explosion(ai_settings.sound_explosion)
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Se a frota toda for destruida, inicia um novo nivel
        bullets.empty()
        ai_settings.increase_speed()

        # Aumenta o nivel
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara um projetil se o limite ainda nao foi alcançado."""
    # Cria um novo projetil e o adiciona ao grupo de projeteis
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        # Em caso afirmativo carrega-ra um som de tiro
        if new_bullet:
            son_bullet(ai_settings.sound)
            bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """"Determina o numero de alienigenas que cabem em uma linha."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_numbers_rows(ai_settings, ship_height, alien_height):
    """Determina o numero de linhas com alienigenas que cabem na tela."""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    numbers_rows = int(available_space_y /(2 * alien_height))
    return numbers_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Cria um alienigena e o posiciona na linha
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Cria uma frota completa de alienigena"""
    # Cria um alienigena e calcula o numero de alienigenas em uma linha
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    numbers_rows = get_numbers_rows(ai_settings, ship.rect.height,
                                    alien.rect.height)

    # Cria a frota de alienigenas
    for row_number in range(numbers_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)


def check_fleet_edges(ai_settings, aliens):
    """Responde apropriadamente se algum alienigena alcançou uma borda."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_setthinds, aliens):
    """Faz toda a frota descer e muda a sua direçao."""
    for alien in aliens.sprites():
        alien.rect.y += ai_setthinds.fleet_drop_speed
    ai_setthinds.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Responde ao fato de a espaçonave ter sido atingida por um alienigena."""
    if stats.ships_left > 0:
        # Decrementa ships_left
        stats.ships_left -= 1

        # Atualiza o painel de pontuaçoes
        sb.prep_ship()

        # Esvazia a lista de alienigenas e de projeteis
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota e centraliza a espaçonave
        ship.center_ship()

        # Faz uma pausa
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Verifica se algum alienigena alcançou a parte inferior da tela."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Trata esse caso do mesmo modo que e feito quando a espaçonave e atingida
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    Verifica se a frota esta em uma das bordas
    e entao atualiza as posiçoes de todos os alienigenas da frota.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Verifica se houve colisoes entre alienigenas e a espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # Verifica se ha algum alienigena que atingiu a parte inferior da tela
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def son_bullet(son):
    """Carrega um son de tiro para nave"""
    pygame.mixer.music.load(son)
    pygame.mixer.music.play()


def son_explosion(son):
    """Carrega um son de explosao para nave alienigena"""
    pygame.mixer.music.load(son)
    pygame.mixer.music.play()


def check_high_score(stats, sb):
    """Verifica se ha uma nova pontuaçao maxima."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()