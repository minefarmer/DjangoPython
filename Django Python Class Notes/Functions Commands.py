# LAMBDA  27
# # LAMBDA  return based on a condition, *** use filter command 34
# 
# 
# 
# 
# 
# 
# 
# 
# 

# def add_five(x):
#     return x + 5
# nums= [11, 22, 33, 44, 55]
# result = list(map(add_five, nums))
# print(result)  # [16, 27, 38, 49, 60]

# def add_five(x):
#     return x + 5
# nums= [11, 22, 33, 44, 55]
# result = map(add_five, nums)
# print(result)  # <map object at 0x7f9a2d8c2450>



# # LAMBDA
# nums= [11, 22, 33, 44, 55]

# result = list(map(lambda x: x +5, nums))
# print(result)  # [16, 27, 38, 49, 60]


# LAMBDA  return based on a condition  *** use filter command
# nums= [11, 22, 33, 44, 55
# result = list(filter(lambda x: x % 2 == 0, nums))
# print(result)  # [22, 44]


# def add_five(x):
#     if x % 2 == 0:
#         return x
# nums= [11, 22, 33, 44, 55]
# result = list(filter(add_five, nums))
# print(result)  # [22, 44]

# res = list(filter(lambda x: x % 2 == 0, nums))
# print(res)  # [22, 44]


def add_five(x):
    if x % 2 == 0:
        return x
nums= [i for i in range(2, 100)]

result = list(filter(add_five, nums))
print(result)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

# res = list(filter(lambda x: x % 2 == 0, nums))  # used 2 == 0
# print(res)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

res = list(filter(lambda x: x % 3 == 0, nums))  # used 3 == 0 
print(res)  # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]