"""
finished  database starts at line 54



"""

# name = str(input('please enter your name : '))

# l = []
# l.append(name)  # rich
# print(l)  # ['rich']


# # SPLIT  **************************************************** ONE  ** using spaces
# n = 'rich carl sandra roger beth jess'
# name = n.split()
# print(name)
# l = []
# print(l)  # ['rich', 'carl', 'sandra', 'roger', 'beth', 'jess']
#           # []


# # SPLIT  **************************************************** TWO  ** using periods and commas
# n = 'rich.carl.sandra.roger,beth,jess'
# name = n.split(',')
# print(name)
# l = []
# print(l)  # ['rich', 'carl', 'sandra', 'roger', 'beth', 'jess']
#           # []


# database = [
#     ['rich', 'carl', 'sandra'], 
#     ['roger', 'beth', 'jess'],
#     [81, 77, 80],
# ]
# print(database)  # [['rich', 'carl', 'sandra'], ['roger', 'beth', 'jess'], [81, 77, 80]]


# database = [
#     ['rich', 'carl', 'sandra'], 
#     ['roger', 'beth', 'jess'],
#     [81, 77, 80],
# ]
# first_name = database[0]
# last_name = database[1]
# ages = database[2]f

# input_1 = str(input('Please enter user or pass : '))  # f
# if input_1 == 'f' or input_1 == 'firstname':
#     print(first_name)  # ['rich', 'carl', 'sandra']

database = [
    ['rich', 'carl', 'sandra'], 
    ['roger', 'beth', 'jess'],
    [81, 77, 80],
]
first_name = database[0]
last_name = database[1]
ages = database[2]

input_1 = str(input('Please enter user or pass : '))  # f
if input_1 == 'f' or input_1 == 'firstname':
    print(first_name)  # ['rich', 'carl', 'sandra']
elif input_1 == 'l' or input_1 == 'lastname':
    print(last_name)
elif input_1 == 'ages':
    print(ages)
else:
    print('please enter the correct info ')

# PS C:\Users\pgold\Github\DjangoPython> & C:/Users/pgold/anaconda3/python.exe "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/List Split.py"
# Please enter user or pass : f
# ['rich', 'carl', 'sandra']
# PS C:\Users\pgold\Github\DjangoPython> & C:/Users/pgold/anaconda3/python.exe "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/List Split.py"
# Please enter user or pass : firstname
# ['rich', 'carl', 'sandra']
# PS C:\Users\pgold\Github\DjangoPython> & C:/Users/pgold/anaconda3/python.exe "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/List Split.py"
# Please enter user or pass : lastname
# ['roger', 'beth', 'jess']
# PS C:\Users\pgold\Github\DjangoPython> & C:/Users/pgold/anaconda3/python.exe "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/List Split.py"
# Please enter user or pass : l
# ['roger', 'beth', 'jess']
# PS C:\Users\pgold\Github\DjangoPython> & C:/Users/pgold/anaconda3/python.exe "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/List Split.py"
# Please enter user or pass : ages
# [81, 77, 80]
# PS C:\Users\pgold\Github\DjangoPython> & C:/Users/pgold/anaconda3/python.exe "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/List Split.py"
# Please enter user or pass : dyyff
# please enter the correct info