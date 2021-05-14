# Input is a 2d array
# Output should be a 2d array in echelon 

# Input Structure: Final element on each row of 2-d array should be y
# all preceding elements shoud be xs
# Input elements must be integers biko
# To think of it, that shouldn't be necessary since na computer go dey do the multiplication and division
# computers don't handle fractions well sha



import numpy as np 
from fractions import Fraction

"""
class LinearEquation:

    def __init__(self, elements: list): 

        self.elements = [Fraction(x) for x in list]


    def __add__(self, other: LinearEquation): 
        return [x1 + x2  for x1, x2 in zip(self.elements, other.elements)]

    def __sub__(self, other: LinearEquation): 
        return [x1 - x2 for x1, x2 in zip(self.elements, other.elements)]

    def __mult__
# This is overkill for now. I could come back to implement this after prototyping with a simpler solution
"""

def add(x1: list, x2: list):
    if (len(x1) != len(x2)): 
        raise Exception()
    return [x1 + x2 for x1, x2 in zip(x1, x2)]

def sub(x1:list, x2:list): 
    if (len(x1) != len(x2)): 
        raise Exception()
    return [x1 - x2 for x1, x2 in zip(x1, x2)]

def mult(x1:list, const_val: Fraction)
    return [x * const_val for x in x1]

def div (x1:list, const_val: Fraction): 
    if (const_val == 0 ): 
        raise ZeroDivisionError()
    return mult(x1, 1/const_val)

def swap(equation: list, index1: int, index2: int): 
    # In a final implementation it may be more prudent to have a secondary structure for storing and manipulating order
    equation[index1], equation[index2] = equation[index2], equation[index1]


def find_first_non_zero(equation:list, var:int, start_index:int)
    for eq, idx in enumerate(equation[start_index:], start=start_index)
        if (eq[var] != 0): 
            return idx
    
    return -1 #dangerous since -1 is a valid index
    
def gaussian_reduce(equation: list):
     





