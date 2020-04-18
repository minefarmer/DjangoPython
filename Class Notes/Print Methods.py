# print('hi' + 'rich')  # hirich

# print('hi' + ' rich')  # hi rich
# print('hi ' + 'rich')  # hi rich


a = 33
f = 12.5
name = 'carl'

# print('hi' + '' + f)  # print('hi' + '' + f)
#                       # TypeError: can only concatenate str (not "float") to str

# print('hi' '' + a)  # hi33  # print('hi' '' + a)  # hi33
# 							# TypeError: can only concatenate str (not "int") to str

# print('the number is' + ' ' + str(a))  # the number is 33

# print('the number is %d ' % a )  # the number is 33

# print('the number is %d and %f ' % (a, f) )  # the number is 33 and 12.50000

# print('the number is %d and %f ' % (a, f) )  # the number is 33 and 12.50000
# print('hi %s' % name )  # hi carl

# print('the numbers are {} and {} and the name is {} '.format(a, f, name))  # the numbers are 33 and 12.5 and the name is carl

# print('the numbers are {} and {} and the name is {} '.format(name, f, name))  # the numbers are 33 and 12.5 and the name is carl

print('the numbers are {} and {} and the name is {} '.format(name, f, name))  # the numbers are 33 and 12.5 and the name is carl  *** this code from python2
print(f'the numbers are {a} and {f} and the name is {name}')  # the numbers are 33 and 12.5 and the name is carl  *** added the f in front
