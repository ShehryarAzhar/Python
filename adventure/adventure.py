#                    TEXT-BASED ADVENTURE

# asks the player whether he/she wants to play again
def play_again():
    print("Do you want to play again?(y or n)")

    # gets player answer and convert it into lower string
    answer = input(">").lower()

    if 'y' in answer:
        start()
    else:
        exit()


# game is ended
def game_over(reason):
    print("\n" + reason)
    print("GAME OVER!")

    play_again()


# A room full of diamonds
def diamond_room():
    # Give some prompts
    print("\nYou are now in a room filled with diamonds.")
    print("And there is a door too.\n")

    print("What would you do?(1 or 2)")
    print("1) Take some diamonds and go through the door.")
    print("2) Just go through the door.")

    # gets player answer and convert it into lower string
    answer = input(">").lower()

    if answer == '1':
        # the player died
        game_over("They were cursed diamonds, the moment you touched, the building colapsed, and you die!")
    elif answer == '2':
        # player won the game
        game_over("Nice, You're an honest person, Congrats! you have won the game.")
    else:
        game_over("Go and learn how to type a number.")


# Room where bear is eating tasty honey.
def bear_room():
    # give some prompts
    print("\nThere is a bear here!")
    print("Behind the bear is another room.")
    print("The bear is eating tasty honey!\n")
    
    print("What would you do?(1 0r 2)")
    print("1) Take the honey.")
    print("2) Taunt the bear.\n")

    # gets player answer and convert it into lower string
    answer = input(">").lower()

    if answer == '1':
        # player is dead
        game_over("The bear killed You!")
    elif answer == '2':
        print("Your good time, the bear moved from the door, you can go through it now.")
        # player enters the room full of diamonds
        diamond_room()
    else:
        # Wrong input from the user game_over
        game_over("Don't you know how to type a number?")


# Room where monster is sleeping
def moster_room():
    # give some prompts
    print("\nNow you entered the room of a monster.")
    print("The monster is sleeping.\nBehind the monster, there is another room.\n")
    
    print("What would you do?(1 or 2)")
    print("1) Go through the door silently.")
    print("2) Kill the monster and show your courage!\n")
    
    # gets player answer and convert it into lower string
    answer = input(">").lower()

    if answer == '1':
        # player enters the room full of diamonds
        diamond_room()
    elif answer == '2':
        # the player was killed
        game_over("The monster was hungry he ate you!")
    else:
        game_over("Go and learn how to type a number.")

# let's play
def start():
    # give some prompts
    print("\nYou are standing in a dark room!")
    print("There is a door to your left and right, which one do you want to take? (l or r)\n")

    # gets player answer and convert it into lower string
    answer = input(">").lower()

    if 'l' in answer:
        # player enters the room of a bear
        bear_room()
    elif 'r' in answer:
        # player enters the room of a monster
        moster_room()
    else:
        game_over("Don't you know how to type something properly?")

start()