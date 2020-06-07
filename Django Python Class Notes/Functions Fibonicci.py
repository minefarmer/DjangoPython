# fibonicci  110  ** do not use
# fibonicci using while  ** perferred
# 
# 
# 

# def Prime_n(n):
#     prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#     return prime
# a = int(input('please enter a number :'))  # 17  ** second run 18

# print(Prime_n(a))  # True    ** second run False


# def Prime_n(n):
#     prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#     return prime
# a = int(input('please enter a number :'))  # 4

# print(Prime_n(a), ' is prime')  # False is prime


# def Prime_n(n):
#     prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#     return prime
# a = int(input('please enter a number :'))  # 4   ** second run 17

# if Prime_n(a):
#     print(a, ' is prime')  # nothing for 4   ** second run  17  is prime


# def Prime_n(n):
#     prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#     return prime
# a = int(input('please enter a number :'))  # 6   ** second run 60

# if True:
#     print(a, ' is prime')  # 6  is prime     ** second run  60  is prime


# def Prime_n(n):
#     prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#     return prime

# for i in range(2, 25):
#     if Prime_n(i):
#         print(i, ' is prime')
#     else:
#         print(i, ' IS NOT PRIME')  # 2  is prime
#                                     # 3  is prime
#                                     # 4  IS NOT PRIME
#                                     # 5  is prime
#                                     # 6  IS NOT PRIME
#                                     # 7  is prime
#                                     # 8  IS NOT PRIME
#                                     # 9  IS NOT PRIME
#                                     # 10  IS NOT PRIME
#                                     # 11  is prime
#                                     # 12  IS NOT PRIME
#                                     # 13  is prime
#                                     # 14  IS NOT PRIME
#                                     # 15  IS NOT PRIME
#                                     # 16  IS NOT PRIME
#                                     # 17  is prime
#                                     # 18  IS NOT PRIME
#                                     # 19  is prime
#                                     # 20  IS NOT PRIME
#                                     # 21  IS NOT PRIME
#                                     # 22  IS NOT PRIME
#                                     # 23  is prime
#                                     # 24  IS NOT PRIME


# def Prime_n(n):
#     prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#     return prime

# sum = 0

# for i in range(2, 1000):
#     if Prime_n(i):
#         # print(i, ' is prime')
#         sum += 1
#     else:
#         print(i, ' IS NOT PRIME')  # 1 - 999 numbers that are not prime
# print(sum)  # 168  *** total prime numpers





#  fibonicci
# fibonicci is; 1 + 2 = 3, 2 + 3 = 5  # etc
#  1 2 3 5 8 13 21 34 55 89 144

# for i in range(100):
#     print(i)  # 0 - 99  ** one number per line



first = 1
second = 2

# for i in range(10):
#     print(first)  # 1
#                     # 2
#                     # 3
#                     # 5
#                     # 8
#                     # 13
#                     # 21
#                     # 34
#                     # 55
#                     # 89
#     new = first + second
#     first = second
#     second = new




while first < 40:
    print(first)  # 1
                    # 2 
                    # 3 
                    # 5 
                    # 8 
                    # 13
                    # 21
                    # 34
    new = first + second
    first = second
    second = new