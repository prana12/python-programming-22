#import math
from math import sqrt

def hypotenuse(leg1: float, leg2: float):
    #print(dir(math))
    squares = leg1*leg1 + leg2*leg2
    return sqrt(squares)

if __name__ == "__main__":
    print(hypotenuse(3,4)) # 5.0
    print(hypotenuse(5,12)) # 13.0
    print(hypotenuse(1,1)) # 1.4142135623730951