#############################################################
#  FILE : shapes.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION: A program calculate the area of circle/rectangle/triangle
##############################################################

import math

def shape_area():
    """This function calculate the area of one of three shapes"""

    shape = int(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))
    # circle
    if shape == 1:
        redius = float(input())
        return redius ** 2 * (math.pi)
    # rectangle
    if shape == 2:
        side1 = float(input())
        side2 = float(input())
        return side1 * side2
    # triangle
    if shape == 3:
        triside = float(input())
        return (math.sqrt(3) * (triside**2)) / 4
    return None