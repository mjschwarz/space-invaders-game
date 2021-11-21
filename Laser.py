import pygame
import helpers
import assets


class Laser:
    """
    Represents a laser shot from a spaceship.

    Attributes:
        x: current x position
        y: current y position
        img: laser model image
        mask: fixes laser model so that collisions occur on pixel-by-pixel basis
    """

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def display(self):
        """
        Displays the laser to the window.
        """
        assets.WINDOW.blit(self.img, (self.x, self.y))

    def move(self, vel):
        """
        Advances the laser.
        :param vel: velocity of the laser
        """
        self.y += vel

    def off_screen(self, height):
        """
        Checks if the laser has run off the screen.
        :param height: height of the screen
        :return:
        """
        return not(height >= self.y >= 0)

    def collision(self, ship):
        """
        Checks if a laser has collided with a ship.
        :param ship: ship being checked for collision
        """
        return helpers.collide(self, ship)
