# read an existing file in the terminal  11
# alt read an existing file in the terminal   20
# changing an existing file in the terminal  ** this over wrote the above example  30
# adding an empty line in the terminal  ** this over wrote the above example  40
# open empty file  50
# a better way  56
# 
# 
# 
# 
# f = open('Django Python Class Notes/testA.txt')
# f = f.read()
# print(f)  # hello world
#             # this is python3 
#             # python3 is the best 
#             # how to open files in python3



# #  alt read an existing file in the terminal
# f = open('Django Python Class Notes/testA.txt, 'r')
# file_1 = f.read()
# print(file_1)  # hello world
#             # this is python3 
#             # python3 is the best 
#             # how to open files in python3



# #  changing an existing file in the terminal  ** this over wrote the above example
# f = open('Django Python Class Notes/testA.txt', 'w')
# f.write('Hello world!')
# f.close()
# file_1 = open('Django Python Class Notes/testA.txt','r')
# print(file_1.read())  # hello world




# #  adding an empty in the terminal  ** this over wrote the above example
# f = open('Django Python Class Notes/testA.txt', 'w')
# f.write('Hello world!\n')
# f.close()
# file_1 = open('Django Python Class Notes/testA.txt','r')
# print(file_1.read())  # hello world
#                       # empty line



#  open empty file
# file = open('Django Python Class Notes/carl.txt', 'r')
# f = file.read();print(f) # empty line



# #  a better way  56
# with open('Django Python Class Notes/carl.txt', 'w') as file:
#     file.write('hi \n hello world \n bye')
# file.close()

# with open('Django Python Class Notes/carl.txt') as f:
#     f = f.read()
# print(f)  # hi 
#             # hello world 
#             # bye

