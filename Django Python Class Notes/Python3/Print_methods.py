# a = 'name'
# b = 30
# print(a)  # name
# print(b)  # 30

a = 33
f = 12.5

# print('hi' + ' ' + f)  # Traceback (most recent call last):
#                     #   File "/home/carl/Github/DjangoPython/Django Python Class Notes/Print_methods.py", line 9, in <module>
#                     #     print('hi' + ' ' + f)
#                     # TypeError: can only concatenate str (not "float") to str

# print('HI' + ' ' str(a))  #  print('HI' + ' ' str(a))
#                         #                         ^
#                         #     SyntaxError: invalid syntax

# print('the number is %d ' % a)  # the number is 33 

# print('the number is %d ' % f)  # the number is 12 

# print('the number is %d and %f ' %(a, f))  # the number is 33 and 12.500000

name = 'pedram'

# print('the number is %d ' % f)  # the number is 12 
# print('hi %s' % name )  # hi pedram

# print('the number is {} and {} and the name is {} '.format(a, f, name))  # the number is 33 and 12.5 and the name is pedram

# two differient ways to do the same thing  *** second is standard?
# print('the number is {} and {} and the name is {} '.format(name, f, name))  # the number is pedram and 12.5 and the name is pedram 
print(f'the number is {a} and {f} and the name is {name}')  # the number is 33 and 12.5 and the name is pedram

