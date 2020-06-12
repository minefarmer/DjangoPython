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

f = open('test.txt', 'w')
f.write('Hello World!\n')
f.close()
file_1 = open('test.txt', 'r')
print(file_1.read())  # Hello World!