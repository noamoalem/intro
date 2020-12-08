#############################################################
# FILE : asteroid.py
# WRITER : nir_amzaleg & noamoa , Nir Amzaleg & Noa Moalem,
# 206959686, 208533554
# EXERCISE : intro2cs ex10 2019
# DESCRIPTION: Asteroid class. In this class the objects is an asteroid.
#  Each one has location, speed and size.
#############################################################

import math
from ship import Ship
from torpedo import Torpedo


class Asteroid:
    """ Asteroid class. In this class the objects is an asteroid.
        Each one has location, speed and size. """

    def __init__(self, x_y_sp, x_y_loc, size):

        self.x_y_sp = x_y_sp
        self.x_y_loc = x_y_loc
        self.size = size

    def get_x_y_sp(self):
        """ Get the asteroid speed """
        return self.x_y_sp

    def set_x_y_sp(self, new_sp_lc):
        """ Set new steroid speed """
        self.x_y_sp = new_sp_lc

    def get_x_y_loc(self):
        """ Get the asteroid location """
        return self.x_y_loc

    def set_x_y_loc(self, new_sp_lc):
        """ Set new asteroid location """
        self.x_y_loc = new_sp_lc

    def get_size(self):
        """ Get the asteroid size """
        return self.size

    def set_size(self, new_size):
        """ Set new asteroid size """
        self.size = new_size

    def get_radius(self):
        """ Get the asteroid radius"""
        return (self.size * 10) - 5

    def has_intersection(self, obj):
        """ Check whether the asteroid collided with another object"""
        x_obj, y_obj = obj.get_x_y_loc()
        x, y = self.get_x_y_loc()
        distance = math.sqrt((x_obj - x)**2 + (y_obj - y)**2)
        if distance <= self.get_radius() + obj.get_radius():
            return True
        return False
