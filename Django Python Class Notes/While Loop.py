# 
# 
# 
# 
# 

# i = 0
# while i < 10:
#     print(i)    # 0
#                 # 1
#                 # 2
#                 # 3
#                 # 4
#                 # 5
#                 # 6
#                 # 7
#                 # 8
#                 # 9
#     i = i + 1

# i = 0
# while i < 11:
#     if i % 2 == 0:
#         print(i)    # 0
#                     # 2
#                     # 4
#                     # 6
#                     # 8
#                     # 10
#     i = i + 1

# i = 0
# while i < 11:
#     if i % 2 == 0:
#         print(i)    # 0
#     print('i ++')   # 1 ++
#                     # i ++
#                     # 2
#                     # i ++
#                     # i ++
#                     # 4
#                     # i ++
#                     # i ++
#                     # 6
#                     # i ++
#                     # i ++
#                     # 8
#                     # i ++
#                     # i ++
#                     # 10
#                     # i ++
#     i = i + 1
    

sum = 'matson'
i = 0

# print(sum[0])  # m
# print(sum[2])  # t
# print(sum[4])  # o

while i < len(sum):
    print('i ====> ', i)
    print(sum[i])   # i ====>  0
                    # m
                    # i ====>  1
                    # a
                    # i ====>  2
                    # t
                    # i ====>  3
                    # s
                    # i ====>  4
                    # o
                    # i ====>  5
                    # n
    i = i + 1