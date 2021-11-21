import constants
import pygame
import os

# ------------------
# LOAD VISUAL ASSETS
# ------------------
RED_SPACE_SHIP = pygame.image.load(os.path.join("img", "ship_red.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("img", "ship_green.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("img", "ship_blue.png"))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("img", "ship_yellow.png"))

RED_LASER = pygame.image.load(os.path.join("img", "laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("img", "laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("img", "laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("img", "laser_yellow.png"))

BG = pygame.transform.scale(pygame.image.load(os.path.join("img", "background.png")),
                            (constants.WIDTH, constants.HEIGHT))

# ---------------------------
# SETUP PYGAME CONFIGURATIONS
# ---------------------------
pygame.font.init()
pygame.display.set_caption("Space Invaders")
WINDOW = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
CLOCK = pygame.time.Clock()

# -----------
# SETUP FONTS
# -----------
TITLE_FONT = pygame.font.SysFont("helvetica", 70)
MAIN_FONT = pygame.font.SysFont("helvetica", 50)
LOST_FONT = pygame.font.SysFont("helvetica", 60)
WAVE_FONT = pygame.font.SysFont("Aerial", 70)



