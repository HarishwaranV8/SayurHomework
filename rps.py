import random

options = ['rock','paper','scissors']
print('1.Rock\n2.Paper\n3.Scissors')


def decide_winner():
    computer_points = 0
    player_points = 0
    for i in range(3):
        player_choice = options[int(input('Enter your input: '))-1]
        print('Your choice:',player_choice)
        computer_choice = random.choice(options)
        print('Computer choice:',computer_choice)
        if computer_choice == 'rock':
            if player_choice == 'paper':
                player_points += 1
            elif player_choice == 'scissors':
                computer_points += 1
        if computer_choice == 'paper':
            if player_choice == 'scissors':
                player_points += 1
            elif player_choice == 'rock':
                computer_points += 1
        if computer_choice == 'scissors':
            if player_choice == 'rock':
                player_points += 1
            elif player_choice == 'paper':
                computer_points += 1
        
    
    if player_points > computer_points:
        print('Player is the winner')
    elif player_points < computer_points:
        print('Computer is the winner')
    else:
        print('The game is draw')

decide_winner()
