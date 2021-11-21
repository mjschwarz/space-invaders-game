import pygame
from Spaceship import Spaceship
import constants
import assets


class Player(Spaceship):
    """
    Represents the player spaceship. Derived from the Spaceship base class.

    Attributes:
        x: current x position
        y: current y position
        health: current health
        ship_img: image used to model ship
        laser_img: image used to model ship's laser
        lasers: list of all of ship's active lasers
        cool_down_counter: countdown until ship can fire another laser
        mask: fixes ship model so that collisions happen on a pixel by pixel basis
        max_health: maximum health of ship
        score: current score
    """
    def __init__(self, x, y, health=100, score=0):
        super().__init__(x, y, health)
        self.ship_img = assets.YELLOW_SPACE_SHIP
        self.laser_img = assets.YELLOW_LASER
        self.max_cooldown = 15
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.score = score

    def advance_lasers(self, vel, invaders):
        """
        Advances the active lasers.
        Overrides the base class method.
        :param vel: velocity of the lasers
        :param invaders:
        :return:
        """
        self.manage_cooldown()
        # advance all active lasers
        for laser in self.lasers:
            laser.move(vel)
            # off top of screen
            if laser.off_screen(constants.HEIGHT):
                self.lasers.remove(laser)
            else:
                for invader in invaders:
                    # collision with invader
                    if laser.collision(invader):
                        invaders.remove(invader)
                        self.score += 10
                        # remove from active lasers
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def display_changes(self):
        """
        Displays the player ship to the game window.
        Overrides the base class method.
        """
        super().display_changes()
        self.update_healthbar()

    def update_healthbar(self):
        """
        Updates and displays the health bar.
        """
        # red bar
        pygame.draw.rect(assets.WINDOW, constants.RED, (self.x,
                                                        self.y + self.ship_img.get_height() + 10,
                                                        self.ship_img.get_width(),
                                                        10))
        # green bar
        pygame.draw.rect(assets.WINDOW, constants.GREEN, (self.x,
                                                          self.y + self.ship_img.get_height() + 10,
                                                          self.ship_img.get_width() * (self.health / self.max_health),
                                                          10))
