
# Swap number in one line
"""
a =3
b = 4

print("Before swap")
print("a-> " ,a)
print("b-> " ,b)

a,b = b,a

print("After swap")
print("a-> " ,a)
print("b-> " ,b)

"""

# Swap function using third variable temp

"""
def swap(a, b):

    temp = a
    a = b
    b = temp

    return a, b

ans = swap(2,3)
print(ans)

"""



# Without using third variable

"""
def swapWithOutThirdVariable(a, b):

    a = a + b
    b = a - b
    a = a - b

    return a, b

ans = swapWithOutThirdVariable(2,3)
print(ans)

"""

# Another way using without third variable

def swapUsingBit(a, b):

    a = a ^ b
    b = a ^ b
    a = a ^ b

    return a, b

ans = swapUsingBit(2, 3)

print(ans)
