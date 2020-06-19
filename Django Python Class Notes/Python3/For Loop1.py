# 
# 
# 
# 
# 
# def users(names):
# 	for name in names:
# 		msg = 'Hello ' + name.title() + '!'
# 		print(msg)
# user_names = ['ali', 'pedram', 'maryam', 'hsan']

# users(user_names)  # Hello Ali!
# 					# Hello Pedram!
# 					# Hello Maryam!
# 					# Hello Hsan!
     
     
     
# l1 = ['iphone_case', 'case', 'robot', 'car', 'toys']
# l2 = []
# while l1:
#     l3 = l1.pop()
# print(l1)  # []

# l1 = ['iphone_case', 'case', 'robot', 'car', 'toys']
# l2 = []
# print(l1)  # ['iphone_case', 'case', 'robot', 'car', 'toys']
# while l1:
#     l3 = l1.pop()
#     l2.append(l3)
# print(l2)  # ['toys', 'car', 'robot', 'case', 'iphone_case']

# l1 = ['iphone_case', 'case', 'robot', 'car', 'toys']
# l2 = []
# print(l1)  # ['iphone_case', 'case', 'robot', 'car', 'toys']
# while l1:
#     l3 = l1.pop()
#     print(l3)  # toys       
# 				# car        
# 				# robot      
# 				# case       
# 				# iphone_case
#     # l2.append(l3)
# print(l2)  # []   *** an empty list

# l1 = ['iphone_case', 'case', 'robot', 'car', 'toys']
# l2 = []
# print(l1)  # ['iphone_case', 'case', 'robot', 'car', 'toys']
# while l1:
#     l3 = l1.pop()
#     print(l3)  # toys       
# 				# car        
# 				# robot      
# 				# case       
# 				# iphone_case
#     # l2.append(l3)
# print(type(l3))  # <class 'str'>

l1 = ['iphone_case', 'case', 'robot', 'car', 'toys']
l2 = []
print(l1)  # ['iphone_case', 'case', 'robot', 'car', 'toys']
while l1:
    l3 = l1.pop()
    print('l3 is ', l3)  # l3 is  toys
						# l3 is  car
						# l3 is  robot
						# l3 is  case
						# l3 is  iphone_case
    l2.append(l3)
print('l2 is ', l2)  # l2 is  ['toys', 'car', 'robot', 'case', 'iphone_case']