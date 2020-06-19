#  Join 60

# spam = 'hello world'
# print(spam.upper())  # HELLO WORLD
# test = 'HELLO WORLD'
# print(test.lower())  # hello world

# print('how are you? ')  # how are you?
# feeling = input()
# if feeling.lower() == 'great':
#     print('I feeling great too.')  # I feeling great too.
# else:
#     print('i hope the rest of your day is good.')
    
    
# >>> 'hello'.isalpha()
# True
# >>> 'hello123'.isalnum
# <built-in method isalnum of str object at 0x037EDD68>
# >>> 'hello123'.isalnum()
# True
# >>> '123'.isdecimal()
# True
# >>> '     '.isspace()
# True
# >>> 'this is title'.istitle()
# False
# >>> 'this is Title'.istitle()
# False
# >>> 'This is Title'.istitle()
# False
# >>> 'This Is Title'.istitle()
# True
# >>> exit
# Use exit() or Ctrl-Z plus Return to exit
# >>> exit()

# while True:
#     print('enter your age: ')  # first = matson   ****** after line 42 = 81
#     age = input()
#     if age.isdecimal():
#         break
#     else:
#         print('Please enter a number for your age. ')  # Please enter a number for your age.  ### matson  *** 81  
        

# while True:
#     print('select a new password (letters and numbers only)')  # 123   ## matson123
#     password = input()
#     if password.isalnum():
#         print('thanks ', password)  # thanks  123  ## thanks  matson123
#         break
#     print('password can only have letters and numbers')






#  Join **************************************************************
# print(', '.join(['cat', 'dog', 'bat']))  # cat, dog, bat
# print('*, '.join(['cat', 'dog', 'bat']))  # cat*, dog*, bat



# >>> 'hello'.rjust(10)
# '     hello'
# >>> 'hello'.rjust(40)
# '                                   hello'
# >>> 'hello'.ljust(40)
# 'hello                                   '
# >>> 'hello'.rjust(40)
# '                                   hello'
# >>> 'hello'.rjust(20, '*')
# '***************hello'
# >>> 'hello'.ljust(20, '*')
# 'hello***************'
# >>> 'hello'.ljust(20, '-')
# 'hello---------------'
# >>> 'hello'.ljust(20, '_')
# 'hello_______________'
# >>> 'hello'.ljust(20, '_')
# 'hello_______________'
# >>> 'hello'.center(20, '*')
# '*******hello********'
# >>> print('hello'.center(20, '*'))
# *******hello********
# >>>

# see lesson 36 for more info