# Changing a string into a list
# removing the third function and moving it into the second function ** 30
# # removing the third function and moving it into the second function PART: 2  ** 60
# # removing the third function and moving it into the second function PART: 3  ** 90
# 
# 
# 
# 
# 
# 
# class Test():
#     def __init__(self, l):
#         self.l = l
        
#     def print_l(self):
#         print(self.l)
        
#     def split_l(self):
#         s = (self.l).split()
#         print(s)
        
# test = Test('hi this is python')
# test.print_l()  # hi this is python
# test.split_l()  # ['hi', 'this', 'is', 'python']





# # removing the third function and moving it into the second function ** 30
# class Test():
#     def __init__(self, l):
#         self.l = l
        
#     def print_l(self):
#         if type(self.l) == type(''):
#             s = (self.l).split()
#             print(s, ' is string')  # ['hi', 'this', 'is', 'python']  is string
#             for i in s:
#                 print('_', i)
#         elif type(self.l) == type([]):
#             print(s, ' is list')
#             for i in self.l:
#                 print('_', i)
       
# test = Test('hi this is python')
# test.print_l()  # hi 
#                 # this
#                 # is
#                 # python
#  # comments     # >>> type(a)
#                 # <class 'str'>
#                 # >>> b = type(a)
#                 # >>> b
#                 # <class 'str'>
#                 # >>> type(a) == b
#                 # True


# # removing the third function and moving it into the second function PART: 2  ** 60
# class Test():
#     def __init__(self, l):
#         self.l = l
        
#     def print_l(self):
#         if type(self.l) == type(''):
#             s = (self.l).split()
#             print(s, ' is string')  # ['hi', 'this', 'is', 'python']  is string
#             for i in s:
#                 print('_', i)
#         elif type(self.l) == type([]):
#             print(s, ' is list')
#             for i in self.l:
#                 print('_', i)
       
# test = Test('hi this is python')
# test.print_l()  # hi 
#                 # this
#                 # is
#                 # python
#  # comments     # >>> type(a)
#                 # <class 'str'>
#                 # >>> b = type(a)
#                 # >>> b
#                 # <class 'str'>
#                 # >>> type(a) == b
#                 # True


# removing the third function and moving it into the second function PART: 3  ** 90
class Test():
    def __init__(self, l):
        self.l = l
        
    def print_l(self):
        if type(self.l) == type(''):
            s = (self.l).split()
            print(s, ' is string')  # ['hi', 'this', 'is', 'python']  is string
            for i in s:
                print('_', i)
        elif type(self.l) == type([]):
            print(self.l, ' is list')  # ['hi', 'this', 'is', 'python']  is list
            for i in self.l:
                print('_', i)
       
test = Test(['hi', 'this', 'is', 'python'])
test.print_l()  # hi 
                # this
                # is
                # python
 # comments     # >>> type(a)
                # <class 'str'>
                # >>> b = type(a)
                # >>> b
                # <class 'str'>
                # >>> type(a) == b
                # True