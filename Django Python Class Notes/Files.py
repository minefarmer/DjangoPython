# FILES WITH OPEN  ** 50
# BETTER WAY TO DO THE ABOVE WORK  60
# rstrip  80
# # # easy way to create a new file  95  ******************************
# # #   readlines  # 100  
# class string  # 105
# #  class list  # 115
# Using rstrip  145
# 
# 

# f = open('test.txt')
# f = f.read()
# print(f)

# f = open('test.txt', 'r')
# file_1 = f.read()
# print(file_1)  # this is a test.

# f = open('test.txt', 'w')
# file_1 = f.read();print(file_1)  # Traceback (most recent call last):
#                                 # File "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/Files.py", line 10, in <module>
#                                 #     file_1 = f.read();print(file_1)
#                                 # io.UnsupportedOperation: not readable
# # the contents of the file have been deleated

# f = open('test.txt', 'w')
# f.write('Hello World!')
# f.close()
# file_1 = open('test.txt', 'r')
# print(file_1.read())  # Hello World!

# f = open('test.txt', 'w')
# f.write('Hello World!', '\n')
# f.close()
# file_1 = open('test.txt', 'r')
# print(file_1.read())  # Traceback (most recent call last):
#                         # File "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/Files.py", line 23, in <module>
#                         #     f.write('Hello World!', '\n')
#                         # TypeError: write() takes exactly one argument (2 given)

# f = open('test.txt', 'w')
# f.write('Hello World!\n')
# f.close()
# file_1 = open('test.txt', 'r')
# print(file_1.read())  # Hello World!



# FILES WITH OPEN  ** 50
# file = open('rich.txt', 'r')
# f = file.read();print(f)  # nothing printed == empty file

# file = open('rich.txt', 'w')   # ** Do not use **
# file.write('hello world\n')
# file.close()  # must always be done to save the file  *** not workin g as shown in video



#  BETTER WAY TO DO THE ABOVE WORK  60
# with open('rich.txt') as file:
#     f = file.read()  # can use file instead of f
# print(f)  # hello world

# with open('rich.txt', 'w') as file:
#     file.write('hi \n helloworld \n bye')  # can use file instead of f
# print(file)  # <_io.TextIOWrapper name='rich.txt' mode='w' encoding='cp1252'>



# with open('rich.txt', 'w') as file:
#     file.write('hi \n hello world \n bye')  # can use file instead of f
# file.close()

# with open ('rich.txt') as f:
#     f = f.read()
# print(f)  # hi
#             # hello world 
#             # bye
# rstrip
# with open('rich.txt', 'w') as file:
#     file.write('hi \n hello world \n bye')  # can use file instead of f
# file.close()

# with open ('rich.txt') as f:
#     f = f.read()
# print(f.rstrip())  # hi
#                     # hello world 
#                     # bye





#  create new file  95
# with open ('Django Python Class Notes/testA.txt', 'w') as file:
#     file.write('hello world\n this is python3 \n python3 is the best \n how to open files in python3')


#  readlines  # 100
# with open ('Django Python Class Notes/testA.txt', 'r') as file:
#     file = file.readlines()
# print(file)  # ['hello world\n', ' this is python3 \n', ' python3 is the best \n', ' how to open files in python3']

#  class string  # 105
# filename = 'Django Python Class Notes/carl.txt'
# with open(filename, 'r') as file:
#     line = file.readlines()
    
#     string = ''
    
#     print(type(line))  # <class 'list'>
  
    
# #  class list 
# filename = 'Django Python Class Notes/testA.txt'
# with open(filename) as file:
#     line = file.readlines()
    
# string = ''
    
# for i in line:
#     print(i)


# filename = 'Django Python Class Notes/testA.txt'
# with open(filename) as file:
#     line = file.readlines()
    
# string = ''
    
# for i in line:
#     # string += i.rstrip()

#   string = ''

#     print(i)  # hello world

#                 # this is python3

#                 # python3 is the best

#                 # how to open files in python3

# # Using rstrip  145
# filename = 'Django Python Class Notes/testA.txt'
# with open(filename) as file:
#     line = file.readlines()
    
# string = ''
    
# for i in line:
#     string += i.rstrip()
    
#     print(string)  # hello world


#     # print(i)  # hello world
#                 # this is python3
#                 # python3 is the best
#                 # how to open files in python3


# filename = 'Django Python Class Notes/testA.txt'
# with open(filename, 'r') as file:
#     file = file.readlines()  
# string = ''
    
# for f in file:
#     string += f.strip()

# if 'python' in string:
#     print('yes')  # yes
# else:
#     print('no')
    

# with open('Django Python Class Notes/carl2.txt', 'w') as file:
#     file.write('hello world\n')
#     file.write('this is python learning\n')
#     file.write('how to write data in a file with python')
# file.close()


with open('Django Python Class Notes/carl2.txt') as f:
    f = f.read()
print(f)  # hello world
            # this is python learning
            # how to write data in a file with python

