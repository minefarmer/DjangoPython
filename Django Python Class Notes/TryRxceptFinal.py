# except ZeroDivisionError  11
# except name error  24
# except statement  35
# except statement, without error  43
# hello, except statement  52
# hello, except,  finally statement  61
# 1, 3 72
# 2, 3, 82
# ????????   92
# index continued  113
# try:
#     num1 = 7
#     num2 = 0
#     print(num1 / num2)
#     print(num1 / num2)
#     print('hi')
#     print('test')
#     print('lastone')
# except ZeroDivisionError:
#     print('an error')  # an error



# # name error  24
# try:
#     a = 10
#     print(a + b)
# except ZeroDivisionError:
#     print('zero division error')
# except NameError:
#     print('name error')  # name error



# except statement
# try:
#     num = 42
#     print(num / 0)
# except (ZeroDivisionError, TypeError):
#     print('except statement')  # except statement
    
    
# except statement
# try:
#     name = 'spam'
#     print(name + world)
# except:
#     print('except statement without error')  # except statement without error



#  hello, except statement  52
# try:
#     print('hello') # hello
#     print(1/0)
# except ZeroDivisionError:
#     print('except statement')  # except statement



# #  hello, except,  finally statement  61
# try:
#     print('hello')    # hello
#     print(1/0)
# except ZeroDivisionError:
#     print('except statement')  # except statement
# finally:
#     print('finally statement')  # finally statement



# #  1, 3 72
# try:
#     print('1')  # 1
# except:
#     print('2')
# finally:
#     print('3')  # 3



#  2, 3, 72
# try:
#     print('1', name)  
# except:
#     print('2')  # 2
# finally:
#     print('3')  # 3



#  ????????   92
# try:
#     print('1')
#     print(10/0)
# except ZeroDivisionError:
#     print(unkown_var)  # raceback (most recent call last):
#                         # File "/home/carl/Github/DjangoPython/Django Python Class Notes/TryRxceptFinal.py", line 93, in <module>
#                         #     print(10/0)
#                         # ZeroDivisionError: division by zero

#                         # During handling of the above exception, another exception occurred:

#                         # Traceback (most recent call last):
#                         # File "/home/carl/Github/DjangoPython/Django Python Class Notes/TryRxceptFinal.py", line 95, in <module>
#                         #     print(unkown_var)
#                         # NameError: name 'unkown_var' is not defined
# finally:
#     print('ok')  # ok



# raise NameError  117



# raise NameError
# print('1')  # 1
# raise NameError  # Traceback (most recent call last):
#                 # File "/home/carl/Github/DjangoPython/Django Python Class Notes/TryRxceptFinal.py", line 122, in <module>
#                 #     raise NameError
#                 # NameError

# print('2')
# print('3')
# print('4')




try:
    print(1/0)
except ZeroDivisionError:
    raise ValueError