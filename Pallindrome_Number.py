n=int(input("Enter the number: "))
temp=n
rev=0
while(temp>0):
    t=temp%10
    rev=rev*10+t
    temp=temp//10


if(rev==n):
    print("Pallindrome Number ")
else:
    print("Not a Pallindrome number")
