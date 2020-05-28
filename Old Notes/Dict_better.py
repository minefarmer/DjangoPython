my_dict = {'name' : 'carl', 'age' : 33, 'car_name' : 'BMW'}
my_dict_1 = {'numbers_1' : [1, 2, 3, 4], 'numbwrsa_2' : [2, 3, 60], 'car_name' : 'bmw'}

# print(my_dict)  # {'name': 'carl', 'age': 33, 'car_name': 'BMW'}
# print(my_dict_1)  # {'numbers_1': [1, 2, 3, 4], 'numbwrsa_2': [2, 3, 60], 'car_name': 'bmw'}



# print(my_dict_1)
# for k in my_dict_1:
#     print(k)    # numbers_1
#                 # numbwrs_2
#                 # car_name

# for k, v in my_dict_1.items():
#     print(k, v)  # numbers_1 [1, 2, 3, 4]
#                 # numbwrs_2 [2, 3, 60]
#                 # car_name bmw



my_list = [1, 2, 3, 4, 5]
# for i in my_dict_1.keys():
#     print(i)  # numbers_1
#             # numbwrs_2
#             # car_name

# my_list = [1, 2, 3, 4, 5]
# for i in my_dict_1.items():
#     print(i)  # ('numbers_1', [1, 2, 3, 4])
#             # ('numbwrs_2', [2, 3, 60])
#             # ('car_name', 'bmw')

# for i in my_dict_1.values():
#     print(i)  # [1, 2, 3, 4]
#             # [2, 3, 60]
#             # bmw

# for a, b in my_dict_1.items():
#     print(a, b)  # numbers_1 [1, 2, 3, 4]
#                 # numbwrs_2 [2, 3, 60]
#                 # car_name bmw
                
                
                
# my_dict_2 = {1 : [1, 2, 3, 4], 'numbwrs_2' : [2, 3, 60], 'car_name' : 'bmw'}
 
# print(my_dict_2)



my_dict_3 = {1 : {'name' : 'car'}, 'numbwrs_2' : [2, 3, 60], 'car_name' : 'bmw'}
 
# print(my_dict_3)  # {1: {'name': 'car'}, 'numbwrs_2': [2, 3, 60], 'car_name': 'bmw'}



# my_dict_4 = {
#     'name' : ['sandra', 'jess', 'roger', 'carl'],
#     'numbers' : [1, 2, 3, 4, 5, 6],
#     'colors' : 'yellow',
# }
# print(my_dict_4)  # {'name': ['sandra', 'jess', 'roger', 'carl'], 'numbers': [1, 2, 3, 4, 5, 6], 'colors': 'yellow'}



my_dict_4 = {
    'name' : ['sandra', 'jess', 'roger', 'carl'],
    'numbers' : [1, 2, 3, 4, 5, 6],
    'colors' : 'yellow',
}

# for k, v in my_dict_4:
#     print(k, v)  # ValueError: too many values to unpack (expected 2)

# for k, v in my_dict_4.items():
#     print(k, v)  # name ['sandra', 'jess', 'roger', 'carl']
#                 # numbers [1, 2, 3, 4, 5, 6]
#                 # colors yellow

# for k, v in my_dict_4.items():
#     print(k, v)  # name ['sandra', 'jess', 'roger', 'carl']
#                 # numbers [1, 2, 3, 4, 5, 6]
#                 # colors yellow
                
# a = my_dict_4['name']
# print(a)  # ['sandra', 'jess', 'roger', 'carl']

# a = my_dict_4['name']
# print(my_dict_4['numbers'])  # [1, 2, 3, 4, 5, 6]
# print(a)  # ['sandra', 'jess', 'roger', 'carl']

a = my_dict_4['name']
print(my_dict_4['numbers'])  # [1, 2, 3, 4, 5, 6]
print(a)  # ['sandra', 'jess', 'roger', 'carl']
a = 'salam'
print(a)  # salam