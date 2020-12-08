#############################################################
#  FILE : quadratic_equation.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION: A program that solve quadratic equation
##############################################################

import math

def quadratic_equation(a, b, c):
    """This function solve quadratic equation"""
    insroot = pow(b, 2) - 4 * a * c
    if insroot < 0:
        return None, None
    elif insroot == 0:
        res = (-b) / 2 * a
        return None, res
    else:
        res1 = (-b + (math.sqrt(insroot))) / (2 * a)
        res2 = (-b - (math.sqrt(insroot))) / (2 * a)
        return res1, res2


def quadratic_equation_user_input():
    """This function get three number and solve quadratic equation"""

    list = str(input("Insert coefficients a, b, and c: ")).split()
    a = float(list[0])
    b = float(list[1])
    c = float(list[2])

    x = quadratic_equation(a,b,c)
    if x[0] == None and x[1]== None:
        print("The equation has no solutions")
    elif x[0] == None and x[1]!=None:
        print("The equation has 1 solution:",x[1])
    else:
        print("The equation has 2 solutions:", x[0], "and", x[1])

print(quadratic_equation(2,26,72))