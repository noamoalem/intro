#############################################################
# FILE : torpedo.py
# WRITER : nir_amzaleg & noamoa , Nir Amzaleg & Noa Moalem,
# 206959686, 208533554
# EXERCISE : intro2cs ex10 2019
# DESCRIPTION: torpedo class. In this class the objects is a torpedo.
#  Each one has location, direction. radius and life.
#############################################################


class Torpedo:
    """ Torpedo class. In this class the objects is a torpedo.
        Each one has location, direction. radius and life."""

    def __init__(self, x_y_sp, x_y_loc, direction):
        self.x_y_sp = x_y_sp
        self.x_y_loc = x_y_loc
        self.dir = direction
        self.radius = 4
        self.life = 200

    def get_x_y_sp(self):
        """ Get the torpedo speed """
        return self.x_y_sp

    def set_x_y_sp(self, new_sp_lc):
        """ Set new torpedo speed """
        self.x_y_sp = new_sp_lc

    def get_x_y_loc(self):
        """ Get the torpedo location"""
        return self.x_y_loc

    def set_x_y_loc(self, new_sp_lc):
        """ Set new torpedo location """
        self.x_y_loc = new_sp_lc

    def get_dir(self):
        """ Get the torpedo direction"""
        return self.dir

    def set_dir(self, new_dir):
        """ Set new torpedo direction """
        self.dir = new_dir

    def get_radius(self):
        """ Get the torpedo radius"""
        return self.radius

    def get_life(self):
        """ Get the torpedo life"""
        return self.life

    def lose_life(self):
        """ Remove one life from the torpedo """
        self.life -= 1
