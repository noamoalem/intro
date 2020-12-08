#############################################################
#  FILE :  largest_and_smallest.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION: A program that give the largest and smallest between three
# numbers
##############################################################

def largest_and_smallest(x, y, z):
    """This function give the largest and smallest between three numbers"""

    if x >= y and x >= z: # x max
        if y >= z:
            smallest = z
        else:
            smallest = y
        largest=x
    elif y >= x and y >= z: #y max
        if x >= z:
            smallest = z
        else:
            smallest = x
        largest = y
    else: # z max
        if x >= y:
            smallest = y
        else:
            smallest = x
        largest = z
    return largest, smallest