#############################################################
#  FILE : far_to_cel.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION: A program that convert fahrenheit to celsius
##############################################################

def convert_far_to_cel(far):
    """This function convert fahrenheit to celsius"""
    cel = (far-32) * (5/9)
    return cel