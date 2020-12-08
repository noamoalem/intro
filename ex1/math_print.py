#############################################################
#  FILE : ex1.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex1 2019
# DESCRIPTION: A program that print to screen six calculations and word
##############################################################


import math

def golden_ratio():
    """
    This function print the golden ratio
    """
    print((1+math.sqrt(5))/2)


def six_cubed():
    """
    This function print 6**3
    """
    print(math.pow(6,3))


def hypotenuse():
    """
    This function print the length of hypotenuse in a right triangle
    """
    print(math.sqrt(5**2 +3**2))


def pi():
    """
    This function print the number pi
    """
    print(math.pi)


def e():
    """
    This function print the number e
    """
    print(math.e)


def triangular_area():
    """
    This function print the area of isosceles triangle
    """
    print(1*1/2, 2*2/2, 3*3/2, 4*4/2, 5*5/2, 6*6/2, 7*7/2, 8*8/2, 9*9/2,
          10*10/2)





if __name__ == "__main__":
    golden_ratio()
    six_cubed()
    hypotenuse()
    pi()
    e()
    triangular_area()
