# lesson 30  continue starts on line 80
# Some Dict and boolean 133
# Main Dict and boolean 165
# while loops with lists  190
# while loops with lists-2  235

# i = 0
# while i < 10:
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
#     i = i + 1

# i = 0
# while i < 11:
#     if i % 2 == 0:
#         print(i)    # 0
#                     # 2
#                     # 4
#                     # 6
#                     # 8
#                     # 10
#     i = i + 1

# i = 0
# while i < 11:
#     if i % 2 == 0:
#         print(i)    # 0
#     print('i ++')   # 1 ++
#                     # i ++
#                     # 2
#                     # i ++
#                     # i ++
#                     # 4
#                     # i ++
#                     # i ++
#                     # 6
#                     # i ++
#                     # i ++
#                     # 8
#                     # i ++
#                     # i ++
#                     # 10
#                     # i ++
#     i = i + 1
    

# sum = 'matson'
# i = 0

# # print(sum[0])  # m
# # print(sum[2])  # t
# # print(sum[4])  # o

# while i < len(sum):
#     print('i ====> ', i)
#     print(sum[i])   # i ====>  0
#                     # m
#                     # i ====>  1
#                     # a
#                     # i ====>  2
#                     # t
#                     # i ====>  3
#                     # s
#                     # i ====>  4
#                     # o
#                     # i ====>  5
#                     # n
#     i = i + 1
    


#  lesson 30 = while loop and continue  *********************************************

# i = 0
# while True:
#     i += 1
#     if i == 2:
#         print('skipping 2')
#         continue
#     if i == 10:
#         print('skippimg 10')
#         continue
#     if i == 20:
#         print('now break')
#         break
#     print(i)
# print('finish')
#             # Printed
#             # 1
#             # skipping 2
#             # 3
#             # 4
#             # 5
#             # 6
#             # 7
#             # 8
#             # 9
#             # skippimg 10
#             # 11
#             # 12
#             # 13
#             # 14
#             # 15
#             # 16
#             # 17
#             # 18
#             # 19
#             # now break
#             # finish

# i = 0
# while True:
#     i += 1
#     if i % 2 == 0:
#         print('skipping {i}')
#         continue
#     if i == 21:
#         print('now break')
#         break
#     print(i)
# print('finish')



# Dict and boolean  ***********************************************
# a = 'rich'
# a = 'carl' # the second one always replaces the first one

# my_list1_active = ['root', 'admin', 'boss']
# my_list2 = []

# while my_list1_active:
#     current_user = my_list1_active.pop()
#     print('verifying user: ' + current_user) # verifying user: boss
#                                   # verifying user: admin
#                                   # verifying user: root
#     my_list2.append(current_user)
# print('\n the following users have been confirmed')  #  the following users have been confirmed
# for i in my_list2:
#     print('  ', i.title())  # Boss
#                             # Admin
#                             # Root


# pets = ['dog', 'cat', 'dog', 'cat', 'rabbit', 'cat', 'dog']

# # while  'cat' in pets:  # removing all cats from list
# #     pets.remove('cat')
# # print(pets)  # ['dog', 'dog', 'rabbit', 'dog']

# while  'cat' in pets:  # removing all cats from list
#     pets.remove('cat')
# print(pets) 



# while True:
#     print('Please enter your name: ')
#     name = input('> ')
#     if name == 'exit' or name == 'e':
#         break
    
# res = {}

# active = True
# prompt = '> '
# while active:
#     print('Please enter your name: ')  # Please enter your name: 
#     name = input(prompt)  $ rich
#     response = input('please enter your date of birth: ')  # please enter your date of birth: 10/15/1938
#     res[name] = response
#     print('do you want to repeat the questions? ')  # do you want to repeat the questions?
#     repeat = input('yes/ no ')  # yes/ no no
#     if repeat == 'no':
#         active = False
# for k, v in res.items():
#     print('  ', k, v)  #   rich 10/15/1938

    
    
    
#  while loops with lists
#  THIS DOES NOT WORK
# words = ['hello', 'world', 'spam', 'eggs']
# counter = 0

# max_index = len(words) - 1
# print(words[max_index:])
# while counter <= max_index:
#     words = words[counter]
#     print(words + ' !')
#     counter += 1


# while True:  ***DO NOT USE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     print('please enter numbers to calc')
#     a = int(input('please enter first number '))
#     b = int(input('please enter second number '))
#     print('this is a simple calc')
#     print('enter sub to subtract two numbers')
#     print('enter sum to sum two numbers ')
#     print('ENTER DIV DIVIDE TWO NUMBERS ')
#     print('enter mult to multiply two numbers ')
#     print('press enter exit or e to exit')
#     user_input = input('> ')
    
#     if user_input == 'exit' or user_input == 'e':
#         break
#     elif user_input == 'sum':
#         c = a + b 
#     elif user_input == 'sub':
#         c = a - b 
#     elif user_input == 'div':
#         c = a / b 
#     elif user_input == 'mult':
#         c = a * b 
        
#     print(f'the answer of {user_input} is {c}')
    
# print('finish')






#  while loops with lists Part two

while True:
    print('please enter numbers to calc')
    print('this is a simple calc')
    print('enter sub to subtract two numbers')
    print('enter sum to sum two numbers ')
    print('ENTER DIV DIVIDE TWO NUMBERS ')
    print('enter mult to multiply two numbers ')
    print('press enter exit or e to exit')
    user_input = input('> ')
    
    if user_input == 'exit' or user_input == 'e':
        break
    elif user_input == 'sum':
        a = float(input('please enter first number '))
        b = float(input('please enter second number '))
        c = a + b 
    elif user_input == 'sub':
        a = float(input('please enter first number '))
        b = float(input('please enter second number '))
        c = a - b 
    elif user_input == 'div':
        a = float(input('please enter first number '))
        b = float(input('please enter second number '))
        c = a / b 
    elif user_input == 'mult':
        a = float(input('please enter first number '))
        b = float(input('please enter second number '))
        c = a * b 
    else:
        print('Please enter sum or sub or div mult')
        print()
        print('now continue..............')
        continue
    print(f'the answer of {user_input} is {c}')
    
print('finish')