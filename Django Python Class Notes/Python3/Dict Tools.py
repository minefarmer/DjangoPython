# d = {
#     'name' : 'rich',
#     'age' : 81,
#     'family_name' : 'matson'
# }

# print(d.keys())  # dict_keys(['name', 'age', 'family_name'])
# print(d.keys()[0])  # Traceback (most recent call last):
#                     # File "/home/carl/Github/DjangoPython/Django Python Class Notes/Dict Tools.py", line 8, in <module>
#                     #     print(d.keys()[0])
#                     # TypeError: 'dict_keys' object is not subscriptable

# l = [1, 32, 3, 4, 5, 6]
# print(l[4])  # 5



d = {
    'name' : 'rich',
    'age' : 81,
    'family_name' : 'matson'
}
# print(d.values())  # dict_values(['rich', 81, 'matson'])
# print(d.items())  # dict_items([('name', 'rich'), ('age', 81), ('family_name', 'matson')])

# print(d['name']);print(d.get('name'))  # rich
#                                        # rich

# print(d['name']);print(d.get('name'))  # rich
#                                        # None

# print(d['name1']);print(d.get('name')) # Traceback (most recent call last):
#                                         # File "/home/carl/Github/DjangoPython/Django Python Class Notes/Dict Tools.py", line 29, in <module>
#                                         #     print(d['name1']);print(d.get('name')) # rich
#                                         # KeyError: 'name1'

# print(d['name']);print(d.get('name1', 'name1 is not in d'))  # rich
#                                                              #  name1 is not in d

# print(d.get('name', 20))  # rich

# print(d.get('name1', 20))  # 20

# del d['name']
# print(d)  # {'age': 81, 'family_name': 'matson'}

# a = d.pop('name');print(d)  # {'age': 81, 'family_name': 'matson'}

# a = d.pop('name');print(d)  # {'age': 81, 'family_name': 'matson'}
# print(a);print(type(a))  # rich
#                          # <class 'str'>

# d2 = d.copy();print(d2)  # {'name': 'rich', 'age': 81, 'family_name': 'matson'}
# d2['name'] = 'carl';print(d2)  # {'name': 'carl', 'age': 81, 'family_name': 'matson'}

d2 ={}
d2.update(d);print(d2)  # {'name': 'rich', 'age': 81, 'family_name': 'matson'}
