# n = 'carl matson sandra matson roger matson'
# name = n.split()
# l = []
# l.append(name)
# print(l)  # [['carl', 'matson', 'sandra', 'matson', 'roger', 'matson']]



# database = [['sandra', 'roger', 'carl'],
#             ['matson', 'matson', 'matson'],
#             [80, 78, 81],
# ]

# print(database)  # [['sandra', 'roger', 'carl'], ['matson', 'matson', 'matson'], [80, 78, 81]]



database = [['sandra', 'roger', 'carl'],
            ['biskup', 'matson', 'matson'],
            [80, 78, 81],
]
first_name = database[0]
family_name = database[1]
ages = database[2]

input_1 = str(input('please inter user or pass : '))
if input_1 == 'f' or input_1 == 'firstname':
    print(first_name)
elif input_1 == "l" or input_1 == 'lastname':
    print(family_name)
elif input_1 == 'ages':
    print(ages)
else:
    print('please enter the currect info.')