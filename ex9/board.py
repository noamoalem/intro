###################################################################
# FILE : board.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex9 2019
# DESCRIPTION: we asked to write the game rush hour using opp
# #################################################################

BOARD_ROW = 7
BOARD_COL = 7
ORIENTATION = [0, 1]
EXIT_ROW = 3
EXIT_COL = 7
VERTICAL = 0
HORIZONTAL = 1


class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        """built empty board (an array)"""

        self.cars = {}
        self.board = []
        self.create_empty_board()

    def create_empty_board(self):
        """This function create an empty board, that is array"""

        for i in range(BOARD_ROW):
            self.board.append([])

        for row in range(BOARD_ROW):
            if row != EXIT_ROW:
                for j in range(BOARD_COL):
                    self.board[row].append("*")
            if row == EXIT_ROW:
                for j in range(BOARD_COL + 1):
                    if j == EXIT_COL:
                        self.board[row].append("E")  # the target cell
                    elif j != EXIT_COL:
                        self.board[row].append("*")
        return self.board

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board ,* is empty place
        """
        str = ""
        for i in range(BOARD_ROW):
            if i != EXIT_ROW:
                for j in range(BOARD_COL):
                    str += self.board[i][j]
                    str += " "
                str += "\n"
            if i == EXIT_ROW:
                for j in range(BOARD_COL+1):
                    if j == 7:
                        str += self.board[i][j]
                        str += " "
                    elif j != 7:
                        str += self.board[i][j]
                        str += " "
                str += "\n"

        return str

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        list_of_coordinates = []
        for i in range(BOARD_ROW):
            for j in range(BOARD_COL):
                list_of_coordinates.append(tuple([i, j]))
                if i == 3 and j == 6:
                    list_of_coordinates.append(tuple([3, 7]))
        return list_of_coordinates

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
            representing legal moves"""
        res_list = []
        for car in self.cars:
            if car[2] == 0:
                res_list.append(tuple([car, "u", "cause the car vertical"]))
                res_list.append(tuple([car, "d", "cause the car vertical"]))

            res_list.append(tuple([car, "r", "cause the car horizontal"]))
            res_list.append(tuple([car, "l", "cause the car horizontal"]))

        return res_list

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return (EXIT_ROW, EXIT_COL)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """

        if coordinate[0] < BOARD_ROW and coordinate[1] < BOARD_COL+1:
            if self.board[coordinate[0]][coordinate[1]] == "*" or \
                    self.board[coordinate[0]][coordinate[1]] == "E":
                return None  # the cell is empty
        return self.board[coordinate[0]][coordinate[1]]

    def check_location_empty(self, car, location):
        """This function check if the location is empty so we could put there
        the car"""

        check_location_empty = []  # will be filled with True/False
        if car.orientation == VERTICAL:
            for i in range(car.length):
                if location[0]+i < BOARD_ROW:
                    if self.cell_content(tuple([location[0] + i,location[1]]))\
                            is None:  # this cell is empty
                        check_location_empty.append(True)
                    else:
                        check_location_empty.append(False)
        if car.orientation == HORIZONTAL:
            for i in range(car.length):
                if location[0] + i < BOARD_COL:
                    if self.cell_content(tuple([location[0],location[1] + i]))\
                            is None:  # this cell is empty
                        check_location_empty.append(True)
                    else:
                        check_location_empty.append(False)
        # the next line check if all the cells are empty by checking if
        # check_location_empty is filled with True only
        if len(check_location_empty)==car.length and all(check_location_empty):
            return True
        return False

    def add_car_helper(self, car):
        """This function put the letter of the car name on the board"""

        if car.orientation == VERTICAL:
            for i in range(car.length):
                self.board[car.location[0] + i][car.location[1]] = car.name
        if car.orientation == HORIZONTAL:
            for i in range(car.length):
                self.board[car.location[0]][car.location[1] + i] = car.name

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        if car.location[0] < 0 or car.location[1] < 0:
            return False
        if car.name in self.cars:
            return False
        if car.location[0] < BOARD_ROW and car.location[1] < BOARD_COL:
            if self.check_location_empty(car, car.location):
                self.cars[car.name] = car  # adding car to the dictionary cars
                self.add_car_helper(car)  # adding car to thr board
                return True
        return False

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        if name in self.cars:
            empty_place_needed = self.cars[name].movement_requirements(movekey)
            if not empty_place_needed:  # the car can't move in this move key
                return False
            if 0 <= empty_place_needed[0][0] < BOARD_ROW \
                    and self.cell_content(empty_place_needed[0]) is None:
                old_location = self.cars[name].car_coordinates()
                if empty_place_needed[0][0] == EXIT_ROW:
                    if 0 <= empty_place_needed[0][1] < BOARD_COL+1:
                        if self.cars[name].move(movekey):  # move in car
                            # the next lines delete the old car from the board
                            for i in old_location:
                                self.board[list(i)[0]][list(i)[1]] = "*"
                            # the next line adding the car in the new location
                            self.add_car_helper(self.cars[name])
                            return True
                        return False
                    return False

                elif 0 <= empty_place_needed[0][1] < BOARD_COL:
                    if self.cars[name].move(movekey):  # move in car
                        # the next lines delete the old car from the board
                        for i in old_location:
                            self.board[list(i)[0]][list(i)[1]] = "*"
                        # the next line adding the car in the new location
                        self.add_car_helper(self.cars[name])
                        return True
                return False
            return False
        return False
