# Functio with any number of parameters  38
# 
# 
# 
# 
# def Test(list1, list2):
# 	while list1:
# 		p = list1.pop()
# 		list2.append(p)
# 		print(list2)  # ['h5']
# 					# ['h5', 'h4']
# 					# ['h5', 'h4', 'h3']
# 					# ['h5', 'h4', 'h3', 'h2']      
# 					# ['h5', 'h4', 'h3', 'h2', 'h1']
# 	return list2

# l1 = ['h1', 'h2', 'h3', 'h4', 'h5']
# l2 = []
# Test(l1, l2)


# def Test(list1, list2):
# 	while list1:
# 		p = list1.pop()
# 		list2.append(p)
# 		print(list2)
# 	return list2

# l1 = ['h1', 'h2', 'h3', 'h4', 'h5']
# l2 = ['s1', 's2', 's3', 's4']
# l1.extend(l2)
# print(l1)  # ['h1', 'h2', 'h3', 'h4', 'h5', 's1', 's2', 's3', 's4']


# Functio with any number of parameters
def test(*t):  # *t makes it possible to use any number of perameters
    print(t)  # ('rich',)  ** ('carl', 'matson')  *** ('carl', 'Richard', 'matson')  **** ('carl', 'Richard', 'matson', '81 years old')
    
test('rich')  # #
test('carl', 'matson')  # **
test('carl', 'Richard', 'matson')  # ***
test('carl', 'Richard', 'matson', '81 years old')  # ****


