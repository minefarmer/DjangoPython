# AssertionError  11
# AssertionError  26
# AssertionError  40
# AssertionError: error, my_func(-10)  50
# No AssertionError: error, my_func(10)   65
# 
# 
# 
# 

# print('1')  # 1

# assert 2 + 2 ==4

# print('2')  # 2

# assert 1 + 1 == 3  # Traceback (most recent call last):
#                     # File "/home/carl/Github/DjangoPython/Django Python Class Notes/TryExceptAssert.py", line 17, in <module>
#                     #     assert 1 + 1 == 3
#                     # AssertionError

# print('3')



# AssertionError  26
# print(0)  # 0

# assert 'h' != 'w'
# print(1)  # 1

# assert 'h' == 'w'  # Traceback (most recent call last):
#                     # File "/home/carl/Github/DjangoPython/Django Python Class Notes/TryExceptAssert.py", line 36, in <module>
#                     #     assert 'h' == 'w'
#                     # AssertionError
# print(2)



# AssertionError  40
# temp = -10

# assert (temp >= 0), 'colder than absolute zero'  # Traceback (most recent call last):
#                                                 # File "/home/carl/Github/DjangoPython/Django Python Class Notes/TryExceptAssert.py", line 43, in <module>
#                                                 #     assert (temp >= 0), 'colder than absolute zero'
#                                                 # AssertionError: colder than absolute zero



# AssertionError: error,  my_func(-10)  50
# def my_func(x):
#     assert x > 0, 'error'
#     print(x)


# my_func(-10)  # Traceback (most recent call last):
#                 # File "/home/carl/Github/DjangoPython/Django Python Class Notes/TryExceptAssert.py", line 56, in <module>
#                 #     my_func(-10)
#                 # File "/home/carl/Github/DjangoPython/Django Python Class Notes/TryExceptAssert.py", line 52, in my_func
#                 #     assert x > 0, 'error'
#                 # AssertionError: error



# NO AssertionError: error, my_func(10)   65
def my_func(x):
    assert x > 0, 'error'
    print(x) # 10


my_func(10)

