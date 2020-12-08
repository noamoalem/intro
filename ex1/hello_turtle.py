#############################################################
#  FILE : ex1.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex1 2019
# DESCRIPTION: A program that draw three flowers
##############################################################

import turtle

def draw_petal():
    """
    This function draw petal
    """
    # These next lines draw a leaf
    turtle.circle(100, 90)
    turtle.left(90)
    turtle.circle(100, 90)


def draw_flower ():
    """
    This function draw flower
    """
    turtle.setheading(0)
    draw_petal()
    turtle.setheading(90)
    draw_petal()
    turtle.setheading(180)
    draw_petal()
    turtle.setheading(270)
    draw_petal()
    turtle.setheading(270)
    turtle.forward(250)


def draw_flower_advance():
    """
    This function draw flower and move the turtle left
    """
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():
    """
    This fuction draw three flowers
    """
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_advance()
    draw_flower_advance()
    draw_flower_advance()


if __name__ == "__main__" :
    draw_flower_bed()
    turtle.done