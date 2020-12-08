NAMES = ["Y", "B", "O", "W", "G", "R"]
DIRECTION =["d", "u", "l", "r"]
possible_car_length = [2, 3, 4]
ORIENTATION = [0, 1]

from helper import *
from board import *
from car import *
import sys


def check_input( userinput):
    if len(userinput) != 3 or "," not in userinput:
        print("its not the right format")
        return False
    if userinput[0] not in NAMES:
        print("there is no such a car")
        return False
    if userinput[2] not in DIRECTION:
        print("unvalid direction")
        return False
    return True

class Game:
    """ This class create a game and drive the game """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board



    def __single_turn(self):
        """The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input"""

        print(self.board.__str__())  # print the board at first
        user_input = input("please enter car and direction: ")
        while not check_input(user_input):  # check the input valid
            user_input = input("please enter car and direction: ")
        if self.board.move_car(user_input[0], user_input[2]): #try move tha car
            print(self.board.__str__())

        print("car didn't move")
         # didn't move the car



    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """

        while self.board.board[self.board.target_location()[0]]\
                [self.board.target_location()[1]] == "E":  # the car didn't
                                                           # arrive the exit
            self.__single_turn()
        print("you won!")


if __name__ == "__main__":
    args = sys.argv
    board = Board()
    cars = load_json("car_config.json")
    for car in cars:
        if car in NAMES and cars[car][0] in possible_car_length and cars[car][2] \
                in ORIENTATION:
            car = Car(car, cars[car][0], cars[car][1], cars[car][2])
            board.add_car(car)
    game = Game(board)
    game.play()
