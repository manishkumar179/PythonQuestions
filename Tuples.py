

# Tuple is immutable it means that we can not able to insert and replace value
tuple = (22, 'manish', 76, 12.4, 3)
# print(min(tuple))
# print(max(tuple))
# print(sum(tuple))

print(type(tuple))

print("Lenght of tuple:- " , len(tuple))

print(tuple[3])
a, b, c, d, e = tuple
print(a)
print(b)
print(e)




# Make list inside tuple

tupA = (2, 3, [3, 4, 5, 55])
print("Before changing the value: ", tupA)

# now we can change the value of list
tupA[2][3] = 99
print("After changing th evalue: ", tupA)

print(3 in tuple)
print(99 in tuple)

