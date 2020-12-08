###################################################################
# FILE : car.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex9 2019
# DESCRIPTION: we asked to write the game rush hour using opp
# #################################################################

NAMES = ["Y", "B", "O", "W", "G", "R"]
ORIENTATION = [0, 1]
HORIZONTAL = 1
VERTICAL = 0


class Car:
    """
    This class create car object ,and has function that help get information on
     the car ,move the car and more"""

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """

        self.name = name
        self.length = length
        self.orientation = orientation
        self.location = location

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        list_of_coordinates = []
        car_location = self.location
        car_length = self.length
        car_orientation = self.orientation

        if car_orientation == VERTICAL:
            for i in range(car_length):
                locat_to_add = (car_location[0]+i, car_location[1])
                list_of_coordinates.append(locat_to_add)
        if car_orientation == HORIZONTAL:
            for i in range(car_length):
                locat_to_add = (car_location[0], car_location[1]+i)
                list_of_coordinates.append(locat_to_add)
        return list_of_coordinates

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        if self.orientation == VERTICAL:
            possible_direction = {"u": "cause the car vertical ",
                                  "d": "cause the car vertical "}
        else:
            possible_direction = {"r": "cause the car horizontal ",
                                  "l": "cause the car horizontal "}

        return possible_direction

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """

        possible_move = self.possible_moves()
        if movekey in possible_move:
            if self.orientation == VERTICAL:
                if movekey == "d":
                    last_cell_location = self.car_coordinates()[-1]
                    empty_cell_neede = [tuple([last_cell_location[0] + 1,
                                        last_cell_location[1]])]
                if movekey == "u":
                    last_cell_location = self.car_coordinates()[0]
                    empty_cell_neede = [tuple([last_cell_location[0] - 1,
                                        last_cell_location[1]])]
                return empty_cell_neede

            if self.orientation == HORIZONTAL:
                if movekey == "r":
                    last_cell_location = self.car_coordinates()[-1]
                    empty_cell_neede = [tuple([last_cell_location[0],
                                        last_cell_location[1] + 1])]
                if movekey == "l":
                    last_cell_location = self.car_coordinates()[0]
                    empty_cell_neede = [tuple([last_cell_location[0],
                                        last_cell_location[1] - 1])]
                return empty_cell_neede

        return False  # because direction is not valid

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """

        possible_move = self.possible_moves()
        if movekey in possible_move:
            old_location = self.location

            if self.orientation == VERTICAL:
                if movekey == "d":
                    self.location = [old_location[0] + 1,
                                      old_location[1]]
                if movekey == "u":
                    self.location = [old_location[0] - 1,
                                      old_location[1]]
            if self.orientation == HORIZONTAL:
                if movekey == "r":

                    self.location = [old_location[0],
                                     old_location[1] + 1]
                if movekey == "l":
                    self.location = [old_location[0],
                                     old_location[1] - 1]
            return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.name

