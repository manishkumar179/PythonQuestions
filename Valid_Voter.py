# WAP to take input of age and check he is valid to vote or not

age=int(input("Enter the age: "))
if(age>=18):
    print("You are eligible to vote: " , age)
else:
    print("Not Eligible to Vote")
    print("You are elegible after ",18-age , " years")