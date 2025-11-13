#https://github.com/anacruizp/Lab11-AR-SS.git
#Partner 1: Ana Ruiz
#Partner 2: Sandra Salkini
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b):
    return a + b
def subtract(a,b):
    return a - b
def mul(a,b):
    return a*b
def div(a,b):
    if a == 0:
        raise ZeroDivisonError("division by zero")
    return a/b
def logarithm(a,b):
     if a <= 0 or b <= 0 or b == 1:
         raise ValueError("invalid input")
     return math.log(b,a)
def exp(a,b):
    return a**b
def square_root(a):
    if a < 0:
        raise ValueError('Invalid input')
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)






