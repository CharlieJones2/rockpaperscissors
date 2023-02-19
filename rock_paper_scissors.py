import random

choices = ['rock', 'paper', 'scissors']

comp = random.choice(choices)
scores = dict()
scores['us'] = 0
scores['cs'] = 0

turnFlag = True

while turnFlag:
    turn = input('rock, paper or scissors? ').lower()
    comp = random.choice(choices)

# quitting
    if turn == 'done':
        playFlag = True
        while playFlag:
            play = input('would you like to finish the game? ')

# quitting
            if play == 'yes':
                print('thank you for playing!')
                print('your score: ', scores['us'])
                print('computers score: ', scores['cs'])
                if scores['us'] > scores['cs']:
                    print('you won!')
                elif scores['us'] == scores['cs']:
                    print('its a tie!')
                else:
                    print('you lost!')
                quit()

# resuming
            elif play == 'no':
                print('resuming game')
                playFlag = False
# invalid entry
            else:
                print('error: please enter "yes" or "no"')

# choosing rock
    elif turn == 'rock':
        print('you chose: ', turn)
        if comp == 'rock':
            print('computer chose: ', comp)
            print('its a tie!')
        elif comp == 'paper':
            print('computer chose: ', comp)
            print('you lose!')
            scores['cs'] = scores['cs'] + 1
        else:
            print('computer chose: ', comp)
            print('you win!')
            scores['us'] = scores['us'] + 1

# choosing paper
    elif turn == 'paper':
        print('you chose: ', turn)
        if comp == 'rock':
            print('computer chose: ', comp)
            print('you win!')
            scores['us'] = scores['us'] + 1
        elif comp == 'paper':
            print('computer chose: ', comp)
            print('its a tie!')
        else:
            print('computer chose: ', comp)
            print('you lose!')
            scores['cs'] = scores['cs'] + 1

# choosing scissors
    elif turn == 'scissors':
        print('you chose: ', turn)
        if comp == 'rock':
            print('computer chose: ', comp)
            print('you lose!')
            scores['cs'] = scores['cs'] + 1
        elif comp == 'paper':
            print('computer chose: ', comp)
            print('you win!')
            scores['us'] = scores['us'] + 1
        else:
            print('computer chose: ', comp)
            print('its a tie!')

# invalid entry
    else:
        print('error! please enter "rock", "paper" or "scissors"')
