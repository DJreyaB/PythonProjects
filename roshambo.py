import random

def play():
    print('Let\'s play a game of Rock, Paper, Scissors')
    user = input("Pick your weapon: 'r' for rock, 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r', 'p', 's'])
    winning_hands = {
        'r':'s',
        's':'p',
        'p':'r'
    }

    if user == computer:
        return 'tie'

    if is_win(user, computer, winning_hands):
    
        return f'Computer played {computer} and you played {user}; You won!'

    return f'Computer played {computer} and you played {user}; you lost.'

def is_win(player, opponent, options):
    if options[player] == opponent:
        return True

print(play())