#############################################################
# FILE : check_maximum.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex3 2019
# DESCRIPTION: we asked to write function that check the function maximum
##############################################################

from ex3 import maximum

def check_function_maximum():
    """This function check the function maximum"""

    flag = [False, False, False, False, False]
    if not maximum([]): #empty list == False
        print("Test 1 succeed")
        flag[0] = True
    else:
        print("Test 1 failed")
    if maximum([0, 0, 0]) == 0:
        print("Test 2 succeed")
        flag[1] = True
    else:
        print("Test 2 failed")
    if maximum([1.5, 1.2, 1.49]) == 1.5:
        print("Test 3 succeed")
        flag[2] = True
    else:
        print("Test 3 failed")
    if maximum([5]) == 5:
        print("Test 4 succeed")
        flag[3] = True
    else:
        print("Test 4 failed")
    if maximum([1/2, 5/2, 5/3, 4/2]) == 5/2:
        print("Test 4 succeed")
        flag[4] = True
    else:
        print("Test 4 failed")


    if all(flag):
        return True
    return False


if __name__ =="__main__":
    check_function_maximum()