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


# database = [
#     ['carl', 'sandra', 'roger'],
#     ['matson', 'matson', 'matson'],
#     [81, 80, 78,],
# ]
# first_name = database[0]
# family_name = database[1]
# ages = database[2]

# input_1 = str(input('please enter user or pass : '))
# if input_1 == 'f' or input_1 == 'firstname':
#     print(first_name)
# elif input_1 == 'l' or input_1 == 'lastname':
#     print(family_name)
# elif input_1 == 'ages':
#     print(ages)
# else:
#     print('please enter the correct info')



l1 = ['ali', 'reza', 'pedram', 'parham']
l2 = ['maryam', 'john', 'chris', 'ali', 'pedram']
l3 = []

roundl = 1

# for a in l1:
#     print('round ', roundl)
#     for b in l2:

#         # print(a)  # round  1
#                     # round  6
#                     # round  11
#                     # round  16
#                     # round  21
#         roundl += 1


# for a in l1:
#     print('round ', roundl) # round  1
#                             # ali
#                             # ali
#                             # ali
#                             # ali
#                             # ali
#                             # round  6
#                             # reza
#                             # reza
#                             # reza
#                             # reza
#                             # reza
#                             # round  11
#                             # pedram
#                             # pedram
#                             # pedram
#                             # pedram
#                             # pedram
#                             # round  16
#                             # parham
#                             # parham
#                             # parham
#                             # parham
#                             # parham
#                             # round  21
#                             # mohamad
#                             # mohamad
#                             # mohamad
#                             # mohamad
#                             # mohamad
#     for b in l2:

#         # print(a)  # 
#         roundl += 1


# for a in l1:
#     print('round ', roundl) 
#     for b in l2:
#         print(a)    # round  1
#                     # ali
#                     # ali
#                     # ali
#                     # ali
#                     # ali
#                     # round  2
#                     # reza
#                     # reza
#                     # reza
#                     # reza
#                     # reza
#                     # round  3
#                     # pedram
#                     # pedram
#                     # pedram
#                     # pedram
#                     # pedram
#                     # round  4
#                     # parham
#                     # parham
#                     # parham
#                     # parham
#                     # parham
#                     # round  5
#                     # mohamad
#                     # mohamad
#                     # mohamad
#                     # mohamad
#                     # mohamad
#     roundl += 1



# for a in l1:
#     print('round ', roundl) 
#     for b in l2:
#         print(b)    # round  1
#         print(a)    # round  1
#                     # maryam
#                     # ali
#                     # john
#                     # ali
#                     # chris
#                     # ali
#                     # ali
#                     # ali
#                     # pedram
#                     # ali
#                     # round  2
#                     # maryam
#                     # reza
#                     # john
#                     # reza
#                     # chris
#                     # reza
#                     # ali
#                     # reza
#                     # pedram
#                     # reza
#                     # round  3
#                     # maryam
#                     # pedram
#                     # john
#                     # pedram
#                     # chris
#                     # pedram
#                     # ali
#                     # pedram
#                     # pedram
#                     # pedram
#                     # round  4
#                     # maryam
#                     # parham
#                     # john
#                     # parham
#                     # chris
#                     # parham
#                     # ali
#                     # parham
#                     # pedram
#                     # parham
#                     # round  5
#                     # maryam
#                     # mohamad
#                     # john
#                     # mohamad
#                     # chris
#                     # mohamad
#                     # ali
#                     # mohamad
#                     # pedram
#                     # mohamad
#     roundl += 1


for a in l1:
    #print('round ', roundl) 
    for b in l2:
        if a == b:
            l3.append(a)

    print(l3)   # ['ali']
                # ['ali']
                # ['ali', 'pedram']
                # ['ali', 'pedram']
                # ['ali', 'pedram']

# With Maryam added to the end list l1
# ['ali']
# ['ali']
# ['ali', 'pedram']
# ['ali', 'pedram']
# ['ali', 'pedram']
# ['ali', 'pedram', 'maryam']