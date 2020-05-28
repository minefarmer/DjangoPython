# a = [1, 2, 3] + [4, 5, 6]
# print(a) # [1, 2, 3, 4, 5, 6]

# print('HI ' * 3)  # HI HI HI   *** need space after the 'HI '

# print(str([1, 2]) + '34')  # [1, 2]34

# a = list('34'); print(a)  # ['3', '4']

# a = [1, 2, 3]
# >>> a = [1, 2, 3]
# >>> 3 in a
# True
# >>> '3' in a
# False
# >>> int('3') in a
# True

# for x in [1, 2, 3,]:
#     print(x, end=' ')  # 1 2 3 sh-5.0$ 

# for x in [1, 2, 3,]:
#     print(x)  # 1 
#               # 2
#               # 3



# rec = [i * 4 for i in 'spam']
# print(rec)  # ['ssss', 'pppp', 'aaaa', 'mmmm']

# res = []
# for c in 'spam':
#     res.append(c * 4)
# print(res)  # ['ssss', 'pppp', 'aaaa', 'mmmm']



a = list(map(abs, [1, 2, -4, -70, -23]))  # abs turns muses into plusses
print(a)  # [1, 2, 4, 70, 23]

b = -90
print(abs(b))  # 90  ** no minus