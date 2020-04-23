# name = str(input('please enter your name : '))

# l = []
# l.append(name)
# print(l)  # ['rich matson root admin']


# n = 'rich matson sandra matson roger matson'
# name = n.split()
# print(name)
# l = []
# print(l)  # ['rich', 'matson', 'sandra', 'matson', 'roger', 'matson']


# n = 'rich.matson.sandra.matson.roger.matson'
# name = n.split('.')
# print(name)  # ['rich', 'matson', 'sandra', 'matson', 'roger', 'matson']



# database = [
#     ['carl', 'sandra', 'roger'],
#     ['matson', 'matson', 'matson'],
#     [81, 80, 78,],
# ]

# print(database)  # [['carl', 'sandra', 'roger'], ['matson', 'matson', 'matson'], [81, 80, 78]]


database = [
    ['carl', 'sandra', 'roger'],
    ['matson', 'matson', 'matson'],
    [81, 80, 78,],
]
first_name = database[0]
family_name = database[1]
ages = database[2]

input_1 = str(input('please enter user or pass : '))
if input_1 == 'f' or input_1 == 'firstname':
    print(first_name)
elif input_1 == 'l' or input_1 == 'lastname':
    print(family_name)
elif input_1 == 'ages':
    print(ages)
else:
    print('please enter the correct info')