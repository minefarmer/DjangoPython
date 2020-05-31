# More about lists 55
# 
# 


list_1 = ['carl', 'ali', 'john', 'maryam']

# print(list_1)  # ['carl', 'ali', 'john', 'maryam']
# print(list_1[0])  # carl


# d = list_1[0]
# a = list_1[1]
# b = list_1[2]
# c = list_1[3]
# print(a, b, c, d)  # ali john maryam carl


# a = list_1[0]
# a = a.title()
# print(a)  # carl


# a = list_1[1]
# b = list_1[-1]
# c = list_1[-2]
# print(b)  # maryam
# print(c)  # john


#  adding elements to the list

# checking how many elements are in the list.
# print(len(list_1))  # 4

#  adding to the list
# list_1.append('car')
# print(list_1)  # ['carl', 'ali', 'john', 'maryam', 'car']

# list_1.insert(0, 'car')
# print(list_1)  # ['car', 'carl', 'ali', 'john', 'maryam', 'car']

# list_1.insert(2, 'car')
# print(list_1)  # 'car', 'carl', 'car', 'ali', 'john', 'maryam', 'car']

#  removing from the list
list_1.remove('carl')
print(list_1)  # ['ali', 'john', 'maryam']
a = list_1.pop(0)
print(list_1)  # ['john', 'maryam']
print(a)  # ali



# More about lists 55
>>> l = [1]
>>> l
[1]
>>> l[:0] = [2, 3, 4]
>>> l
[2, 3, 4, 1]
>>> 