import random

computer = 0
player = 0

while True:

    x = ['rock', 'paper', 'scissors']
    

    y = random.choice(x)
    
    guess = input('Enter your guess: ')
    
    if y == guess:
        player += 1
        if player == 3:
            print('You win!')
            break
    else:
        computer += 1
        print('Computer chose: ', y)
        if computer == 3:
            print('You lose!')
            break
    
print('Computer: ', computer)
print('Player: ', player)
