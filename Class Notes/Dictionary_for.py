# d = {
#     'key_1' : {'name' : 'rich', 'age' : 81, 'f_name' : 'matson'},
#     'key_2' : {'car' : 'audi', 'max speed' : 330, 'color' 'color' : 'black'},
#     'key_3' : {'movie1' : 2003, 'movie2' : 2016}
# }

# # print(d['key_1'])  # {'name': 'rich', 'age': '81', 'f_name': 'matson'}

# # for k, v in f.items():
# for key, value in d.items():
#     # print(key)  # key_1
#     #             # key_2
#     #             # key_3
    
#     # print(key, value)   # key_1 {'name': 'rich', 'age': 81, 'f_name': 'matson'}
#     #                     # key_2 {'car': 'audi', 'max speed': 330, 'colorcolor': 'black'}
#     #                     # key_3 {'movie1': 2003, 'movie2': 2016}
    
#     # print(d[key])   # {'name': 'rich', 'age': 81, 'f_name': 'matson'}
#     #                 # {'car': 'audi', 'max speed': 330, 'colorcolor': 'black'}
#     #                 # {'movie1': 2003, 'movie2': 2016}
    
#     if key == 'key_3':
#         print(value)  # {'movie1': 2003, 'movie2': 2016}



d = {
    'movie1' : 1997,
    'movie2' : 2003,
    'movie3' : 2003,
    'movie4' : 2019,
    'movie5' : 1997,
    'movie6' : 2019,
}

# for k, v in d.items():
#     if v == 2003:
#         print(k)  # movie2
#                   # movie3

# for k, v in d.items():
#     if v == 2019:
#         print(k)  # movie4
#                   # movie6


# input_1 = input('please enter a year : ')  **** see below for alt way

# for k, v in d.items():
#     if v == int(input_1):
    
#         print(k)  # movie4
#                   # movie6



input_1 = int(input('please enter a year : '))  # 2003

my_list = [k for (k, v) in d.items() if v == input_1]
print(my_list)  # ['movie2', 'movie3']
