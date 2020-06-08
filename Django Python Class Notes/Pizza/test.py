def make_pizza(size, *toppings):
    print('\n making pizza with ' + str(size))
    for topping in toppings:
        print('  ' , topping.title())

# make_pizza((30, 'gharch', 'goje', 'panir', 'felfel'))