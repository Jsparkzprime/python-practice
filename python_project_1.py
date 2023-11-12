import random

while True:
    user_input = input(f'OK lets go .. ROCK, PAPER, SCISSORS, SHOOT ')
    computer_input = random.choice(['rock', 'paper', 'scissors'])

    allowed_responses = ['rock', 'paper', 'scissors', 'quit']

    if user_input.lower() not in allowed_responses:
        print('you have to answer rock, paper or scissors. Or you can quit') 
    if user_input.lower() == computer_input:
        print(f'I chose {computer_input}, Its a draw! lets play again')
    elif user_input.lower() == 'paper' and computer_input == 'scissors':
        print(f'I chose {computer_input}, Yay! I won. If you want to quit just type quit if not lets play again ')
    elif user_input.lower() == 'rock' and computer_input == 'paper':
        print(f'I chose {computer_input}, Yay! I won. If you want to quit just type quit if not lets play again ')
    elif user_input.lower() == 'scissors' and computer_input == 'rock':
        print(f'I chose {computer_input}, Yay! I won. If you want to quit just type quit if not lets play again ')
    elif user_input.lower() == 'rock' and computer_input == 'scissors':
        print(f'I chose {computer_input}, Awwn I lost, Do you wanna play again? ')
    elif user_input.lower() == 'scissors' and computer_input == 'paper':
        print(f'I chose {computer_input}, Awwn I lost, Do you wanna play again? ')
    elif user_input.lower() == 'paper' and computer_input == 'rock':
        print(f'I chose {computer_input}, Awwn I lost, Do you wanna play again? ')
    elif user_input.lower() == 'quit':
        break






