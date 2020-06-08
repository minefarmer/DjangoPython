from sys import exit

def gold_room():
    print("this room is full of gold, how much do you take? ")
    
    choice = input('> ')
    
    if '0' in choice or '1' in choice:
        how_much = int(choice)
    else:
        dead('man . learn to type a number')
    if how_much < 50:
        print('nice. you are not greedy. you win')
        exit(0)
    else:
        dead('you are greedy bad')
        
def bear_room():
    print('there is a bear here')
    print('the bear has a bunch of honey')
    print('the fat bear is in from another door')
    print('how are you going to move the bear?')
bear_moved = False

while True:
    choice = input('>')
    if choice == 'take honey':
        dead('the bear looks at you and slaps your face off')
    elif choice  == 'taunt bear' and not bear_moved:
        print('the bear has moved from the door')
        print('you can go through it now')
        print('you can go through the door')
        bear_moved = True
    elif choice == 'taunt bear' and bear_moved:
        dead('the bear gets pissed off and chew your leg off')
        
    elif choice == 'open door':
        gold_room()
        
def dead(msg):
    print(msg + 'Good job')
    
bear_room()
    
    