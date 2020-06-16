# how to open files in python  19
# how to use rstrip to remove empty lines from file  34
# readlines 46
# more on readlines 55
# more on readlines 65
# usng (for i in line) 76
# using i.string 94
# 
# 

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



#  using i.string 94
filename = 'Django Python Class Notes/rich.txt'
with open(filename) as file:
    line = file.readlines()
    
string = ''
    
for i in line:
    string += i.strip()
print(string)  # hello worldthis is pythonpython is the besthow to open files in python