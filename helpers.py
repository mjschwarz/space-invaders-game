import pygame
import sys
import constants
import assets


def collide(obj1, obj2):
    """
    Checks if two objects (ship-ship or ship-laser) have collided.
    :param obj1: either a ship or a laser
    :param obj2: either a ship of a laser
    """
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    # check for collision - pixel by pixel
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


def get_player_input(keys, player):
    """
    Checks what keys the player has pressed.
    :param keys: list of the keys pressed
    :param player: player's ship
    """
    # left
    if keys[pygame.K_a] and player.x - constants.PLAYER_VEL > 0:
        player.x -= constants.PLAYER_VEL
    # right
    if keys[pygame.K_d] and player.x + constants.PLAYER_VEL + player.get_width() < constants.WIDTH:
        player.x += constants.PLAYER_VEL
    # up
    if keys[pygame.K_w] and player.y - constants.PLAYER_VEL > 0:
        player.y -= constants.PLAYER_VEL
    # down
    if keys[pygame.K_s] and player.y + constants.PLAYER_VEL + player.get_height() + 15 < constants.HEIGHT:
        player.y += constants.PLAYER_VEL
    # shoot
    if keys[pygame.K_SPACE]:
        player.shoot()
    # quit
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()


def game_lost(lives, player):
    """
    Checks if the game has been lost.
    :param lives: number of lives remaining
    :param player: player's ship
    """
    return lives <= 0 or player.health <= 0


def calc_high_score(player, high_score):
    """
    Calculates the new high score.
    :param player: player object
    :param high_score: current high score
    """
    return max(player.score, high_score)


def display_high_score(high_score):
    """
    Displays the high score on the main menu.
    :param high_score: current high score
    """
    high_score_label = assets.MAIN_FONT.render(f"High Score: {high_score}", True, constants.WHITE)
    assets.WINDOW.blit(high_score_label, (constants.WIDTH / 2 - high_score_label.get_width() / 2, 10))





