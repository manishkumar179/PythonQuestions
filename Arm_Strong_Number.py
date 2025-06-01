n = int(input("Enter the number: "))

# Change num variable to string,
# and calculate the length (number of digit)

order = len(str(n))

temp = n
ans = 0
while (temp != 0):
    rem = temp % 10
    ans = ans + rem ** order
    temp //= 10

if (n == ans):
    print("Armstrong number")
else:
    print("not")
