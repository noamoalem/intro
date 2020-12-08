#############################################################
# FILE : asteroid_main.py
# WRITER : nir_amzaleg & noamoa , Nir Amzaleg & Noa Moalem,
# 206959686, 208533554
# EXERCISE : intro2cs ex10 2019
# DESCRIPTION: GameRunner class. In this class the objects is asteroid game.
# Each one has Screen, Ship, some Asteroids and Torpedos.
#############################################################


from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
import sys
import random
import math

DEFAULT_ASTEROIDS_NUM = 5
STRT_SPEED = 0
START_DIR = 0
ROUND = 360
AST_SIZE = 3
SCORE = {3: 20,
         2: 50,
         1: 100,
         0: 500}  # score of special shoot
MAX_TORPEDO = 10


class GameRunner:
    """GameRunner class. In this class the objects is asteroid game.
        Each one has Screen, Ship, some Asteroids and Torpedos."""

    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        self.asteroids_list = []
        self.torpedo_list = []
        self.score = 0
        self.special_shoot_list = []
        self.__ship = self._create_ship()
        self._create_asteroids(asteroids_amount)
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        self._game_loop()
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """ This is the main function. its present the current turn """
        self._ship_game_loop()
        self._asteroid_game_loop()
        self.__screen.draw_ship(self.__ship.get_x_y_loc()[0],
                                self.__ship.get_x_y_loc()[1],
                                self.__ship.get_dir())
        self.may_create_torpedo()
        self._torpedo_game_loop()
        self._lose_life_torpedo()
        self._check_whether_game_end()
        self._teleport()
        self._special_shoot()

    def _create_ship(self):
        """ This function create a Ship object in random place on the screen"""
        x = random.randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
        y = random.randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
        ship = Ship((STRT_SPEED, STRT_SPEED), (x, y), START_DIR)
        self.__screen.draw_ship(x, y, START_DIR)
        return ship

    def _move_object(self, object):
        """ This function move object (ship, asteroid or torpedo)
            on the screen"""
        x, y = object.get_x_y_loc()
        x_sp, y_sp = object.get_x_y_sp()
        x_new = (x_sp + x - self.__screen_min_x) \
            % (self.__screen_max_x - self.__screen_min_x) + self.__screen_min_x
        y_new = (y_sp + y - self.__screen_min_y) \
            % (self.__screen_max_y - self.__screen_min_y) + self.__screen_min_y
        object.set_x_y_loc((x_new, y_new))

    def _change_direction(self):
        """ Changes the ship direction according to the user input """
        if self.__screen.is_left_pressed():
            self.__ship.set_dir((self.__ship.get_dir() + 7) % ROUND)
        if self.__screen.is_right_pressed():
            self.__ship.set_dir((self.__ship.get_dir() - 7) % ROUND)

    def _accelerate_ship(self):
        """ Changes the ship speed according to the user input """
        if self.__screen.is_up_pressed():
            x_sp, y_sp = self.__ship.get_x_y_sp()
            cur_dir = self.__ship.get_dir()
            new_x = x_sp + math.cos(math.radians(cur_dir))
            new_y = y_sp + math.sin(math.radians(cur_dir))
            self.__ship.set_x_y_sp((new_x, new_y))

    def _ship_game_loop(self):
        """ Responsible to the changes of the ship in each loop """
        self._change_direction()
        self._accelerate_ship()
        self._move_object(self.__ship)

    def _asteroid_game_loop(self):
        """ Responsible to the changes of the asteroid in each loop """
        for asteroid in self.asteroids_list:
            self._move_object(asteroid)
            x, y = asteroid.get_x_y_loc()
            self.__screen.draw_asteroid(asteroid, x, y)
            if asteroid.has_intersection(self.__ship):
                self.__ship.lose_life()
                self.__screen.show_message("COLLISION", "You collided with "
                                                        "asteroid")
                self.__screen.remove_life()
                self.__screen.unregister_asteroid(asteroid)
                self.asteroids_list.remove(asteroid)

    def _asteroid_start_location(self):
        """ Chose random place on the screen for the new asteroid"""
        x = random.randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
        y = random.randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
        while x == self.__ship.get_x_y_loc()[0] and \
                y == self.__ship.get_x_y_loc()[1]:
            x = random.randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
            y = random.randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
        return x, y

    def _asteroid_speed(self):
        """ Chose random speed for the new asteroid"""
        x = random.randint(-4, 4)
        while x == 0:
            x = random.randint(-4, 4)
        return x

    def _create_asteroids(self, amount):
        """ Create some new asteroids, according to the amount that given,
             with random speed and location"""
        for i in range(amount):
            x, y = self._asteroid_start_location()
            x_sp, y_sp = self._asteroid_speed(), self._asteroid_speed()
            asteroid = Asteroid((x_sp, y_sp), (x, y), AST_SIZE)
            self.__screen.register_asteroid(asteroid, AST_SIZE)
            x, y = self._asteroid_start_location()
            self.__screen.draw_asteroid(asteroid, x, y)
            self.asteroids_list.append(asteroid)

    def may_create_torpedo(self):
        """ Create new torpedo, according to the user input
            (if space pressed)"""

        if self.__screen.is_space_pressed() and \
                len(self.torpedo_list) < MAX_TORPEDO:
            torpedo = Torpedo(self._torpedo_speed(), self.__ship.get_x_y_loc(),
                              self.__ship.get_dir())
            self.torpedo_list.append(torpedo)
            self.__screen.register_torpedo(torpedo)
            self.__screen.draw_torpedo(torpedo, torpedo.get_x_y_loc()[0],
                                       torpedo.get_x_y_loc()[1],
                                       torpedo.get_dir())

    def _torpedo_speed(self):
        """ Calculate the torpedo speed according to the ship
            speed and direction"""
        x, y = self.__ship.get_x_y_sp()
        x_sp = x + 2 * math.cos(math.radians(self.__ship.get_dir()))
        y_sp = x + 2 * math.sin(math.radians(self.__ship.get_dir()))
        return x_sp, y_sp

    def _split_asteroid(self, asteroid, torpedo):
        """ Create 2 new smaller asteroids, according to torpedo intersection,
            and removing the old asteroid """
        if asteroid.get_size() == 1:
            self.asteroids_list.remove(asteroid)
            self.__screen.unregister_asteroid(asteroid)
        else:
            ast1 = Asteroid(self._splited_asteroud_speed(asteroid, torpedo, 1),
                            asteroid.get_x_y_loc(), (asteroid.get_size() - 1))
            as2 = Asteroid(self._splited_asteroud_speed(asteroid, torpedo, -1),
                           asteroid.get_x_y_loc(), (asteroid.get_size() - 1))
            self.__screen.register_asteroid(ast1, ast1.get_size())
            self.__screen.register_asteroid(as2, as2.get_size())
            self.asteroids_list.append(ast1)
            self.asteroids_list.append(as2)
            self.asteroids_list.remove(asteroid)
            self.__screen.unregister_asteroid(asteroid)

    def _splited_asteroud_speed(self, asteroid, torpedo, dir):
        """ Calculate the speed of the 2 new smaller asteroids """
        x, y = asteroid.get_x_y_sp()
        x_sp = (dir * x + torpedo.get_x_y_sp()[0])/math.sqrt(x**2 + y**2)
        y_sp = (dir * y + torpedo.get_x_y_sp()[1]) / math.sqrt(x ** 2 + y ** 2)
        return x_sp, y_sp

    def _lose_life_torpedo(self):
        """ Check whether the Torpedo should disappear """
        for torpedo in self.torpedo_list:
            if torpedo.get_life() == 0:
                self.torpedo_list.remove(torpedo)
                self.__screen.unregister_torpedo(torpedo)
            else:
                torpedo.lose_life()

    def _torpedo_game_loop(self):
        """ Responsible to the changes of the torpedo in each loop """
        for torpedo in self.torpedo_list:
            self._move_object(torpedo)
            x, y = torpedo.get_x_y_loc()
            self.__screen.draw_torpedo(torpedo, x, y, torpedo.get_dir())
            for asteroid in self.asteroids_list:
                if asteroid.has_intersection(torpedo):
                    self.score += SCORE[asteroid.get_size()]
                    self.__screen.set_score(self.score)
                    self._split_asteroid(asteroid, torpedo)

    def _check_whether_game_end(self):
        """ Check whether the game should end """
        flag = False
        if len(self.asteroids_list) == 0:
            self.__screen.show_message("Congratulations", "You won, no more " 
                                                          "asteroids")
            flag = True
        if self.__ship.life == 0:
            self.__screen.show_message("Game over!", "no more life")
            flag = True
        if self.__screen.should_end():
            self.__screen.show_message("End of the game", "You choose to exit")
            flag = True
        if flag:
            self.__screen.end_game()
            sys.exit()

    def _teleport(self):
        """ Check whether the user chose to teleport the ship, And teleport
        it if the user did """
        asteroid_locations_list = []
        if self.__screen.is_teleport_pressed():
            x = random.randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
            y = random.randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
            for asteroid in self.asteroids_list:
                asteroid_locations_list.append(asteroid.get_x_y_loc())
            while (x, y) in asteroid_locations_list:
                x = random.randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
                y = random.randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
            self.__ship.set_x_y_loc((x, y))

    def _special_shoot(self):
        """ The main function of the special shoot, create it and
         Responsible to the changes of the special shoot in each loop  """
        if self.__screen.is_special_pressed() and \
         len(self.special_shoot_list) < 5:
            torpedo1 = Torpedo(self._special_shoot_speed(0),
                               self.__ship.get_x_y_loc(),
                               self.__ship.get_dir())
            torpedo2 = Torpedo(self._special_shoot_speed(-30),
                               self.__ship.get_x_y_loc(),
                               self.__ship.get_dir() - 30)
            torpedo3 = Torpedo(self._special_shoot_speed(30),
                               self.__ship.get_x_y_loc(),
                               self.__ship.get_dir() + 30)
            one_shoot = [torpedo1, torpedo2, torpedo3]
            self.special_shoot_list.append(one_shoot)
            for torpedo in one_shoot:
                self.__screen.register_torpedo(torpedo)
        self._special_shoot_life()
        self._draw_special_shoot()
        self._special_shoot_intersection()

    def _special_shoot_life(self):
        """ Check whether the special shoot should disappear """
        for special_shoot in self.special_shoot_list:
            if special_shoot[0].life == 50:
                for torpedo in special_shoot:
                    self.__screen.unregister_torpedo(torpedo)
                self.special_shoot_list.remove(special_shoot)
            else:
                special_shoot[0].life -= 1

    def _special_shoot_speed(self, heading):
        """ Calculate the special shoot speed according to the ship
             speed and direction"""
        x, y = self.__ship.get_x_y_sp()
        x_sp = x + 2 * math.cos(math.radians(self.__ship.get_dir() + heading))
        y_sp = x + 2 * math.sin(math.radians(self.__ship.get_dir() + heading))
        return x_sp, y_sp

    def _draw_special_shoot(self):
        """ Draw the special shoot on the screen"""
        for special_shoot in self.special_shoot_list:
            for torpedo in special_shoot:
                self._move_object(torpedo)
                self.__screen.draw_torpedo(torpedo, torpedo.get_x_y_loc()[0],
                                           torpedo.get_x_y_loc()[1],
                                           torpedo.get_dir())

    def _special_shoot_intersection(self):
        """ Check whether the special shoot collided with asteroid and
        destroyed it"""
        for asteroid in self.asteroids_list:
            for special_shoot in self.special_shoot_list:
                for torpedo in special_shoot:
                    if asteroid.has_intersection(torpedo):
                        self.score += SCORE[0]
                        self.__screen.set_score(self.score)
                        self.asteroids_list.remove(asteroid)
                        self.__screen.unregister_asteroid(asteroid)


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
