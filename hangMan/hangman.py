from words import words
from lives_visual_dict import lives_visual_dict
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    # if "-" is in word it will loop until word without "-" is selected
    while "-" in word:
        word = random.choice(words)
    
    return word.upper() # returns the word in upper case


def hangman():
    word = get_valid_word(words)
    # print(word)
    word_letters = set(word) # set of word
    alphabets = set(string.ascii_uppercase) # Set of all aphabets (A-Z)
    lives = 7
    used_letters = set()

    while lives > 0 and len(word_letters) > 0: 
        #current word like W-RD 
        current_word = [letter if letter in used_letters else "-" for letter in word]
        
        # telling the player how many lives have left, and which alphabets are already used
        print(lives_visual_dict[lives]) # visual display of hanging man
        print(f"You have {lives} lives left, and you already used these letters,", " ".join(used_letters))
        print(" ".join(current_word)) # current_word

        
        print("Enter the alphabet: ")
        user_letter = input(":> ").upper()

        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word:
                # if letter is in the word then this letter is removed from word_letters set
                word_letters.remove(user_letter)
                print("Yeah! You have guessed the letter.")
            else:
                # if letter is not in the word a message pops up and player loses 1 life
                print("Oops! the letter doesn't exist in the word")
                lives -= 1

        elif user_letter in used_letters:
            print("You have already used this letter. Please go again!")
        else:
            print("Invalid Input! Go and learn how to type an alphabet.")

    if lives == 0:
        print(lives_visual_dict[lives]) # hanging man
        # failure message
        print("-----------------")
        print(f"Oh No! You couldn't guessed the word {word}, You're dead...")
        print("")
    else:
        # success message
        print("-----------------")
        print(f"Yaay! Congrats you have guessed the word {word}")
        print("")

if __name__ == "__main__":
    hangman()