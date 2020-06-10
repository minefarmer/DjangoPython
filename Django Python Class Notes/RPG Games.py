from sys import exit

def gold_room():
    print("this room is full of gold, how much do you take? ")
    
    choice = input('> ')
    
    if '0' in choice or '1' in choice:
        how_much = int(choice)
    else:
        dead('man , learn to type number ')
        
    if how_much < 50:
        print('nice, you are not greedy, you win')
        exit(0)
    else:
        dead('you greedy bad')
        
def bear_room():
    print('there is a bear here')
    print('the bear has a bunch of honey')
    print('the fat bear is in from another door')
    print('how are you going to move the bear')
    bear_moved = False
    
    while  True:
        choice = input('> ')
        if choice == 'take honey':
            dead('the bear look at you then slaps your face off')
        elif choice == 'taunt bear' and not bear_moved:
            print('the bear has moved from the door')
            print('you can go through it now')
            print('you can go through the door')
            bear_moved = True
        elif choice == 'taunt bear' and bear_moved:
            dead('the bear gets pissed off and chew your legs off')

        elif  choice == 'open door':
            gold_room()

        else:
            print('I got no idea what that means.')

def dark_room():
    print('hear you see the great evil dark')
    print('he, it, whatever stares at you and you go insane')
    print('do you flee for your life or eat your head?')
    choice = input('> ')
    if 'flee' in choice:
        start()
    elif 'head' in choice:
        dead('well that was tasty')
    else:
        dark_room()
def start():
    print('you are in a dark room')
    print('there is a door to your right and left')
    print('which one do you chose!')
    choice = input('> ')
    if choice == 'left':
        bear_room()
    elif  choice == 'right':
        dark_room()
    else:
        dead("you stumble around the room until you starve")
        
def dead(msg):
    print(msg + ' Good job!')
    exit(0)

start()






#  THIS WAS ON LINE 41        
# def dead(msg):
#     print(msg + ' Good Job')
#     exit(0)
    
# bear_room()

