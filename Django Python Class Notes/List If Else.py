# name added 29
# name on list 42
# 
# 
# 

# l = []

# if l:
#     for i in l:
#         print(l)
# else:
#     print('There are no items in l')  # There are no items in l


# n = str(input('Please enter your name '))  # Please enter your name
# if n:    *****  nothing entered
#     print('welcome {}'.format(n))
# else:
#     print('please enter your name spud')  # Please enter your name spud

# n = str(input('Please enter your name '))  # Please enter your name rich
# if n:
#     print('welcome {}'.format(n))  # welcome rich
# else:
#     print('please enter your name spud')


# l =['root', 'admin', 'adninistrator', 'matson']

# user_name = str(input('Please enter your user name '))  # rich

# if user_name not in l:
#     print('your user name is not in l')  # your user name is not in l
#     print('but I added your user name in list')  # but I added your user name in list
#     print('welcome {}'.format(user_name))  # welcome rich
#     l.append(user_name)
#     print(l)  # ['root', 'admin', 'adninistrator', 'matson', 'rich']
# else:
#     print('welcome {}'.format(user_name))

l =['root', 'admin', 'adninistrator', 'matson']

user_name = str(input('Please enter your user name '))  # root

if user_name not in l:
    print('your user name is not in l') 
    print('but I added your user name in list')
    print('welcome {}'.format(user_name))
    l.append(user_name)
    print(l)  # ['root', 'admin', 'adninistrator', 'matson', 'rich']
else:
    print('welcome {}'.format(user_name))  # welcome root