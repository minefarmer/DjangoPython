# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# for i in range(0, 10):
#     print(i)    # 0
#                 # 1
#                 # 2
#                 # 3
#                 # 4
#                 # 5
#                 # 6
#                 # 7
#                 # 8
#                 # 9


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# for i in range(0, 11):
#     print(i)    # 0
#                 # 1
#                 # 2
#                 # 3
#                 # 4
#                 # 5
#                 # 6
#                 # 7
#                 # 8
#                 # 9
#                 # 10


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = len(l)
# print(a)  # 11

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = len(l)
# print(l[11])  # Traceback (most recent call last):
#                 # File "/home/carl/Github/DjangoPython/Django Python Class Notes/ListsIteration.py", line 36, in <module>
#                 #     print(l[11])  # 11
#                 # IndexError: list index out of range
                
                
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = len(l)
# print(l[10]) # 11

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = len(l)
# b = l[0:5]
# print(b)  # [1, 2, 3, 4, 5]


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = len(l)
# b = l[0::]
# print(b)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = len(l)
# b = l[0::2]
# for i in range(0, 10, 2):
#     print(i)  # 0
#             # 2
#             # 4
#             # 6
#             # 8


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = len(l)
# b = l[0::2]
# for i in range(0, 11, 2):
#     print(i)  # 0
#             # 2
#             # 4
#             # 6
#             # 8
#              10


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = len(l)
# b = l[-1:-4]
# print(b)  # []


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = len(l)
# b = l[10::-1]
# print(b)  # [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = len(l)
# l2 = ['navid', 'rich', 'carl', 'maryam']
# print(len(l2))  # ['navid', 'rich', 'carl', 'maryam']


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = len(l)
# l2 = ['navid', 'rich', 'carl', 'maryam']
# print(l2[0::])  # ['navid', 'rich', 'carl', 'maryam']


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = len(l)
# l2 = ['navid', 'rich', 'carl', 'maryam']
# print(l2[-1])  # maryam


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# a = len(l)
# l2 = ['navid', 'rich', 'carl', 'maryam']
# print(l2[-1][0])  # m


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
a = len(l)
l2 = ['navid', 'rich', 'carl', 'maryam']
b = l2[-1]
print(b[0])  # m