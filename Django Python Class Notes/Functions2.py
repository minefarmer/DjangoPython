# Default parameters  75
# #  using a default parameter  105
# 
# 
# 

# def get_format_name(first_name, last_name):
#     """ return a full name"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_format_name('jimi', 'hendrix')
# print('musician function is ' , musician)  # Jimi Hendrix

# teacher = get_format_name('rich', 'matson')

# print('teacher finction is ', teacher)  # Rich 



# def get_format_name(first_name, last_name):
#     """ return a full name"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# d = {
#     'teachers' : get_format_name('rich', 'matson'),
#     'musicians' : get_format_name('jimi', 'hendrix')
# }

# print(d['teachers']);print(d['musicians'])  # Rich Matson   # Jimi Hendrix



def get_format_name(first_name, last_name):
    """ return a full name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

d = {
    'teachers' : get_format_name('rich', 'matson'),
    'musicians' : get_format_name('jimi', 'hendrix')
}

# # print(d['teachers']);print(d['musicians'])  # Rich Matson   # Jimi Hendrix
# def Test(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name
# print(Test('rich', 'matson'))  # rich matson
# print(Test('carl', 'matson', 'rich'))



# def Test(a, b):
#     c = a + b
#     return c
# a = 33
# Test(a)  # Traceback (most recent call last):
#         # File "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/Functions2.py", line 60, in <module>
#         #     Test(a)
#         # TypeError: Test() missing 1 required positional argument: 'b'
#         # PS C:\Users\pgold\Github\DjangoPython> 

# #  above corrected
# def Test(a, b):
#     c = a + b
#     return c
# a = 33
# Test(a, 20)  # 



# Default parameters  75
""" 
default parameters by definition are the parameters that are defined with in the function at the same time the user gives that parameter to the program.
"""

# def Test(car_name, car_type):
#     #  display info about cars
#     print('\n i have a ' + car_type + ' car')  #  i have a light car
#     print('my ' + car_type + ' is ' + car_name)  # my light is audi
# Test('audi', 'light')

# def Test(car_name, car_type):  # missing default parameter light from user
#     #  display info about cars
#     print('\n i have a ' + car_type + ' car')  #  i have a light car
#     print('my ' + car_type + ' is ' + car_name)  # my light is audi
# Test('audi')  # Traceback (most recent call last):
#                 # File "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/Functions2.py", line 90, in <module>
#                 #     Test('audi')
#                 # TypeError: Test() missing 1 required positional argument: 'car_type'

# def Test(car_name, car_type='light'):  # not default parameter from user  **  default works if nothing is added, if light is entered it is swown
#     #  display info about cars
#     print('\n i have a ' + car_type + ' car')  #  i have a heavy car
#     print('my ' + car_type + ' car is ' + car_name)  # my heavy is audi
# Test('audi', ' heavy')  





#  using a default parameter
def get_names()
