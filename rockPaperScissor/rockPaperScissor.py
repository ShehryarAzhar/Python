# ROCK PAPER SCISSOR

while True:
    import random

    name = input("Enter you Name :> ")

    print(
    """
    Enter Your Choice:
    'r' for rock
    'p' for paper
    's' for scissor
    """)

    choices = ['r', 'p', 's']
    player = input('> ')

    while player not in choices:
        print('Wrong Input! Try Again...')
        player = input('> ')
        
    computer = random.choice(choices)

    print(f"{name} chose {player}")
    print(f"Computer chose {computer}")

    # Game Logic
    def checkWinner(player1, player2):
        
        if player1 == player2:
            print("It's a Draw")
        elif player1 == 'p' and player2 == 'r':
            print(f"{name} won!")
        elif player1 == 'r' and player2 == 'p':
            print(f"Computer won!")
        elif player1 == 'r' and player2 == 's':
            print(f"{name} won!")
        elif player1 == 's' and player2 == 'r':
            print(f"Computer won!")
        elif player1 == 's' and player2 == 'p':
            print(f"{name} won!")
        else:
            print(f"Computer won!")

    checkWinner(player, computer)
    print('-----')