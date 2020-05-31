l1 = ['ali', 'rich', 'beth', 'carl', 'rich', 'maryam']
l2 = ['maryam', 'ali' 'maryam', 'ali', 'pedram']
l3 = []

# for i in l1:
#     print(i)    # ali
#                 # rich
#                 # beth
#                 # carl
#                 # rich

# roundl = 1

# for i in l1:
#     print('now is ', roundl)
#     print(i)    
#             # now is  1
#             # ali
#             # now is  2
#             # rich
#             # now is  3
#             # beth
#             # now is  4
#             # carl
#             # now is  5
#             # rich

# for a in l1:
#     print('round ', roundl)
#     for b in l2:     
#         print(a)
#     roundl += 1
# # total printed # round  1
#                 # ali
#                 # ali
#                 # ali
#                 # ali
#                 # round  2
#                 # rich
#                 # rich
#                 # rich
#                 # rich
#                 # round  3
#                 # beth
#                 # beth
#                 # beth
#                 # beth
#                 # round  4
#                 # carl
#                 # carl
#                 # carl
#                 # carl
#                 # round  5
#                 # rich
#                 # rich
#                 # rich
#                 # rich

# for a in l1:
#     print('round ', roundl)
#     for b in l2:
#         print(b)   
#         print(a)
#     roundl += 1
# # total printed # round  1
#                 # sandra
#                 # ali
#                 # maryam
#                 # ali
#                 # john
#                 # ali
#                 # chris
#                 # ali
#                 # coletta
#                 # ali
#                 # round  2
#                 # sandra
#                 # rich
#                 # maryam
#                 # rich
#                 # john
#                 # rich
#                 # chris
#                 # rich
#                 # coletta
#                 # rich
#                 # round  3
#                 # sandra
#                 # beth
#                 # maryam
#                 # beth
#                 # john
#                 # beth
#                 # chris
#                 # beth
#                 # coletta
#                 # beth
#                 # round  4
#                 # sandra
#                 # carl
#                 # maryam
#                 # carl
#                 # john
#                 # carl
#                 # chris
#                 # carl
#                 # coletta
#                 # carl
#                 # round  5
#                 # sandra
#                 # rich
#                 # maryam
#                 # rich
#                 # john
#                 # rich
#                 # chris
#                 # rich
#                 # coletta
#                 # rich

roundl = 1

# for a in l1:
#     print('round ', roundl)
#     for b in l2:
#         if a == b:
#             l3.append(a)
# print(l3)
# # total printed # round  1
#                 # round  1
#                 # round  1
#                 # round  1
#                 # round  1
#                 # ['ali']   ********* video shows  ['ali', 'pedram']

for a in l1:
    # print('round ', roundl)
    for b in l2:
        if a == b:
            l3.append(a)
print(l3)
# total printed # ['ali', 'maryam']   ********* video shows  ['ali', 'pedram', 'maryam']