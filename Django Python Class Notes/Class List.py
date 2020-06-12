# list can be added to at a later date  # 25
#  appending this list at a later date 1  # 40
#  appending this list at a later date 2  # 60
# 
# 
# 
# 
# 
# 
# 
# class Test():   ************************************************
#     def __init__(self, list1):
#         self.list1 = list1
#     def print_list(self):
#         for i in self.list1:
#             print(' ', i)  #   carl
#                             # rich  
#                             # matson
            
# my_list = Test(['carl', 'rich', 'matson'])

# my_list.print_list()


# # this list can be added to at a later date   **********************************
# class Test():
#     def __init__(self, list1):
#         self.list1 = [1, 2, 3, 4]
#     def print_list(self):
#         for i in self.list1:
#             print(' ', i)   # 1
#                             # 2
#                             # 3
#                             # 4
            
# my_list = Test(['carl', 'rich', 'matson'])

# my_list.print_list()

# # appending this list at a later date 1   **********************************
# class Test():
#     def __init__(self, list1):
#         self.list1 = []
#     def print_list(self):
#         for i in self.list1:
#             print(' ', i) 
#     def append_list(self, l):
#         for i in l:
#             self.list1.append(i)
            
# my_list = Test(['carl', 'rich', 'matson'])
# my_list.append_list(['test1', 'test2', 'test3'])
# my_list.print_list()    # test1
#                         # test2
#                         # test3




# appending this list at a later date 2     ***********************************
class Test():
    def __init__(self, list1):
        self.list1 = []
        self.list2 = list1
    def print_list(self):
        for i in self.list1:
            print('_', i) 
    def print_list2(self):
        for i in self.list2:
            print('_', i)
    def append_list(self, l):
        for i in l:
            self.list1.append(i)
            
my_list = Test(['carl', 'rich', 'matson'])
my_list.append_list(['test1', 'test2', 'test3'])
my_list.print_list()    #_ test1
                        # _ test2
                        # _ test3
my_list.print_list2()  # _ carl
                        # _ rich
                        # _ matson







