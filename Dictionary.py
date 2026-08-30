#Dictionary is the combination of key and value pair in which key must be unique
# We can say that key are set and value are list
dict1  = {
    "Name":"Manish",
    "Roll":30,
    "Class":"CSE-C",
    "Subject":"PCM",
    "Marks":89
}

print(dict1)

# How to  get/access data
print(dict1['Name'])
print(dict1['Marks'])

# Use .get() to access element

print(dict1.get("Subject"))
print(dict1.get('mark', 'not found'))

key = {'mani', 'navin', 'rahul'} #This is set
value = [22, 45, 94]     # This is list

dict2 = dict(zip(key, value))
print(dict2)


# We can delete the value of dict by pop

dict1.pop("Name")
print("After poping  ",dict1)

# We can also delete the value by using del
del dict1['Subject']
print("After poping subject ",dict1)

# Dictionary inside dictionary is possible and  list inside dictionary is also possible