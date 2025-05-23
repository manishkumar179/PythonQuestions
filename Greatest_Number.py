# WAP to find the greatest among three numbers
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))

great = a
if b > great:
    great = b
if c > great:
    great = c

print("Greatest number between a,b and c is : " , great)