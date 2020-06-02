# 25 changes
# 63 changes
# 100 better dict
# 166 standard way to write a dictionary

# d = {
#     'key_1' : {'name' : 'rich', 'age' : 81, 'f_name' : 'matson'},
#     'key_2' : {'car' : 'audi', 'max_speed' : 330, 'color' : 'black'},
#     'key_2' : {'movie1' : 2003, 'movie2' : 2016}
# }
# print(d['key_1'])  # {'name': 'rich', 'age': 81, 'f_name': 'matson'}

# for key, value in f.items(): # same as next line
# for k, v in f.items():
#     print(key)  # Traceback (most recent call last):
#                 # File "/home/carl/Github/DjangoPython/Django Python Class Notes/Dict For.py", line 14, in <module>
#                 #     for k, v in f.items():
#                 # NameError: name 'f' is not defined

# for key, value in d.items():
#     print(key)  # key_1
#                 # key_2


# d = {
#     'key_1' : {'name' : 'rich', 'age' : 81, 'f_name' : 'matson'},
#     'key_2' : {'car' : 'audi', 'max_speed' : 330, 'color' : 'black'},
#     'key_3' : {'movie1' : 2003, 'movie2' : 2016}
# }
# for key, value in d.items():
#     print(key)  # key_1
#                 # key_2
#                 # key_3

# for key, value in d.items():
#     print(key, value)   # key_1 {'name': 'rich', 'age': 81, 'f_name': 'matson'}
#                         # key_2 {'car': 'audi', 'max_speed': 330, 'color': 'black'}
#                         # key_3 {'movie1': 2003, 'movie2': 2016}

# for key, value in d.items():
#     print(d[key])   # {'name': 'rich', 'age': 81, 'f_name': 'matson'}
#                     # {'car': 'audi', 'max_speed': 330, 'color': 'black'}
#                     # {'movie1': 2003, 'movie2': 2016}

# for key, value in d.items():
#     print(d[key]); print(d['key_1'])  # {'name': 'rich', 'age': 81, 'f_name': 'matson'}
#                                     # {'name': 'rich', 'age': 81, 'f_name': 'matson'}
#                                     # {'car': 'audi', 'max_speed': 330, 'color': 'black'}
#                                     # {'name': 'rich', 'age': 81, 'f_name': 'matson'}
#                                     # {'movie1': 2003, 'movie2': 2016}
#                                     # {'name': 'rich', 'age': 81, 'f_name': 'matson'}

# for key, value in d.items():
#     print(d[key], value)  # {'name': 'rich', 'age': 81, 'f_name': 'matson'} {'name': 'rich', 'age': 81, 'f_name': 'matson'}
#                         # {'car': 'audi', 'max_speed': 330, 'color': 'black'} {'car':'audi', 'max_speed': 330, 'color': 'black'}
#                         # {'movie1': 2003, 'movie2': 2016} {'movie1': 2003, 'movie2':2016}

# for key, value in d.items():
#     if key == 'key_3':
#         print(value)  # {'movie1': 2003, 'movie2': 2016}




# d = {
#     'movie1' : 1997,
#     'movie2' : 2003,
#     'movie3' : 2003,
#     'movie4' : 2019,
#     'movie5' : 1997,
#     'movie6' : 2019,
# }

# print(d) # {'movie1': 1997, 'movie2': 2003, 'movie3': 2003, 'movie4': 2019, 'movie5': 1997, 'movie6': 2019}


# for k, v in d.items():
#     if v == 2003:
#         print(k)  # movie2
#                   # movie3

# input_1 = input('please enter a year : ')  # please enter a year : 2003
# for k, v in d.items():
#     if v == 2019:
#         print(k)  # movie4
#                   # movie6

# input_1 = input('please enter a year : ')  # please enter a year : 2019
# for k, v in d.items():
#     if v == int(input_1):
#         print(k)  # movie4
#                   # movie6

# input_1 = int(input('please enter a year : '))  # please enter a year : # 2003

# my_list = [k for (k, v) in d.items() if v == input_1]
# print(my_list)  # ['movie2', 'movie3']




#  better dict
# my_dict = {'numbers_1' : [1, 2, 3, 4], 'numbers_2' : [2, 3, 60], 'car_name' : 'jeep'}

# print(my_dict)  # {'numbers_1': [1, 2, 3, 4], 'numbers_2': [2, 3, 60], 'car_name': 'jeep'}

# for k in my_dict:
#     print(k)  # numbers_1
#               # numbers_2
#               # car_name

# for k, v in my_dict.items():
#     print(k, v)  # numbers_1 [1, 2, 3, 4]
#                 # numbers_2 [2, 3, 60]
#                 # car_name jeep


# my_list = [1, 2, 3, 4, 5]

# for i in my_dict.items():
#     print(i)  # ('numbers_1', [1, 2, 3, 4])
#               # ('numbers_2', [2, 3, 60])
#               # ('car_name', 'jeep')

# my_list = [1, 2, 3, 4, 5]
# for i in my_dict.keys():
#     print(i)  # numbers_1
#               # numbers_2
#               # car_name

# my_list = [1, 2, 3, 4, 5]
# for i in my_dict.values():
#     print(i)  # [1, 2, 3, 4]
#               # [2, 3, 60]
#               # jeep

# my_list = [1, 2, 3, 4, 5]
# for a, b in my_dict.items():
#     print(a, b)  # numbers_1 [1, 2, 3, 4]
#                  # numbers_2 [2, 3, 60]
#                  # car_name jeep



# my_dict = {{1 : 2, 2: 3} : [1, 2, 3, 4], 'numbers_2' : [2, 3, 60], 'car_name' : 'jeep'}

# print(my_dict)  # Traceback (most recent call last):
#                 # File "/home/carl/Github/DjangoPython/Django Python Class Notes/Dict For.py", line 145, in <module>
#                 #     my_dict = {{1 : 2, 2: 3} : [1, 2, 3, 4], 'numbers_2' : [2, 3, 60], 'car_name' : 'jeep'}
#                 # TypeError: unhashable type: 'dict'



# my_dict = {1 : [1, 2, 3, 4], 'numbers_2' : [2, 3, 60], 'car_name' : 'jeep'}

# print(my_dict)  # {1: [1, 2, 3, 4], 'numbers_2': [2, 3, 60], 'car_name': 'jeep'}



# my_dict = {1 : {'name' : 'car'}, 'numbers_2' : [2, 3, 60], 'car_name' : 'jeep'}

# print(my_dict)  # {1: {'name': 'car'}, 'numbers_2': [2, 3, 60], 'car_name': 'jeep'}



my_dict = {
    'names' : ['carl', 'rich', 'roger', 'sis'],
    'numbers' : [1, 2, 3, 4, 5, 6],
    'colors' : 'yellow',
}
# for k, v in my_dict.items():
#     print(k, v)  # names ['carl', 'rich', 'roger', 'sis']
#                 # numbers [1, 2, 3, 4, 5, 6]
#                 # colors yellow

# for k, v in my_dict.items():
#     print(k, v)  # Class Notes/Dict For.py"
#                 # names ['carl', 'rich', 'roger', 'sis']
#                 # numbers [1, 2, 3, 4, 5, 6]
#                 # colors yellow
# a = my_dict['names']

# a = my_dict['names']
# print(a)  # ['carl', 'rich', 'roger', 'sis']

a = my_dict['names']
print(my_dict['numbers'])  # [1, 2, 3, 4, 5, 6]
a = 'salam'
print(a)