import random

def roll():
    # chooses a random number between 1 and 6 (including 1 and 6)
    num = random.randint(1,6)

    if num == 1:
        print('[-----]')
        print('[     ]')
        print('[  O  ]')
        print('[     ]')
        print('[-----]')
    if num == 2:
        print('[-----]')
        print('[ O   ]')
        print('[     ]')
        print('[   O ]')
        print('[-----]')
    if num == 3:
        print('[-----]')
        print('[     ]')
        print('[O O O]')
        print('[     ]')
        print('[-----]')
    if num == 4:
        print('[-----]')
        print('[O   O]')
        print('[     ]')
        print('[O   O]')
        print('[-----]')
    if num == 5:
        print('[-----]')
        print('[O   O]')
        print('[  O  ]')
        print('[O   O]')
        print('[-----]')
    if num == 6:
        print('[-----]')
        print('[O O O]')
        print('[     ]')
        print('[O O O]')
        print('[-----]')
        
x = "y"

while x == "y":
    roll()
    print("\n")
    # asks the player whether he/she wants to roll again
    print("Do you want to play again? (y/n)")
    x = input("> ")