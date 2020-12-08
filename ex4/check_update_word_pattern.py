##############################################################
# FILE : check_update_word_pattern.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex4 2019
# DESCRIPTION: we asked to write function that check the function
# update_word_pattern
###############################################################
from hangman import update_word_pattern

def check_fu_update_word_pattern():

    """This function check the function update_word_pattern"""

    flag = [False, False, False, False, False]
    if update_word_pattern("hello", "_____", "l") == "__ll_":
        flag[0] = True

    if update_word_pattern("h", "_", "l") == "_":
        flag[1] = True

    if update_word_pattern("python", "______", "l") == "______":
        flag[2] = True

    if update_word_pattern("python", "______", "n") == "_____n":
        flag[3] = True

    if update_word_pattern("python", "python", "n") == "python":
        flag[4] = True

    if all(flag):
        print("Test succeed")
        return True
    else:
        print("Test failed")
        return False

if __name__ == "__main__":
    check_fu_update_word_pattern()