# Set:- Set is the unordered collection of unique value , represent using {}
# Set can containe any value number, char or string
# We can perform operations on set like - , union, intersection , &(common value in set),
# ^ :- print not common in set

set1 = {10, 20, 34, 44, 56,10, 20}
print("Set contain only unique value:- ", set1)
print(20 in set1)
print("Length of set:- ", len(set1) )
print("Type of set:- ", type(set1))

set2 = set('sjbdfeygrgbk')
set3 = set('iuirriebbf')

print("Set2:- ", set2)
print("Set3:- ", set3)
print("Set2 - set3 :- ", set2-set3)
print("Common value in these set Set2 & set3 :- ", set2 & set3)
print("Not Common value in these set Set2 ^ set3 :- ", set2 ^ set3)
