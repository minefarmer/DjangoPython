# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in my_list:
#     print(i)  # 1 - 10

# for i in my_list:
#     m = i ** 2
#     print(m)  # 1
#             # 4
#             # 9
#             # 16
#             # 25
#             # 36
#             # 49
#             # 64
#             # 81
#             # 100



# my_list = list(range(1, 11))

# for i in my_list:
#     m = i ** 2
#     print(m)  # 1
#             # 4
#             # 9
#             # 16
#             # 25
#             # 36
#             # 49
#             # 64
#             # 81
#             # 100   print(m)



# squares = []

# for value in range(1, 11):
#     square = value**2
#     squares.append(square)
# print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  **** print outside the for loop

# for value in range(1, 11):
#     square = value**2
#     squares.append(square)
#     print(squares)  # [1]   ****** print is inside the loop
#                     # [1, 4]
#                     # [1, 4, 9]
#                     # [1, 4, 9, 16]
#                     # [1, 4, 9, 16, 25]
#                     # [1, 4, 9, 16, 25, 36]
#                     # [1, 4, 9, 16, 25, 36, 49]
#                     # [1, 4, 9, 16, 25, 36, 49, 64]
#                     # [1, 4, 9, 16, 25, 36, 49, 64, 81]
#                     # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for value in range(1, 11):
#     squares.append(value**2)
#     print(squares)  # [1] 
#                     # [1, 4]
#                     # [1, 4, 9]
#                     # [1, 4, 9, 16]
#                     # [1, 4, 9, 16, 25]
#                     # [1, 4, 9, 16, 25, 36]
#                     # [1, 4, 9, 16, 25, 36, 49]
#                     # [1, 4, 9, 16, 25, 36, 49, 64]
#                     # [1, 4, 9, 16, 25, 36, 49, 64, 81]
#                     # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
                    



# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(min(digits))  # 1

# minimum = []
# minimum.append(min(digits))
# print(minimum)  # 1

# print(max(digits))  # 10

# print(sum(digits))  # 55



# my_list = digits = [i for i in range(1, 11)]

# print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# my_list = [i**2 for i in range(1, 11)]

# print(my_list)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]




players = ['charles', 'martina', 'michael', 'eli', 'chris', 'john']

for player in players[:3]:
    print(player.title())   # Charles
                            # Martina
                            # Michael

