# 
# 
# 
# 
# 
def get_formated_name(first_name, last_name):
    # return full name
    full_name = first_name + ' ' + last_name
    return full_name

while True:
    print('please enter your name : ')
    print('please enter exit to exit ')
    
    f_name = input('First name : ')
    if f_name == 'exit' or f_name == 'e':
        break
    l_name = input('Last name : ')
    if l_name == 'exit' or l_name == 'e':
        break
    fullname = get_formated_name(f_name, l_name)
    print('Hello ' + fullname + ' ')
    repeat = input('do you want to repeat the questions? ')
    if repeat == 'exit' or repeat == 'e':
        break
