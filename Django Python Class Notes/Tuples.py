# a = ();print((type(a)))  # <class 'tuple'>

users = ('rich', 'carl', 'root' 'administrator', 'public')
# print(type(users))  # <class 'tuple'>

# print(users[0])  # rich

# print(users.index('rich'))  # 0

# users[5] = 'admin'  # Traceback (most recent call last):
#                     # File "/home/carl/Github/DjangoPython/Django Python Class Notes/Tuples.py", line 15, in <module>
#                     #     users[5] = 'admin'
#                     # TypeError: 'tuple' object does not support item assignment


password = ('123', '1234', '12345', '123456')

l = []
l.append(users);l.append(password)
# print(l)  # [('rich', 'carl', 'rootadministrator', 'public'), ('123', '1234', '12345', '123456')]

# print(l[1])  # ('123', '1234', '12345', '123456')

# print(l[1]);print(type(l[1]));print(type(l[0]))  # ('123', '1234', '12345', '123456')
#                                                 # <class 'tuple'>
#                                                 # <class 'tuple'>

# print(l[1]);print(type(l[1]));print(type(l[0]));print('classe 1 has', type(l))  # ('123', '1234', '12345', '123456')
#                                                                                 # <class 'tuple'>
#                                                                                 # <class 'tuple'>
#                                                                                 # classe 1 has <class 'list'>

# print(l[1]);print(type(l[1]));print(type(l[0]));print('classe 1 has', type(l))  #

# del l[0]
# print(l)  # [('123', '1234', '12345', '123456')]  ***** users list deleted

# del l[0][0] # Traceback (most recent call last):
#             # File "/home/carl/Github/DjangoPython/Django Python Class Notes/Tuples.py", line 43, in <module>
#             #     del l[0][0]
#             # TypeError: 'tuple' object doesn't support item deletion

print(l[0].index('ali'))


