# 
# 
# 
# 
# my_dict ={'name' : 'rich', 'age' : 81, 'color': 'red'}
# print(my_dict['name'])  # rich
# print(my_dict['age'])  # 81

# my_dict ={'name' : 'rich', 'age' : 81, 'color': 'red'};print(my_dict['color'])  # red
# print(my_dict['name'])  # rich
# print(my_dict['age'])  # 81

# test = {'x_position' : 0, 'y_position' : 25}
# print(test['x_position'])  # 0
# print(test['y_position'])  # 25

# print('the location is ', test['x_position'], test['y_position'])  # the location is  0 25

# test = {'x_position' : 0, 'y_position' : 25}
# test['speed'] = 80
# print(test)  # {'x_position': 0, 'y_position': 25, 'speed': 80}

# test = {
#     'rich' : 'python',
#     'sara' : 'c',
#     'jess' : 'ruby',
#     'beth' : 'perl',
# }
# print(test)  # {'rich': 'python', 'sara': 'c', 'jess': 'ruby', 'beth': 'perl'}

# del test['rich']
# print(test)  # {'sara': 'c', 'jess': 'ruby', 'beth': 'perl'}

# test['rich'] = 'c++'
# print(test)  # {'rich': 'c++', 'sara': 'c', 'jess': 'ruby', 'beth': 'perl'}
# test['speed'] = 80
# print(test) {'rich': 'c++', 'sara': 'c', 'jess': 'ruby', 'beth': 'perl', 'speed': 80}


# test = {
#     1 : 'python',
#     'rich' : 'python',
#     'sara' : 'c',
#     'jess' : 'ruby',
#     'beth' : 'perl',
# }

# print(test)  # {1: 'python', 'rich': 'python', 'sara': 'c', 'jess': 'ruby', 'beth': 'perl'}

# test = {
#     [1, 2, 3] : 'python',
#     'rich' : 'python',
#     'sara' : 'c',
#     'jess' : 'ruby',
#     'beth' : 'perl',
# }

# print(test)  # {1: 'python', 'rich': 'python', 'sara': 'c', 'jess': 'ruby', 'beth': 'perl'}
# print(test)     # Traceback (most recent call last):
                # File "/home/carl/Github/DjangoPython/Django Python Class Notes/Dict.py", line 55, in <module>
                #     'beth' : 'perl',
                # TypeError: unhashable type: 'list'
                
# test = {
#     {'ali'} : 'python',
#     'rich' : 'python',
#     'sara' : 'c',
#     'jess' : 'ruby',
#     'beth' : 'perl',
# }
# print(test)  # Traceback (most recent call last):
#             # File "/home/carl/Github/DjangoPython/Django Python Class Notes/Dict.py", line 69, in <module>
#             #     'beth' : 'perl',
#             # TypeError: unhashable type: 'set'

# test = {
#     'my_list' : [1, 2, 3, 4, 5],
#     'rich' : 'python',
#     'sara' : 'c',
#     'jess' : 'ruby',
#     'beth' : 'perl',
# }
# print(test)  # {'my_list': [1, 2, 3, 4, 5], 'rich': 'python', 'sara': 'c', 'jess': 'ruby', 'beth': 'perl'}

test = {
    'my_list' : {'name' : 'rich'},
    'rich' : 'python',
    'sara' : 'c',
    'jess' : 'ruby',
    'beth' : 'perl',
}
print(test)  # {'my_list': {'name': 'rich'}, 'rich': 'python', 'sara': 'c', 'jess': 'ruby', 'beth': 'perl'}