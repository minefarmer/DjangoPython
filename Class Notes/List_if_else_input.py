# l = []

# if l:
#     for i in l:
#         print(l)
# else:
#     print('there are no items in l')



# # If I don't enter my name
# n = str(input('please enter your name '))  # if I don't enter my name when "please enter your name" shows and I hit enter

# if n:
#     print('welcome {}' .format(n))  # Does not print anything
# else:
#     print('Please enter your name ksdig')  # and this is printed *** Please enter your name ksdig


# n = str(input('please enter your name '))  # if I enter my name when "please enter your name" shows and I hit enter

# if n:
#     print('welcome {}' .format(n))  # welcome rich
# else:
#     print('Please enter your name ksdig')  # does nothing



# l = ['root', 'admin', 'administrator', 'matson']

# user_name = str(input('please enter your user name '))  # rich

# if user_name not in l:
#     print('your user name is not in l ')  # your user name is not in l
#     print('but, I added your user name in list')  # but, I added your user name in list
#     print("welcome {}".format(user_name))  # welcome rich
#     l.append(user_name)
#     print(l)  # ['root', 'admin', 'administrator', 'matson', 'rich']
# else:
#     print('welcome {}'.format(user_name))


l = ['root', 'admin', 'administrator', 'matson']

user_name = str(input('please enter your user name '))  # root

if user_name not in l:
    print('your user name is not in l ')
    print('but, I added your user name in list')
    print("welcome {}".format(user_name))
    l.append(user_name)
    print(l)
else:
    print('welcome {}'.format(user_name))  # welcome root