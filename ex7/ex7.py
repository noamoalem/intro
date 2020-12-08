#################################################################
# FILE : ex7.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex7 2019
# DESCRIPTION: we asked to write 10 recursive function
# #################################################################

def print_to_n(n):
    """This function print the number from n to 1 in ascending order """

    if n < 1:  # if n is smaller then 1 we won't print anything & base case
        return
    print_to_n(n - 1)
    print(n)


def print_reversed(n):
    """This function print the number from 1 to n in descending order"""

    if n < 1:  # if n is smaller then 1 we won't print anything & base case
        return
    print(n)
    print_reversed(n - 1)


def check_prime(n, d):
    """This function find if n is a prime number """

    if n % d == 0:
        return False
    if n < d * d:  # check all divisors till sqrt
        return True  # because all numbers till sqrt of n not divides n

    return check_prime(n, d + 1)


def is_prime(n):
    """This function return true if a number is a prime number and false if
    it's not """

    if n <= 1:  # n is not a prime number
        return False
    if n == 2:
        return True

    return check_prime(n, 2)


def factorial(n):
    """This function calculate n!"""

    if n == 0:
        return 1

    return n * factorial(n - 1)


def exp_n_x(n, x):
    """This function calculate tne exponential function sum which is:
    ∑ x^i/x! """

    if n == 0:
        return 1
    else:
        return (x ** n / factorial(n)) + exp_n_x(n - 1, x)


def play_hanoi(hanoi, n, src, dest, temp):
    """This function run the game Tower of Hanoi"""
    if n <= 0:
        return

    play_hanoi(hanoi, n - 1, src, temp,
               dest)  # move n-1 disks from src to temp
    hanoi.move(src, dest)  # move the last disk from src to dest
    play_hanoi(hanoi, n - 1, temp, dest,
               src)  # move n-1 disks from temp to dest


def print_sequences_helper(char_list, n, combination):
    """This function receives a list of characters, and prints all possible
    combinations of characters in length of n with characters from the given
    list"""

    if n == 0:
        print("")
        return

    if n == 1:
        for i in char_list:
            print(i)
        return
    if len(combination) == n:
        print(combination)
        return
    elif len(combination) < n:
        for i in char_list:
            combination += i
            print_sequences_helper(char_list, n, combination)
            combination = combination[:-1]
        return


def print_sequences(char_list, n):
    """This function use the print_sequences_helper to prints all possible
     combinations of characters in length of n with characters from the given
     list"""

    return print_sequences_helper(char_list, n, "")


def print_no_repetition_sequences_helper(char_list, n, combination):
    """This function receives a list of characters to prints all possible
    combinations of characters in length of n with characters from the given
    list without repetition"""

    if n == 0:
        print("")
        return

    if n == 1:
        for i in char_list:
            print(i)
        return
    if len(combination) == n:
        print(combination)
        return
    elif len(combination) < n:
        for i in char_list:
            if i not in combination:  # so we won't have repetition
                combination += i
                print_no_repetition_sequences_helper(char_list, n, combination)
                combination = combination[:-1]
        return


def print_no_repetition_sequences(char_list, n):
    """This function use the print_no_repetition_sequences_helper to prints all
     possible combinations of characters in length of n with characters from
     the given list without repetition"""

    return print_no_repetition_sequences_helper(char_list, n, "")

print(print_no_repetition_sequences("012",2))
def parentheses_helper(n, open, close, str, final):
    """This function find all the balanced combinations of parentheses in len
    of n"""

    if n == 0:
        final.append("")
        return final

    if close == n:  # we have balanced combination
        final.append(str)
        return

    if open < n:  # we will not have more then n "("
        parentheses_helper(n, open + 1, close, str + "(", final)

    if open > close:  # we will have the same amout of "(" and ")"
        parentheses_helper(n, open, close + 1, str + ")", final)

    return final


def parentheses(n):
    """This function find all the balanced combinations of parentheses in len
    of n"""

    return parentheses_helper(n, 0, 0, "", [])


def up_and_right_helper(char_list, n, k, way):
    """This function prints all the ways to reach the (n, k) only by steps
    right or up"""
    if n+k == 0:
        print("")
        return
    if len(way) == n+k:
        print(way)
        return
    elif len(way) < n+k:
        for i in char_list:
            if i == "r":
                if way.count(i) < n:  # so we still need to go right
                    way += i
                    up_and_right_helper(char_list, n, k, way)
                    way = way[:-1]
            else:
                if way.count(i) < k:  # so we still need to go up
                    way += i
                    up_and_right_helper(char_list, n, k, way)
                    way = way[:-1]
        return


def up_and_right(n, k):
    """This function use the up_and_right_helper to prints all the ways to
    reach the (n, k) only by steps right or up"""

    return up_and_right_helper(["r", "u"], n, k, "")


def flood_fill(image, start):
    """This function fill the empty places on the board with *, according to
    the rules"""

    image[start[0]][start[1]] = "*"  # fill this place with *
    for i in ["d", "u", "r", "l"]:  # the direction we need to search in
        if i == "d":
            new_start = [start[0] + 1, start[1]]  # change the start position
            if image[new_start[0]][new_start[1]] == ".":
                # we need to fill this place
                flood_fill(image, new_start)  # call the function again to
                # fill this place and keep searching for places to fill
        if i == "u":
            new_start = [start[0] - 1, start[1]]
            if image[new_start[0]][new_start[1]] == ".":
                flood_fill(image, new_start)
        if i == "r":
            new_start = [start[0], start[1] + 1]
            if image[new_start[0]][new_start[1]] == ".":
                flood_fill(image, new_start)
        if i == "l":
            new_start = [start[0], start[1] - 1]
            if image[new_start[0]][new_start[1]] == ".":
                flood_fill(image, new_start)
