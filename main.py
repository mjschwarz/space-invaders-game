import sys
import pygame
import time
import random
import constants
from Player import Player
from Invader import Invader
import helpers
import assets


def refresh_display(player, invaders, lives, level, lost):
    """
    Updates the game display for each frame.
    :param player: player's ship
    :param invaders: list of all active invaders
    :param lives: number of lives remaining
    :param level: current game level
    :param lost: boolean, whether player has lost or not
    """
    assets.WINDOW.blit(assets.BG, (0, 0))

    # display game information
    lives_label = assets.MAIN_FONT.render(f"Lives: {lives}", True, constants.WHITE)
    level_label = assets.MAIN_FONT.render(f"Level: {level}", True, constants.WHITE)
    score_label = assets.MAIN_FONT.render(f"Score: {player.score}", True, constants.WHITE)
    assets.WINDOW.blit(lives_label, (10, 10))
    assets.WINDOW.blit(level_label, (constants.WIDTH - level_label.get_width() - 10, 10))
    assets.WINDOW.blit(score_label, (constants.WIDTH / 2 - score_label.get_width() / 2, 10))

    # update invader changes to screen
    for enemy in invaders:
        enemy.display_changes()
    # update player changes to screen
    player.display_changes()

    # check if lost - display message
    if lost:
        lost_label = assets.LOST_FONT.render("You Lost!", True, constants.WHITE)
        assets.WINDOW.blit(lost_label, (constants.WIDTH / 2 - lost_label.get_width() / 2, 350))

    pygame.display.update()


def manage_invaders(player, invaders, lives):
    """
    Updates the status of each invader.
    :param player: player's ship
    :param invaders: list of all active invaders
    :param lives: number of lives remaining
    """
    for invader in invaders[:]:
        # advance down the screen
        invader.move(constants.INVADER_VEL)
        invader.advance_lasers(constants.LASER_VEL, player)

        # shoot
        if random.randrange(0, 2 * 60) == 1:
            invader.shoot()

        # collision with player
        if helpers.collide(invader, player):
            player.health -= constants.HIT_PTS
            invaders.remove(invader)
            player.score += constants.HIT_PTS

        # past bottom of screen
        elif invader.y + invader.get_height() > constants.HEIGHT:
            lives -= 1
            invaders.remove(invader)

    return player, invaders, lives


def create_next_wave(level, wave_invaders, invaders, player):
    """
    Resets the game for the next wave of invaders.
    :param level: current level
    :param wave_invaders: amount of invaders per wave
    :param invaders: list of active invaders
    :param player: player's ship
    """
    # update game variables
    level += 1
    player.score += constants.ROUND_PTS * (level - 1)
    wave_invaders += 3

    # regenerate some health
    player.health += (player.max_health - player.health) / 2

    # new wave warning
    wave_label = assets.WAVE_FONT.render(f"Wave {level} Incoming!", True, constants.WHITE)
    assets.WINDOW.blit(wave_label, (constants.WIDTH / 2 - wave_label.get_width() / 2, 350))
    pygame.display.update()
    time.sleep(2)

    # create next wave of invaders
    for i in range(wave_invaders):
        invader = Invader(random.randrange(50, constants.WIDTH - 100), random.randrange(-1500, -100),
                          random.choice(["red", "blue", "green"]))
        invaders.append(invader)

    return level, wave_invaders, invaders


def game_loop(high_score):
    """
    Controls main game loop.
    """
    # initialize game variables and objects
    lives = 5
    level = 0
    invaders = []
    wave_invaders = 5
    player = Player(300, 630)

    while True:
        # refresh display
        assets.CLOCK.tick(constants.FPS)
        refresh_display(player, invaders, lives, level, False)

        # check if lost
        if helpers.game_lost(lives, player):
            refresh_display(player, invaders, lives, level, True)
            high_score = helpers.calc_high_score(player, high_score)
            time.sleep(1.5)
            return high_score

        # level complete - all invaders dead
        if len(invaders) == 0:
            level, wave_invaders, invaders = create_next_wave(level, wave_invaders, invaders, player)

        # check user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # execute player movement
        keys = pygame.key.get_pressed()
        helpers.get_player_input(keys, player)

        # update and advance invaders
        player, invaders, lives = manage_invaders(player, invaders, lives)

        # advance player lasers
        player.advance_lasers(-constants.LASER_VEL, invaders)


def main_menu():
    """
    Controls the main menu.
    """
    high_score = 0
    run = True
    while run:
        # main menu screen
        assets.WINDOW.blit(assets.BG, (0, 0))
        title_label = assets.TITLE_FONT.render("Press any key...", True, constants.WHITE)
        assets.WINDOW.blit(title_label, (constants.WIDTH/2 - title_label.get_width()/2, 350))
        helpers.display_high_score(high_score)
        pygame.display.update()

        # get user input (quit or start game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                high_score = game_loop(high_score)
    pygame.quit()
    sys.exit()


# --------
# RUN GAME
# --------
main_menu()
