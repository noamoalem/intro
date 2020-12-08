#############################################################
# FILE : ex3.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex3 2019
# DESCRIPTION: we asked to write 9 function
##############################################################

def input_list():
    """This function creates list from the user input"""

    yourlist = []
    inlist = input()
    while inlist != "":
        yourlist.append(inlist)
        inlist = input()

    return yourlist


def concat_list(str_list):
    """This is function that turn a list to one string"""

    fullsting =""
    if str_list == []: # if list is empty
        return ""

    for i in range(len(str_list) - 1):
        fullsting += str_list[i] + " "
    for i in range(len(str_list) - 1, len(str_list)): #so there wont be
                                                     #widespace in the end
        fullsting += str_list[i]

    return fullsting


def maximum(num_list):
    """This function find the maximum between numbers in a list"""

    max = 0 #because all numbers in num_list >=0
    if num_list == []:
        return None

    # compere all the number in num_list to max and change the max if needed
    for i in num_list:
        if i >= max:
            max = i

    return max


def cyclic(lst1, lst2):
    """This function check if one list is cyclic permutations of the second"""

    if lst1 == [] and  lst2 == []: #both list empty
        return True

    if len (lst1) == len (lst2):
        for m in range (len (lst1)):
            for k in range (len (lst1)):
                if lst1 [k] != lst2 [(k + m) % len (lst1)]:
                    break
            else:
                return True
    return False


def seven_boom(n):
    """This is function that return the result of 7 boom game"""

    gameresult = []
    x = "boom"
    for i in range(1, n+1):
        if i % 7 == 0: #the number divisible in 7
            gameresult.append(x)
        elif "7" in str(i): #the number include 7
            gameresult.append(x)
        else:
            gameresult.append(str(i))

    return gameresult


def histogram(n, num_list):
    """This function find the histogram of list """

    histlist = []
    for i in range(n): #creats a list of n members = 0
        histlist.append(0)

    for i in range(0, n):
        for numinlist in num_list:
            if i == numinlist: #count how many tims number is in num_list
                histlist[i] += 1
    return histlist


def prime_factors(n):
    """This function find the prime factor of number"""

    lst_of_p_factors = [] #empty list that will includ the prime factors of n

    if n > 1:
        for i in range(2, n+1):
            while n % i == 0: # n divisible in i
                lst_of_p_factors.append(i)
                n = n/i

    return lst_of_p_factors


def cartesian(lst1, lst2):
    """This function creates a cartesian product from two lists,"""

    biglist = [] #the list that includ the small lists

    for i in lst1:
        for j in lst2:

            biglist.append([i, j])

    return biglist


def pairs(num_list, n):
    """This function find if num_list has two number that 1num+2num = n"""

    biglist = [] #the list that includ the small lists
    for i in num_list:
        for j in range(1, len(num_list)):
            #the next line check if there is two numbers in num_list=n
            # and if this cuple is already in biglist
            if (i + num_list[j] == n ) :
                if ([num_list[j], i] not in biglist and [i, num_list[j]]
                        not in biglist):

                    biglist.append([i, num_list[j]])
                    j += 1


    return biglist