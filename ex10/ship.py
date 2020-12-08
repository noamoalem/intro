#############################################################
# FILE : ship.py
# WRITER : nir_amzaleg & noamoa , Nir Amzaleg & Noa Moalem,
# 206959686, 208533554
# EXERCISE : intro2cs ex10 2019
# DESCRIPTION: Ship class. In this class the objects is a space ship.
#  Each one has location, speed, direction, radius and life.
#############################################################


class Ship:
    """ In this class the objects is a space ship.
    Each one has location, speed, direction, radius and life"""

    def __init__(self, x_y_sp, x_y_loc, direction):

        self.x_y_sp = x_y_sp
        self.x_y_loc = x_y_loc
        self.dir = direction
        self.radius = 1
        self.life = 3

    def get_x_y_sp(self):
        """ Get the ship speed """
        return self.x_y_sp

    def set_x_y_sp(self, new_sp_lc):
        """ Set new ship speed """
        self.x_y_sp = new_sp_lc

    def get_x_y_loc(self):
        """ Get the ship location """
        return self.x_y_loc

    def set_x_y_loc(self, new_sp_lc):
        """ Set new ship location """
        self.x_y_loc = new_sp_lc

    def get_dir(self):
        """ Get the ship direction """
        return self.dir

    def set_dir(self, new_dir):
        """ Set new ship direction """
        self.dir = new_dir

    def get_radius(self):
        """ Get the ship radius """
        return self.radius

    def lose_life(self):
        """ Remove one life from the ship"""
        self.life -= 1
