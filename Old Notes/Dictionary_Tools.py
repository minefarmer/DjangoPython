d = {
    'name' : 'rich',
    'age' : '81',
    'family_name' : 'matson'
}

# print(d.keys())  # dict_keys(['name', 'age', 'family_name'])

l = [1, 2, 3, 4, 5, 6]
# print(l[4])  # 5

# print(d.values())  # dict_values(['rich', '81', 'matson'])

# print(d.items())  # dict_items([('name', 'rich'), ('age', '81'), ('family_name', 'matson')])

# print(d['name'])  # rich

# print(d['name']);print(d.get('name'))  # rich

# print(d.get('name', 20))  # rich

# del d['name']
# print(d)  # {'age': '81', 'family_name': 'matson'}

# d.pop('name')
# print(d)  # {'age': '81', 'family_name': 'matson'}

# a = d.pop('name');print(d)  # {'age': '81', 'family_name': 'matson'}

# a = d.pop('name');print(d)  # {'age': '81', 'family_name': 'matson'}
# print(a);print(type(a)) # rich
#                         # <class 'str'>

#  saving a copy of an original when I want to change the original.
# d2 = d.copy();print(d2)  # {'name': 'rich', 'age': '81', 'family_name': 'matson'}

# d2 = d.copy();print(d2)
# d2['name'] = 'carl';print(d2)  # {'name': 'rich', 'age': '81', 'family_name': 'matson'}  *** d
#                                # {'name': 'carl', 'age': '81', 'family_name': 'matson'}  *** d2

# updating the dict
d2 = {}
d2.update(d);print(d2)  # {'name': 'rich', 'age': '81', 'family_name': 'matson'}