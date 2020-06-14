# ZeroDivisionError  * 10
# solving the ZeroDivisionError  ** 15
# solving the ZeroDivisionError - second example. setp one. ** 27
# solving the ZeroDivisionError - second example.  Step two. ** 45
# 
# Full working copy == solving the ZeroDivisionError - second example.  Step three. ** 66



# print(5/0)  #   File "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/Try Except.py", line 1, in <module>
#             #     print(5/0)
#             # ZeroDivisionError: division by zero


# # solving the ZeroDivisionError  ** 15
# n = int(input('please enter a number: '))
# n2 = int(input('please enter a second number: '))

# try:
#     print(n/n2)
# except ZeroDivisionError:
#     print('the number is zero')  #  5
#                                 # please enter a second number: 0
#                                 # the number is zero


# # solving the ZeroDivisionError - second example ** 27
# print('give me two numbers, and I"ll divide them')
# print('enter q to quit')

# while True:
#     first_number = input('\nFirst number: ')
#     if first_number == 'q':
#         break
#     second_number = input('second_number: ')
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)  # Traceback (most recent call last):
#                     # File "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/Try Except.py", line 41, in <module>
#                     #     answer = int(first_number) / int(second_number)
#                     # ZeroDivisionError: division by zero


# # solving the ZeroDivisionError - second example.  Step two. ** 45
# print('give me two numbers, and I"ll divide them')
# print('enter q to quit')

# while True:
#     first_number = input('\nFirst number: ')
#     if first_number == 'q':
#         break
#     second_number = input('second_number: ')
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#         print(answer)  # 7
#                         # 0
#                         # the number is 0 or Zero
                        
#     except ZeroDivisionError:
#         print('the number is 0 or Zero')


# # solving the ZeroDivisionError - second example.  Step three. ** 66
print('give me two numbers, and I"ll divide them')
print('enter q to quit')

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('second_number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
                        
    except ZeroDivisionError:
        print('the number is 0 or Zero')
    else:
        print(answer)  # give me two numbers, and I"ll divide them
                        # enter q to quit

                        # First number: 50
                        # second_number: 2
                        # 25.0

                        # First number: 60
                        # second_number: 3
                        # 20.0

                        # First number: 60
                        # second_number: 0
                        # the number is 0 or Zero

                        # First number: q