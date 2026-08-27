
list = [23, 45, 55, 60]
ans = list.count(23)
print(ans)

# Add value to list (append: add element at last)
print("After add element to last:-")
list.append(33)
print(list)

# Insert value at specific location (insert: insert the element)
print("After insert operation:- ")
list.insert(1,49)
print(list)

# Remove element using the value(remove: use value to remove the element)
print("After removing 23 from list:- ")
list.remove(23)
print(list)

# Remove the element from the index (pop(index) :- used to remove the value using index)
print("After removing the element at index 2 ")
list.pop(2)
print(list)

# list.pop() :- It can remove the last element from the list

# How to remove multiple element from the list

print("After removing multiple element from index 1 and 2: ")
del list[1:3]
print(list)


# Insert multiple value in list (extend([value] : add multiple element into list)

print("After adding multiple value in list using extend ")
list.extend([34, 44, 66, 46, 22, 40])
print(list)

# Replace the value in list
print("After replacing the value of index 2 and 3 from 90 and 80")
list[2:4] = [90,80]
print(list)

# We can reverse the list using reverse function of list
# Use sort to sort the element

list.reverse()
print("Reverse the list :-  " , list)
list.sort()
print("Sort the list :-  " , list)

# min(list),max(list),sum(list) = used to find min, max and sum of list
print("Min:- " , min(list))
print("Max:- " , max(list))
print("Sum:- " , sum(list))

list[2] = 999
print(list)

print("Length of list: ", len(list))
print(80 in list)


