#############################################################
#  FILE : check_largest_and_smallest.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION: A program that check the function largest and smallest
##############################################################

from largest_and_smallest import largest_and_smallest

def check_function_largandsmall():
    """This function check the function largest and smallest"""

    if largest_and_smallest(0, 0, 0)[0] == 0 and \
        largest_and_smallest(0, 0, 0)[1] == 0:
        if largest_and_smallest(-1, 2, -2)[0] == 2 and \
            largest_and_smallest(-1, 2, -2)[1] == -2:
            if largest_and_smallest(-1, -2, -3)[0] == -1 and \
                largest_and_smallest(-1, -2, -3)[1] == -3:
                if largest_and_smallest(-3, -2, -1.5)[0] == -1.5 and \
                        largest_and_smallest(-3, -2, -1.5)[1] == -3:
                    if largest_and_smallest(-5/2, -10/2, 15/2)[0] == 15/2 and \
                            largest_and_smallest(-5/2, -10/2, 15/2)[1] ==-10/2:
                        print("Function 4 test success")
                        return True
    print("Function 4 test fail")
    return False

if __name__ =="__main__":
    check_function_largandsmall()