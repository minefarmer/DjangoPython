# lambda 30
#   normal function 37
#   lambda function 43
#   #  normal function   ***** Example 2  49
#   # Lambda function example 3  60

# def test(n):
#     return n ** 2

# print(test(5))  # 25


# def apply_ones(func, arg):
#     return func(arg)

# def add_five(x):
#     return x + 5

# print(apply_ones(add_five, 10))  # 15


# def apply_twice(func, arg):
#     return func(func(arg))
# def add_five(x):
#     return x + 5
# print(apply_twice(add_five, 10))  # 20



# def test(f, arg):
#     return f(arg)

# print(test(lambda x: 2*x, 5))  # 10



# #  normal function
# def test(x):
#     return x**2 + 5*x + 4
# print(test(-4))  # 0


#  lambda function   ***  This is a duplicate of the above normal function

# print((lambda x: x**2 + 5*x + 4)(-4))  # 0



# #  normal function   ***** Example 2
# def test(x):
#     return x**2 + 5*x + 4
# print(test(5))  # 54


# #  lambda function   ***  This is a duplicate of the above normal function

# print((lambda x: x**2 + 5*x + 4)(5))  # 54


# Lambda function example 3
# a = (lambda  x: x*x)(40)
# print(a)  # 1600

triple = lambda x: x * 3
add = lambda x, y: x + y

print(triple(3))  # 9
print(add(2, 3))  # 5
