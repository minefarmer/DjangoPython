# how to open files in python  19
# how to use rstrip to remove empty lines from file  34
# readlines 46
# more on readlines 55
# more on readlines 65
# usng (for i in line) 76
# using f.strip 94
# using f.strip 107
# writing to file 124

# file_path = 'Django Python Class Notes/carl3.py'


# with open(file_path, 'w') as file:
#     file.write('hello world\n this is python \n python is the best \n how to open files in python')



# #  how to open files in python  19
# filename = 'Django Python Class Notes/rich.txt'

# with open(filename, 'r') as file:
#     for f in file:
#         print(f)  # hello world

#                     # this is python 

#                     # python is the best 

#                     # how to open files in python



# #  how to use rstrip to remove empty lines from file  34
# filename = 'Django Python Class Notes/rich.txt'

# with open(filename, 'r') as file:
#     for f in file:
#         print(f.rstrip())  # hello world
#                     # this is python 
#                     # python is the best 
#                     # how to open files in python



# #  readlines 46
# filename = 'Django Python Class Notes/rich.txt'

# with open(filename, 'r') as file:
#     file = file.readlines()
# print(file)  # ['hello world\n', ' this is python \n', ' python is the best \n', ' how to open files in python']



# #  more on readlines 55
# filename = 'Django Python Class Notes/rich.txt'
# with open(filename, 'r') as file:
#     line = file.readlines()
    
# string = ''
    
# print(type(line))  # <class 'list'>


# #  more on readlines 65
# filename = 'Django Python Class Notes/rich.txt'
# with open(filename, 'r') as file:
#     line = file.readlines()
    
# string = ''
    
# print(line)  # ['hello world\n', ' this is python \n', ' python is the best \n', ' how to open files in python']



# #  usng (for i in line) 76
# filename = 'Django Python Class Notes/rich.txt'
# with open(filename, 'r') as file:
#     line = file.readlines()
    
# string = ''
    
# for i in line:
#     print(i)  # hello world

#                 # this is python 

#                 # python is the best 

#                 # how to open files in python



# #  using i.strip 94
# filename = 'Django Python Class Notes/rich.txt'
# with open(filename) as file:
#     line = file.readlines()
    
# string = ''
    
# for i in line:
#     string += i.strip()
# print(string)  # hello worldthis is pythonpython is the besthow to open files in python



# #  using f.strip 107
# with open('Django Python Class Notes/rich.txt', 'r') as file:
#     file = file.readlines()    
# string = ''


# for f in file:
#     string += f.strip()
    
    
# if 'python' in string:
#     print('yes')  # yes
# else:
#     print('no')



#  writing to file 124
with open('Django Python Class Notes/rich.txt', 'w') as file:
    file.write('hello world\n')
    file.write('this is python learning\n')
    file.write('how to write data in the file with python')
file.close()


with open('Django Python Class Notes/rich.txt') as f:
    f = f.read()
print(f)  # hello world
            # this is python learning
            # how to write data in the file with python
