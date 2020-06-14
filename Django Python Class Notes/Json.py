import json
# 
# 
# 
# 
# 
# 
# 
# 
# 


filename = 'username.json'

try:
    with open('Django Python Class Notes/Json1.py') as file:
        username = json.load(file)
except FileNotFoundError:
    username = input('Whats your username: ')
    with open('Django Python Class Notes/Json1.py', 'w') as file:
        json.dump(username, file)
        print('well remember you when you come back ' + username + ' !')

else:
    print('welcome back ' + username + ' !')  # welcome back rich !




# num = [2, 3, 4, 5, 6]
# filename = 'num.json'
# with open(filename, 'w') as file:
#     json.dump(num, file)


# filename = 'num.json'
# with open(filename) as file:
#     my_list = json.load(file)
# print(my_list[0])  # 2
# print(my_list[1])  # 3


# username = input('please enter your username: ')  # rich
# filename = 'username.json'
# with open(filename, 'w') as file:
#     json.dump(username, file)
# print('we will remember you when you come back {} !'.format(username))  # we will remember you when you come back rich !


# filename = 'username.json'
# with open(filename, 'r') as file:
#     username = json.load(file)
# print(f'welcome back {username}')  # welcome back rich