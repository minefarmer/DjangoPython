# my_dict = {'name' : 'rich', 'age' : 81, 'color': 'red'};print(my_dict['color'])  # red
# print(my_dict['name'])  # rich
# print(my_dict['age'])  # 81

# test = {'x_position' : 0, 'y_position' : 25}
# print(test)  # {'x_position': 0, 'y_position': 25}
# print(test['x_position'])  # 0
# print(test['y_position'])  # 25
# print('the location is ', test['x_position'], test['y_position'])  # the location is  0 25


# test = {'x_position' : 0, 'y_position' : 25}
# test['speed'] = 80  # {'x_position': 0, 'y_position': 25, 'speed': 80}
# print(test)


# test = {
#     'rich' : 'python',
#     'sara' : 'c',
#     'pedramm' :'ruby',
#     'parham' : 'perl'
# }
# # print(test)  # {'rich': 'python', 'sara': 'c', 'pedramm': 'ruby', 'parham': 'perl'}


# test['rich'] = 'C++'
# print(test)  # {'rich': 'C++', 'sara': 'c', 'pedramm': 'ruby', 'parham': 'perl'}
# test['speed'] = 80
# print(test)  # {'rich': 'C++', 'sara': 'c', 'pedramm': 'ruby', 'parham': 'perl', 'speed': 80}


# test = {
#     'rich' : 'python',
#     'sara' : 'c',
#     'pedramm' :'ruby',
#     'parham' : 'perl'
# }
# # print(test)  # {'rich': 'python', 'sara': 'c', 'pedramm': 'ruby', 'parham': 'perl'}


# test['rich'] = 'C++'
# print(test)  # {'rich': 'C++', 'sara': 'c', 'pedramm': 'ruby', 'parham': 'perl'}
# test['speed'] = 80
# print(test)  # {'rich': 'C++', 'sara': 'c', 'pedramm': 'ruby', 'parham': 'perl', 'speed': 80}


# test = {
#     1 : 'python',
#     'sara : 'c',
#     'pedramm' :'ruby',
#     'parham' : 'perl'
# }
# print(test)  # {1: 'python', 'sara': 'c', 'pedramm': 'ruby', 'parham': 'perl'}


# test = {
#     'rich : 'python',
#     [1, 2, 3] : 'c',
#     'pedramm' :'ruby',
#     'parham' : 'perl'
# }
# print(test)  # Traceback (most recent call last):
# #  File "/home/carl/Github/DjangoPython/Class Notes/Dictionary_intro.py", line 60, in <module>
# #   'parham' : 'perl'
# #  TypeError: unhashable type: 'list'


# test = {
#     'rich' : 'python',
#     {'rich : 3'} : 'c',
#     'pedramm' :'ruby',
#     'parham' : 'perl'
# }
# print(test)  # Traceback (most recent call last):  ******** Shows error in wrong place
#             # File "/home/carl/Github/DjangoPython/Class Notes/Dictionary_intro.py", line 72, in <module>
#             #     'parham' : 'perl'
#             # TypeError: unhashable type: 'set'

test = {
    'my_list' : [1, 23, 4, 5],
    'sara' : 'c',
    'pedramm' :'ruby',
    'parham' : 'perl'
}
print(test)  # {'my_list': [1, 23, 4, 5], 'sara': 'c', 'pedramm': 'ruby', 'parham': 'perl'}
test['speed'] = 80
print(test)  # {'my_list': [1, 23, 4, 5], 'sara': 'c', 'pedramm': 'ruby', 'parham': 'perl', 'speed': 80}
