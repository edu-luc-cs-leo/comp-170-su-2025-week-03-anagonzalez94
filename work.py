# Code

## Diamond Shape
def draw_diamond(height: int):
    # to calculate the number of hashes and spaces, we need the function 2x+1
    for i in range(height):
        print(" " * (height - i), "#" * (2*i+1))
    for i in range(height -2, -1, -1):
        print(" " * (height - i), "#" * (2*i+1))

## Right Triangle
def draw_triangle(height: int):

## Compound Interest
def compound_interest(principal: int, interest: int, time: int):
    rate = interest / 100
    for i in range(time):


## Hollow Square