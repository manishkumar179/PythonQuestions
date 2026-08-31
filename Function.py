import math
# def  :- this keyword is used to make a function in python

# import  math
from math import sqrt,ceil,pow

def add(a, b):
    c = a + b
    print(c)


add(3,5)
add(3,5)
add(9,5)


def sub(x, y):
    ''' Subtract two value '''
    s = x - y
    return s

ans = sub(5,3)
print(ans)


# Squart of number using sqrt inbuilt function
def  squart(x):
    # ans = math.sqrt(x)
    ans = sqrt(x)
    return ans


result = squart(25)
print("Squart root of number is :- ", result)

def power(x,y):
    ans1 = pow(x,y)
    return ans1

result1 = power(5,3)
print("Power of x,and y:- ", result1)






