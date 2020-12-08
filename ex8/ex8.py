#################################################################
# FILE : ex8.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex8 2019
# DESCRIPTION: we asked to write the sudoku game , and 3 more function
# using backtracking
# #################################################################

import math
def solve_sudoku(board):
    """This function gets a sudoku board. if the sudoku as a sulotion it fill
    the board with it and return True, if it doesn't it return False"""

    n = len(board[0])
    lst_of_empty = ["row", "col"]

    if not find_if_empty_place(board, n, lst_of_empty):  # the board full
        return True

    #  find_if_empty_place(board,n)
    for i in range(1, n+1):
        if check_if_legal_place(board, lst_of_empty[0], lst_of_empty[1], i, n):
            # so we can put in this place the num i
            board[lst_of_empty[0]][lst_of_empty[1]] = i
            if solve_sudoku(board):  # try to continue solving the game
                return True          # the board full
            # we could not find a sulotion with i in this place ,backtrack
            board[lst_of_empty[0]][lst_of_empty[1]] = 0
    return False


def already_in_row(board, sudoku_row_number, num, n):
    """This function gets the sudoku row and check if the number is already
    somewhere in this row, if it dose it return true, else return false"""

    for i in range(n):
        if board[sudoku_row_number][i] == num:
            return True

    return False


def already_in_col(board, sudoku_col_number, num, n):
    """This function gets the sudoku row and check if the number is already
    somewhere in this col, if it dose it return true, else return false"""

    for i in range(n):
        if board[i][sudoku_col_number] == num:
            return True

    return False


def already_in_squr(board, sudoku_row_number, sudoku_col_number, num, n):
    """This function check if the number is already somewhere in this square,
     if it dose it return true, else return false"""

    row = sudoku_row_number // math.sqrt(n)
    col = sudoku_col_number // math.sqrt(n)
    # searching in the box that include sudoku_row_number,sudoku_col_number
    for i in range(int(row * int(math.sqrt(n))),
                   int(row * int(math.sqrt(n)) + int(math.sqrt(n)))):
        for j in range(int(col * int(math.sqrt(n))),
                       int(col * int(math.sqrt(n)) + int(math.sqrt(n)))):
            if board[i][j] == num:
                return True

    return False


def find_if_empty_place(board, n, lst_of_empty):
    """This function check if there is any empty place on the board, return
       True if there is """

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                lst_of_empty[0] = i
                lst_of_empty[1] = j
                return True
    else:
        return False


def check_if_legal_place(board, sudoku_row_number, sudoku_col_number, num, n):
    """This function check if we can put number in the place
    board [sudoku_row_number][sudoku_col_number], return True if we can."""

    if ((not already_in_row(board, sudoku_row_number, num, n)) \
    and (not already_in_col(board, sudoku_col_number, num, n)) \
    and (not already_in_squr(board, sudoku_row_number, sudoku_col_number, num,
                             n))):
        return True
    else:
        return False


def k_subset_helper(cur_set, k, index, picked):
    """This function change the cur_set array (put True in different index
       in cur_set) to create all the subset in size k of numbers from 0 to n-1
       and then call the function print_set with cur_set """

    if k == picked:  # base: we picked out k items
        print_set(cur_set)  # print the subset in size k of nums from 0 to n-1
        return

    if index == len(cur_set):  # If we reached the end of the list, backtrack
        return

    cur_set[index] = True  # Runs on all sets that include this index
    k_subset_helper(cur_set, k, index + 1, picked + 1)

    cur_set[index] = False  # Runs on all sets that do not include index
    k_subset_helper(cur_set, k, index + 1, picked)


def print_set(cur_set):
    """This function print lists of combination in size k of numbers from 0 to
       n - 1 according to the cur_set"""

    lst_of_one_combination = []  # create an empty list that will include the
                                 # current combination
    for (idx, in_cur_set) in enumerate(cur_set):  # fill the cur_set with
                                                  # numbers where its true
        if in_cur_set:
            lst_of_one_combination.append(idx)
    print(lst_of_one_combination)


def print_k_subsets(n, k):
    """This function use the k_subset_helper to print all the subset in size k
       of numbers from 0 to n - 1"""

    if k <= n:
        cur_set = [False] * n  # create a list of n lists
        k_subset_helper(cur_set, k, 0, 0)


def fill_k_subset_helper(cur_set, k, index, picked,lst):
    """This function change the cur_set array (put True in different index
        in cur_set) to create all the subset in size k of numbers from 0 to n-1
        and then call the function fill_lst with cur_set """

    if k == picked:  # base: we picked out k items
        fill_lst(cur_set, lst)
        return

    if index == len(cur_set):  # If we reached the end of the list, backtrack
        return

    cur_set[index] = True  # Runs on all sets that include this index
    fill_k_subset_helper(cur_set, k, index + 1, picked + 1, lst)

    cur_set[index] = False  # Runs on all sets that do not include index
    fill_k_subset_helper(cur_set, k, index + 1, picked, lst)


def fill_lst(cur_set, lst_of_all_combination=[]):
    """This function fill lst_of_all_combination with lists of combination in
    size k of numbers from 0 to n - 1 according to the cur_set. at the end we
    get that lst_of_all_combination include all the possible combination"""

    lst_of_one_combination = []  # create an empty list that will include the
                                 # current combination
    for (idx, in_cur_set) in enumerate(cur_set):
        if in_cur_set:  # fill the cur_set with
                        # numbers where its true
            lst_of_one_combination.append(idx)
    # adding the current combination to the big list
    lst_of_all_combination.append(lst_of_one_combination)


def fill_k_subsets(n, k, lst):
    """This function use the fill_k_subset_helper to fill a given empty list
    with all the subset in size k of numbers from 0 to n - 1"""

    if k <= n:
        cur_set = [False] * n
        fill_k_subset_helper(cur_set, k, 0, 0, lst)


def return_k_subsets(n, k):
    """This function return a list of all the subset in size k of numbers
       from 0 to n - 1"""

    if n < k or k < 0:
        return []
    if k == n:  # we left with only one option
        return [list(range(k))]

    lst_to_return = []
    for i in return_k_subsets(n - 1, k - 1):
        lst_to_return.append(i+[n-1])
    # recursive call for the function
    return return_k_subsets(n - 1, k) + lst_to_return