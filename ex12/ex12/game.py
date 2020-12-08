#############################################################
# FILE : game.py
# WRITERs : Nir Amzaleg, Noa Moalem, nir_amzaleg, noamoa 206959686 ,208533554
# EXERCISE : intro2cs ex12 2019
# DESCRIPTION: This file contain the Game class how responsible
# on the 4 in a row logical. In addition, we chose to create assist class
# Board how responsible on the coordinate and the order in the board.
#############################################################


class Game:
    """
    The Game class how responsible on the 4 in a row logical
    """

    BOARD_SIZE = (6, 7)
    PLAYER1 = 1
    PLAYER2 = 2
    WIN = 4
    DIRECTIONS = {"down": (1, 0), "right": (0, 1),
                  "upright": (-1, 1), "downright": (1, 1)}
    STOP_GAME = [0, 1, 2]

    def __init__(self):
        self.board = Board()
        self.TURN_NUM = 0

    def make_move(self, column):
        """ This function play the current move according to given column """
        if column != -1:
            winner = self.get_winner()
            new_coor = self.board.col_to_coor(column)
            if not new_coor or winner in Game.STOP_GAME:
                raise Exception("Illegal move")
            else:
                self.board.update_player_coord(new_coor,
                                               self.get_current_player())
                self.TURN_NUM += 1

    def get_winner(self):
        """ This function check whether one of the players won """
        for coor in self.board.coord:
            winner = self.check_all_directions(coor)
            if winner:
                return winner
        if self.draw_check():
            return 0
        else:
            return

    def check_coor_one_direction(self, coor, d_row, d_col):
        """ This function check whether one of the players won in
         given coordination and direction"""
        row, col = coor
        player = self.get_player_at(row, col)
        lst = []
        for i in range(0, Game.WIN):
            new_coor = (row + i*d_row, col + i*d_col)
            if new_coor not in self.board.coord:
                return
            if player == Game.PLAYER1:
                if new_coor in self.board.player1_coord:
                    lst.append(new_coor)
            if player == Game.PLAYER2:
                if new_coor in self.board.player2_coord:
                    lst.append(new_coor)
            if not player:
                return
        if len(lst) == Game.WIN:
            return player

    def check_all_directions(self, coor):
        """ This function check whether one of the players won in
         given coordination and all direction"""
        for dir in Game.DIRECTIONS:
            row = Game.DIRECTIONS[dir][0]
            col = Game.DIRECTIONS[dir][1]
            winner = self.check_coor_one_direction(coor, row, col)
            if winner:
                return winner
        return

    def draw_check(self):
        """ This function check whether there is draw """
        for coor in self.board.coord:
            if coor not in self.board.player1_coord and \
             coor not in self.board.player2_coord:
                return False
        return True

    def get_player_at(self, row, col):
        """ This function return the player how chose this coordination"""
        if (row, col) in self.board.player1_coord:
            return Game.PLAYER1
        elif (row, col) in self.board.player2_coord:
            return Game.PLAYER2
        elif (row, col) in self.board.coord:
            return
        else:
            raise Exception("illegal location")

    def get_current_player(self):
        """ This function return the current player in this time"""
        if self.TURN_NUM % 2 == 0:
            return self.PLAYER1
        return self.PLAYER2

    def update_turn(self):
        """ Update the turn number"""
        self.TURN_NUM += 1
        return


class Board:
    """
    We chose to create assist class Board how responsible on
    the coordinate and the order in the board.
    """

    def __init__(self):
        self.row_size = Game.BOARD_SIZE[0]
        self.col_size = Game.BOARD_SIZE[1]
        self.coord = self.create_all_coor()
        self.player1_coord = []
        self.player2_coord = []

    def create_all_coor(self):
        """ Create list of all the coordinates of the board"""
        lst_of_coord = []
        for row in range(self.row_size):
            for col in range(self.col_size):
                lst_of_coord.append((row, col))
        return lst_of_coord

    def update_player_coord(self, coord, player):
        """ Update the list of each player """
        if player == Game.PLAYER1:
            self.player1_coord.append(coord)
        elif player == Game.PLAYER2:
            self.player2_coord.append(coord)
        return

    def col_to_coor(self, col):
        """ Gets the user input and return the chosen coordinate,
         if every row is taken return None"""
        taken_rows = []
        if 0 <= col <= 6:
            for coord in self.player1_coord:
                if coord[1] == col:
                    taken_rows.append(coord[0])
            for coord in self.player2_coord:
                if coord[1] == col:
                    taken_rows.append(coord[0])
            if taken_rows:
                row = min(taken_rows)
                if row == 0:
                    return
                return row - 1, col
            else:
                return self.row_size - 1, col
        return
