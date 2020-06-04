# math 90
# good function 110
# expanded function 150
# 
# 
# #  this ius a function
# a = {'name': 'rich'}
# b = a.copy();print(b)  # {'name': 'rich'}

# print('HI' + 'carl')  # HIcarl
# print('HI ' + 'rich')  # HI rich
# print('HI' + 'sis')  # HIsis

# def Test()  copy()  update()  input()

# def Test():
#     print('hi ' + 'rich')  # hi rich
    
# Test()  # this needed for print to work  # hi rich
# Test()  # this needed for print to work  # hi rich

# def Test(name):
#     print('hi ' + 'name')  # hi name
    
# Test('rich')

# def Test(name):
#     print('hi ' + name)  # Traceback (most recent call last):
#                         # File "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/Function.py", line 30, in <module>
#                         #     Test(3)
#                         # File "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/Function.py", line 28, in Test    
#                         #     print('hi ' + name)  # hi name
#                         # TypeError: can only concatenate str (not "int") to str
    
# Test(3)


# def Test(a, b):
#     # give me two number
#     c = a * b
#     return c
# Test(2)  # Traceback (most recent call last):
#         # File "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/Function.py", line 41, in <module>
#         #     Test(2)
#         # TypeError: Test() missing 1 required positional argument: 'b'
#         # PS C:\Users\pgold\Github\DjangoPython> 


# def Test(a, b):
#     # give me two number
#     c = a * b
#     return c
# print(Test(2, 5))  # 10


# def Test():
#     return 'hi'
# Test('rich')  # Traceback (most recent call last):
#             # File "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/Function.py", line 58, in <module>
#             #     Test('rich')
#             # TypeError: Test() takes 0 positional arguments but 1 was given
            
            
# def Test():
#     return 'hi'
# Test()
# d = {'name' : 'rich'}
# d2 = d.copy(3)  # Traceback (most recent call last):
#                 # File "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/Function.py", line 68, in <module>
#                 #     d2 = d.copy(3)
#                 # TypeError: copy() takes no arguments (1 given)


# def sum_number(a, b):
#     c = a + b
#     print('the answer is ' + ' ' + str(c))
# def multiple_numbers(a, b):
#     c = a * b
#     print('the answer is ' + ' ' + str(c))
# def subtrac_numbers(a, b):
#     c = a - b
#     print('the answer is ' + ' ' + str(c))
# def division_numbers(a, b):
#     c = a / b
#     print('the answer is ' + ' ' + str(c))
    
# sum_number(140, 34)  # the answer is  174


# def sum_number(a, b):
#     c = a + b
#     print('the answer is ' + ' ' + str(c))
# def multiple_numbers(a, b):
#     c = a * b
#     print('the answer is ' + ' ' + str(c))
# def subtrac_numbers(a, b):
#     c = a - b
#     print('the answer is ' + ' ' + str(c))
# def division_numbers(a, b):
#     c = a / b
#     print('the answer is ' + ' ' + str(c))
    
# sum_number(140 + 43, 50)  # the answer is  233
# multiple_numbers(50, 12)  # the answer is  600
# subtrac_numbers(20, 10)  # the answer is  10
# division_numbers(40, 10)  # the answer is  4.0



# good function   ************************************************

# def isphonenumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i]. isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True

# print(isphonenumber('000-000-0000'))  # True



# message = 'call me at 415-555-1011 tomorrow. 415-555-999 is my office'

# # for i in range(len(message)):
# #     print(i)  # 1 thru 57
    
    
# for i in range(len(message)):
#     test = message[i:i+12]
#     if isphonenumber(test):
#         print('phone number found: ' + test)

# print('Done')




# expanded function

def isphonenumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i]. isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'call me at 415-555-1011 tomorrow. 415-555-999 is my office'

  
for i in range(len(message)):
    test = message[i:i+12]
    if isphonenumber(test):
        print('phone number found: ' + test)  # phone number found: 415-555-1011

print('Done')  # Done