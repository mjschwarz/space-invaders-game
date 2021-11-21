from Laser import Laser
import constants
import assets


class Spaceship:
    """
    Represents a spaceship.

    Abstracts base class. Provides an interface for what a spaceship should look like.

    Attributes:
        x: current x position
        y: current y position
        health: current health
        ship_img: image used to model ship
        laser_img: image used to model ship's laser
        lasers: list of all of ship's active lasers
        cool_down_counter: countdown until ship can fire another laser
        max_cooldown: maximum cooldown time
    """
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        self.max_cooldown = 30

    def display_changes(self):
        """
        Displays each active laser in the window.
        """
        assets.WINDOW.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.display()

    def advance_lasers(self, vel, ship):
        """
        Advances all of the ship's active lasers.
        :param vel: laser's velocity
        :param ship: object that the laser has hit
        """
        self.manage_cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(constants.HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(ship):
                ship.health -= 10
                self.lasers.remove(laser)

    def manage_cooldown(self):
        """
        Tracks the time until the ship can fire another laser.
        """
        # cooldown finished
        if self.cool_down_counter <= 0:
            self.cool_down_counter = 0
        # otherwise increment countdown
        elif self.cool_down_counter > 0:
            self.cool_down_counter -= 1

    def shoot(self):
        """
        Fires a laser.
        """
        if self.cool_down_counter <= 0:
            laser = Laser(self.x, self.y, self.laser_img)
            # add to list of active lasers
            self.lasers.append(laser)
            # start cooldown counter
            self.cool_down_counter = self.max_cooldown

    def get_width(self):
        """
        Returns ship's width.
        """
        return self.ship_img.get_width()

    def get_height(self):
        """
        Returns the ship's height.
        """
        return self.ship_img.get_height()
