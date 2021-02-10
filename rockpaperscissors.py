import random
weapon = ['scissors', 'rock', 'paper']
def rockpaperscissors():
    computer_weapon = random.choice(weapon)
    user_weapon = input("Choose your weapon between rock, paper or scissors: ")
    if user_weapon == computer_weapon:
        print("Draw")
    elif user_weapon == 'scissors' and computer_weapon == 'rock':
        print("you lose")
    elif user_weapon == 'scissors' and computer_weapon == 'paper':
        print("you win")
    elif user_weapon == 'rock' and computer_weapon == 'paper':
        print("you lose")
    elif user_weapon == 'rock' and computer_weapon == 'scissors':
        print("you win")
    elif user_weapon == 'paper' and computer_weapon == 'scissors':
        print("you lose")
    elif user_weapon == 'paper' and computer_weapon == 'rock':
        print("you win")
rockpaperscissors()