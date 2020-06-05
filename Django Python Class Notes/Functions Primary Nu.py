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


def Prime_n(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    return prime
a = int(input('please enter a number :'))  # 6   ** second run 60

if True:
    print(a, ' is prime')  # 6  is prime     ** second run  60  is prime