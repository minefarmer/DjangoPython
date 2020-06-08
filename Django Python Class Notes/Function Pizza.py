# first part on bottom
# 
# 
# 
# 

def make_pizza(size, *toppings):
    print('\n making pizza with ' + str(size))
    for topping in toppings:
        print('  ' , topping.title())

make_pizza((30, 'gharch', 'goje', 'panir', 'felfel'))


# def build_profile(first, last, **user_info):
#     p = {}
#     p['first_name'] = first
#     p['last_name'] = last
#     for k, v in user_info.items():
#         p[k] = v
#     return p
# m = build_profile('rich', 'matson', location='paris', field='physics', shoghl='programmer')
# print(m)  # {'first_name': 'rich', 'last_name': 'matson', 'location': 'paris', 'field': 'physics', 'shoghl': 'programmer'}


 
 
    