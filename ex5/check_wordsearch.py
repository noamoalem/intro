#################################################################
# FILE : wordsearch.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex5 2019
# DESCRIPTION: we asked to write function that check one of the function
# we built
# #################################################################
from wordsearch import find_diagonals_matrix

def check_function_find_diagonals_matrix():
    """This function check the function find_diagonals_matrix"""
    flag = [False, False, False, False]
    if find_diagonals_matrix(["a"]) == ([['a']], [['a']]):
        flag[0] = True
    if find_diagonals_matrix([]) == None:
        flag[1] = True
    if find_diagonals_matrix([["a","b","c"],
                              ["d","e","f"],
                              ["g","h","i"]]) == ([['a', 'e', 'i'], ['b', 'f'],
    ['c'], ['d', 'h'], ['g']], [['a'],['d', 'b'], ['g', 'e', 'c'],
                                ['h', 'f'], ['i']]):
        flag[2] = True
    if find_diagonals_matrix([["a","b","c"],
                              ["d","e","f"],
                              ["g","h","i"],
                              ["j","k","l"],
                              ["m","n","o"]]) == \
        ([['a', 'e', 'i'], ['b', 'f'], ['c'], ['d', 'h', 'l'],
        ['g', 'k', 'o'], ['j', 'n'], ['m']], [['a'], ['d', 'b'],
        ['g', 'e', 'c'], ['j', 'h', 'f'], ['m', 'k', 'i'], ['n', 'l'], ['o']]):
        flag[3] = True

    if all(flag):
        print("Test succeed")
        return True
    else:
        print("Test failed")
        return False

if __name__ == "__main__":
    check_function_find_diagonals_matrix()
