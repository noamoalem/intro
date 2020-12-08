#############################################################
#  FILE : stable_price.py
# WRITER : noa moalem , noamoa , 208533554
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION: A program that check if the price has change over 3 years
##############################################################

def is_it_stable(saf, price1, price2, price3):
    """This function check if the price has change over 3 years"""
    if price2-price1 < saf and price3-price2 < saf:
        return True
    return False
