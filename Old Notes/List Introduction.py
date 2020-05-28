# List introduction and How to insert, pop, remove, append

list_1 = ['rich', 'ali', 'roger', 'sandra']
print(list_1)  # ['rich', 'ali', 'roger', 'sandra']

print(list_1[0])  # rich

d = list_1[0]
a = list_1[1]
b = list_1[2]
c = list_1[3]
print(a, b, c, d)  # ali roger sandra rich

a = list_1[0]
a = a.title()
print(a)  # Rich

a = list_1[1]

b = list_1[-1]
c = list_1[-2]
print(c)  # roger

print(len(list_1))  # 4

list_1.append('car')
print(list_1)  # ['rich', 'ali', 'roger', 'sandra', 'car']

list_1.insert(0,'bike')
print(list_1)  # ['bike', 'rich', 'ali', 'roger', 'sandra', 'car']

list_1.insert(2, 'truck')
print(list_1)  # ['bike', 'rich', 'truck', 'ali', 'roger', 'sandra', 'car']

list_1.remove('rich')
print(list_1)  # ['bike', 'truck', 'ali', 'roger', 'sandra', 'car']

list_1.insert(2, 'car')
a = list_1.pop(0)
print(list_1)
print(a)  # bike