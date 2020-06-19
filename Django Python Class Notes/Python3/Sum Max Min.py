# Using a minimum amount of programing  88
# 
# 


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # for i in my_list:
# #     print(i)    # 1
# #                 # 2
# #                 # 3
# #                 # 4
# #                 # 5
# #                 # 6
# #                 # 7
# #                 # 8
# #                 # 9
# #                 # 10
    
# # for i in my_list:
# #     m = i ** 2
# #     print(m)    # 1
# #                 # 4
# #                 # 9
# #                 # 16
# #                 # 25
# #                 # 36
# #                 # 49
# #                 # 64
# #                 # 81
# #                 # 100



# # my_list = list(range(1, 9))  # ***************************

# # for i in my_list:
# #     m = i ** 2
# #     print(m)    # 1
# #                 # 4
# #                 # 9
# #                 # 16
# #                 # 25
# #                 # 36
# #                 # 49
# #                 # 64
                
                
                
# squares = []   # print is outside the for loop**********************

# for value in range(1, 11):  
#     square = value**2
#     squares.append(square)
# print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# squares = []   # print is inside the for loop *******************************

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
# print(minimum)    # 1

# print(max(digits))  # 10

# print(sum(digits))  # 55



# Using a mimimum amount of programming  ************************
# my_list = [i for i in range(1, 11)]
# print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = [i**2 for i in range(1, 11)]
# print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

players = ['roger', 'Coletta', 'tom', 'tom', 'sandra', 'jess']

for player in players[:3]:
    print(player.title())   # Roger
                            # Coletta
                            # Tom