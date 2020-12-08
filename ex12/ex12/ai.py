#############################################################
# FILE : ai.py
# WRITERs : Nir Amzaleg, Noa Moalem, nir_amzaleg, noamoa 206959686 ,208533554
# EXERCISE : intro2cs ex12 2019
# DESCRIPTION: This file contain the AI class how responsible
# on the ai of the computer in 4 in a row game.
#############################################################
import random


class AI:
    """
    the AI class how responsible on the ai of the computer in 4 in a row game.
    """

    def __init__(self, game, player):
        self.game = game
        self.player = player

    def find_legal_move(self, timeout=None):
        """ This function chose random column for the computer player"""
        prev_col = set()
        while len(prev_col) < 7:
            col = random.randint(0, 6)
            for row in range(5, -1, -1):
                if not self.game.get_player_at(row, col):
                    return col
            prev_col.add(col)
        Exception("No possible AI moves")

    def get_last_found_move(self):
        pass
