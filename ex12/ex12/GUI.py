#############################################################
# FILE : GUI.py
# WRITERs : Nir Amzaleg, Noa Moalem, nir_amzaleg, noamoa 206959686 ,208533554
# EXERCISE : intro2cs ex12 2019
# DESCRIPTION: This file contain the GUI class how responsible
# on the visual graphic of the 4 in a row game.
#############################################################

import tkinter as tk
from .ai import AI
from .game import Game


class Gui:
    """
    The GUI class how responsible on the visual graphic of the 4 in a row game
    """

    DIRECTIONS = {"down": (1, 0), "right": (0, 1),
                  "upright": (-1, 1), "downright": (1, 1)}
    WIN = 4
    COM_VS_HUMAN = 2
    COM_VS_COM = 4

    def __init__(self, game):

        self.game = game
        self.TURN_NUM = 0
        self.STOP_GAME = [0, 1, 2]
        self.ai_objects = []
        self.player1cor = []
        self.player2cor = []
        self.game_mode = self.entry_menu()  # Create entry menu
        self.ai_player_num = self.create_ai()

        # Create the board
        self.root = tk.Tk()
        self.root.wm_title("Four In A Row!")
        self.up_frame = tk.Frame(self.root, bg="#33adff")
        self.up_frame.grid(row=0, rowspan=5)
        self.down_frame = tk.Frame(self.root)
        self.down_frame.grid(columnspan=7, row=6)
        self.coor = self.create_sub_frames()
        self.col_buttons()

        if self.game_mode == Gui.COM_VS_HUMAN:
            self.button_pressed(self.ai_objects[0].find_legal_move())
        elif self.game_mode == Gui.COM_VS_COM:
            self.com_vs_com()
        self.root.protocol("WM_DELETE_WINDOW", exit)
        self.root.mainloop()

    def col_buttons(self):
        """ This function create the columns buttons that represent the
        user chose """
        b1 = tk.Button(self.down_frame, text="   0    ",font=("Helvetica", 18),
                       command=lambda: self.button_pressed(0), bg="#33ccff")
        b2 = tk.Button(self.down_frame, text="   1    ",font=("Helvetica", 18),
                       command=lambda: self.button_pressed(1), bg="#33ccff")
        b3 = tk.Button(self.down_frame, text="   2    ",font=("Helvetica", 18),
                       command=lambda: self.button_pressed(2), bg="#33ccff")
        b4 = tk.Button(self.down_frame, text="   3    ",font=("Helvetica", 18),
                       command=lambda: self.button_pressed(3), bg="#33ccff")
        b5 = tk.Button(self.down_frame, text="   4    ",font=("Helvetica", 18),
                       command=lambda: self.button_pressed(4), bg="#33ccff")
        b6 = tk.Button(self.down_frame, text="   5    ",font=("Helvetica", 18),
                       command=lambda: self.button_pressed(5), bg="#33ccff")
        b7 = tk.Button(self.down_frame, text="   6    ",font=("Helvetica", 18),
                       command=lambda: self.button_pressed(6), bg="#33ccff")
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)
        b4.grid(row=0, column=3)
        b5.grid(row=0, column=4)
        b6.grid(row=0, column=5)
        b7.grid(row=0, column=6)

    def button_pressed(self, button):
        """ This function update the Gui and the Game according to the
        user chose/ the Ai random chose """
        if len(self.coor[button])and self.game.get_winner() not in self.STOP_GAME:
            if self.check_how_play():
                canvas = self.coor[button][-1]
                canvas.create_oval(0, 0, 80, 80, fill=self.player_color())
                self.update_player_cor(len(self.coor[button])-1, button)
                self.coor[button].pop()
                try:
                    self.game.make_move(button)
                except:
                    if self.game.get_winner() in self.STOP_GAME:
                        self.game_over(self.game.get_winner())
                    else:
                        self.game_over(self.game.get_winner())
            if not self.check_how_play() and \
                    self.game.get_winner() not in self.STOP_GAME:
                button = self.ai_objects[0].find_legal_move()
                canvas = self.coor[button][-1]
                canvas.create_oval(0, 0, 80, 80, fill=self.player_color())
                self.update_player_cor(len(self.coor[button]) - 1, button)
                self.coor[button].pop()
                try:
                    self.game.make_move(button)
                except:
                    if self.game.get_winner() in self.STOP_GAME:
                        self.game_over(self.game.get_winner())
                    else:
                        self.game_over(self.game.get_winner())
        if self.game.get_winner() in self.STOP_GAME:
            self.game_over(self.game.get_winner())

    def update_player_cor(self, row, col):
        """ This function update the coordinate that chose in this turn """
        cor = row, col
        if self.game.get_current_player() == 1:
            self.player1cor.append(cor)
        else:
            self.player2cor.append(cor)

    def com_vs_com(self):
        """ This function run the game with 2 AI, and not user input """
        if not self.game.get_winner() in self.STOP_GAME:
            button = self.ai_objects[0].find_legal_move()
            canvas = self.coor[button][-1]
            canvas.create_oval(0, 0, 80, 80, fill=self.player_color())
            self.update_player_cor(len(self.coor[button]) - 1, button)
            self.coor[button].pop()
            try:
                self.game.make_move(button)
            except:
                if self.game.get_winner() in self.STOP_GAME:
                    self.game_over(self.game.get_winner())
                else:
                    self.game_over(self.game.get_winner())
            self.root.after(1000, self.com_vs_com)
        else:
            self.game_over(self.game.get_winner())

    def create_sub_frames(self):
        """ This function create the sub frames how represent
            the coordinates"""
        canvas_matrix = []
        for i in range(7):
            lst = []
            for j in range(6):
                canvas = tk.Canvas(self.root, bg="#33ccff", height=80, width=80)
                canvas.grid(row=j, column=i)
                canvas.create_oval(0, 0, 80, 80, fill="white")
                lst.append(canvas)
            canvas_matrix.append(lst)
        return canvas_matrix

    def player_color(self):
        """ Return the color of the current player """
        if self.game.get_current_player() == 1:
            return "#ff5050"
        return "#ffff66"

    def entry_menu(self):
        """ Create a pop up menu that ask the player which mode he chose """
        root = tk.Tk()
        root.wm_title("Entry Menu! please chose mode: ")
        root.protocol("WM_DELETE_WINDOW", exit)
        b1 = tk.Button(root, text="Play human against computer",
                       font=("Helvetica", 18), fg="red",
                       command=lambda: self.mode_change(1, root))
        b2 = tk.Button(root, text="Play computer against human",
                       font=("Helvetica", 18), fg="#ffcc00",
                       command=lambda: self.mode_change(2, root))
        b3 = tk.Button(root, text="Play human against human",
                       font=("Helvetica", 18), fg="green",
                       command=lambda: self.mode_change(3, root))
        b4 = tk.Button(root, text="Watch the computer playing",
                       font=("Helvetica", 18), fg="blue",
                       command=lambda: self.mode_change(4, root))

        b1.pack(side=tk.TOP)
        b2.pack(side=tk.TOP)
        b3.pack(side=tk.TOP)
        b4.pack(side=tk.TOP)
        self.TURN_NUM = 0
        root.mainloop()
        return self.GAME_MODE

    def mode_change(self, chose, root):
        """ Update the attribute game mode according to the entry menu """
        self.GAME_MODE = chose
        root.destroy()

    def check_coor_one_direction(self, coor, d_row, d_col, winner):
        """ this function check if there is 4 circle in a row according to
        given coordinate and direction"""
        row, col = coor
        lst = []
        if winner == 1:
            coor_lst = self.player1cor
        else:
            coor_lst = self.player2cor
        for i in range(Gui.WIN):
            new_coor = (row + i * d_row, col + i * d_col)
            if new_coor in coor_lst:
                    lst.append(new_coor)
        if len(lst) == Gui.WIN:
            return lst

    def find_winner_cor(self, coor, winner):
        """ This function check if there is 4 circle in a row according to
        given coordination and all direction"""
        for dir in Gui.DIRECTIONS:
            row = Gui.DIRECTIONS[dir][0]
            col = Gui.DIRECTIONS[dir][1]
            winner_coor = self.check_coor_one_direction(coor, row, col, winner)
            if winner_coor:
                return winner_coor

    def game_over(self, winner):
        """ This function been called if there is a winner or draw,
        it create the pop up window and call the function that bold the
        winning coordinates"""
        if winner == 0:
            msg = "Draw, no winner!"
            color = "black"
        elif winner == 1:
            msg = "Red won!"
            color = "#ff0000"
            self.bold_win()
        else:
            msg = "Yellow won!"
            color = "#ffff00"
            self.bold_win()
        popup = tk.Tk()
        popup.wm_title("Game over!")
        popup.protocol("WM_DELETE_WINDOW", exit)
        label = tk.Label(popup, text=msg, font=("Helvetica", 40, "bold"),
                         fg=color)
        label.pack(side="top")
        b1 = tk.Button(popup, text="Play Again",
                       font=("Helvetica", 18, "bold"),
                       command=lambda: self.play_again(popup))
        b2 = tk.Button(popup, text="Exit",
                       font=("Helvetica", 18),
                       command=lambda: self.exit_game(popup))
        b1.pack(side="top")
        b2.pack(side="top")
        popup.mainloop()

    def bold_win(self):
        """ This function bold the winning coordinates"""
        winner = self.game.get_winner()
        if winner == 1:
            lst = self.player1cor
        else:
            lst = self.player2cor
        for coor in lst:
            winner_coor = self.find_winner_cor(coor, winner)
            if winner_coor:
                break
        for canvas_coor in winner_coor:
            canvas = tk.Canvas(self.root, bg="#33ccff", height=80, width=80)
            canvas.grid(row=canvas_coor[0], column=canvas_coor[1])
            canvas.create_oval(0, 0, 80, 80, fill="#ff00ff")

    def exit_game(self, popup):
        """ This function destroy the gui root """
        popup.destroy()
        self.root.destroy()

    def play_again(self, popup):
        """ If the user cose to, it restart the Gui and the game """
        popup.destroy()
        self.root.destroy()
        game = Game()
        g = Gui(game)

    def create_ai(self):
        """ This function create AI player/s according to the chosen mode """
        lst = []
        if self.game_mode == 1:
            ai1 = AI(self.game, 2)
            self.ai_objects.append(ai1)
            lst.append(2)
        elif self.game_mode == 2:
            ai1 = AI(self.game, 1)
            self.ai_objects.append(ai1)
            lst.append(1)
        elif self.game_mode == 4:
            ai1 = AI(self.game, 1)
            ai2 = AI(self.game, 2)
            self.ai_objects.append(ai1)
            self.ai_objects.append(ai2)
            lst.append(1)
            lst.append(2)
        return lst

    def check_how_play(self):
        """ This function return False if it is the turn of the AI player """
        return not (self.game.get_current_player() in self.ai_player_num)

    def x_is_pressed(self):
        exit()

