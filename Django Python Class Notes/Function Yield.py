# Two printing results  7
# 
# 
# 
# 
# 
# def countdown(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i
            
# print(list(countdown(10)))  # [0, 2, 4, 6, 8]
# for i in countdown(10):
#     print(i)  # 0
#                 # 2
#                 # 4
#                 # 6
#                 # 8

                         
# def countdown(x):
#         for i in range(x):
#             if i % 2 == 0:
#                 yield i
            
# my_list = list(countdown(10));print(my_list)  # [0, 2, 4, 6, 8]


def make_word():
    word = ''
    for w in 'spam':
        word += w
        yield word

list1 = list(make_word());print(list1)  # ['s', 'sp', 'spa', 'spam']
# list1 = ['s', 'sp', 'spa', 'spam']