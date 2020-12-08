#############################################################
#  FILE : calculate_mathematical_expression.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION: A program that calculate mathematical expression
##############################################################

def calculate_mathematical_expression(x, y, sing):
    """This function calculate simple mathematical expression"""
    if sing == "+":
        return x+y
    if sing == "*":
        return x*y
    if sing == "-":
        return x-y
    if y!= 0 and sing == "/":
        return x/y
    return None


def calculate_from_string(param = "x s y"):
    """This function calculate simple mathematical expression from string """
    L = param.split(" ")
    return calculate_mathematical_expression(float(L[0]), float(L[2]), L[1])