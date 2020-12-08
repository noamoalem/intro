#############################################################
# FILE : four_in_a_row.py
# WRITERs : Nir Amzaleg, Noa Moalem, nir_amzaleg, noamoa 206959686 ,208533554
# EXERCISE : intro2cs ex12 2019
# DESCRIPTION: This file create  GUI object with Game()
# object how run the four in a row game in fact.
#############################################################
from ex12.GUI import Gui
from ex12.game import Game


if __name__ == '__main__':
    game = Game()
    g = Gui(game)
