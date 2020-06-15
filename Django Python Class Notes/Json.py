import json
# best store user setup setup  43
# if user name exists  70
# if user name does not exist  102   
# 
# 
# 
# 
# 
# 
# filename = 'username.json'
# try:
#     with open('Django Python Class Notes/Json1.py') as file:
#         username = json.load(file)
# except FileNotFoundError:
#     username = input('Whats your username: ')  # rich
#     with open('Django Python Class Notes/Json1.py', 'w') as file:
#         json.dump(username, file)
#         print('well remember you when you come back ' + username + ' !')
# else:
#     print('welcome back ' + username + ' !')  # welcome back rich !





# def greet_user():
#     filename = 'username.json'
#     try:
#         with open(filename) as file:
#             username = json.load(file)
#     except FileNotFoundError:
#         username = input('whats your username: ')  # whats your username: rich
#         with open(filename , 'w') as file:
#             json.dump(username, file)
#             print('well remember you when you come back ' + username)
#     else:
#             print('welcome back ' + username)  # well remember you when you come back rich

# greet_user()


#  best setup  43
# def greet_user():
#     filename = 'username.json'
#     try:
#         with open(filename) as file:
#             username = json.load(file)
#     except FileNotFoundError:
#         return None
#     else:
#         return username

# def store_user():
#     username = greet_user()
#     if username:
#         print('welcome back ' + username)  # welcome back admin  ** this is printed on the second run of this code
#     else:
#         username = input('whats your username? ')  # admin
#         filename = 'username.json'
#         with open (filename, 'w') as file:
#             json.dump(username, file)
#             print('well remember you when you come back ' + username + ' !')  # well remember you when you come back admin !

# store_user()




#  if user name exists  70
# def get_stored_username():
#     """ works if user name is available """
#     filename = 'username.json'
#     try:
#         with open(filename) as file:
#             username = json.load(file)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
# def get_new_username():
#     """prompt user for a new username"""
#     username = input('whats your user name ')
#     filename = 'username.json'
#     with open(filename, 'w') as file:
#         json.dump(username, file)
#     return username


# def greet_user():
#     """printing username"""
#     username = get_stored_username()
#     if username:
#         print('welcome back ' + username + ' !')
#     else:
#         username = get_new_username()
#         print('well remember you when you come back ' + username + ' !')
        
# greet_user()
        
    
# if user name does not exist  102   
def get_stored_username():
    """ works if user name is available """
    filename = 'admin.json'
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """prompt user for a new username"""
    username = input('whats your user name ')  # whats your user name root  8 1st run
    filename = 'admin.json'
    with open(filename, 'w') as file:
        json.dump(username, file)
    return username


def greet_user():
    """printing username"""
    username = get_stored_username()
    if username:
        print('welcome back ' + username + ' !')  # welcome back root ! * 2nd run
    else:
        username = get_new_username()
        print('well remember you when you come back ' + username + ' !')  # well remember you when you come back root !
        
greet_user()