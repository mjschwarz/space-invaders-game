import pygame
from Spaceship import Spaceship
from Laser import Laser
import assets


class Invader(Spaceship):
    """
    Represents an invader spaceship. Derived from the Spaceship base class.

    Attributes:
        x: current x position
        y: current y position
        health: current health
        ship_img: image used to model ship
        laser_img: image used to model ship's laser
        lasers: list of all of ship's active lasers
        cool_down_counter: countdown until ship can fire another laser
        mask: fixes ship model so that collisions happen on a pixel by pixel basis
    """
    # map color name to image models for ship and laser
    COLOR_MAP = {
                "red": (assets.RED_SPACE_SHIP, assets.RED_LASER),
                "green": (assets.GREEN_SPACE_SHIP, assets.GREEN_LASER),
                "blue": (assets.BLUE_SPACE_SHIP, assets.BLUE_LASER)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        """
        Advances the invader down the screen.
        :param vel: ship's velocity
        """
        self.y += vel

    def shoot(self):
        """
        Fires a laser.
        """
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            # start cooldown
            self.cool_down_counter = self.max_cooldown
