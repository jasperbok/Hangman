import random
import os

wordList = ["spam", "eggs", "cheese", "bryan", "python", "flying", "circus"]
guessesLeft = 0
guessedLetters = []
lastGuess = ""
letters = []

def pick_word():
    """
    Picks a random word from the wordList list and returns it.
    """
    global wordList

    word = wordList[random.randint(0, len(wordList)-1)]
    
    return word



def make_letter_list(word):
    """
    Takes a word as an argument, turns it into a list, and returns that list.

    The list is used to keep track of what letters are guessed. To achieve that
    functionality, every entry in the list is a nested list containing a letter
    and a boolean which tells whether the letter has been guessed or not.
    """
    letterList = []
    for letter in word:
        letterList.append([letter, False])
    return letterList



def initialize_game():
    """
    Initializes a new game.

    First it gives the player a new set of guesses. Next, it empties the
    guessedLetters list. Finally, it selects a new word.
    """
    global guessesLeft
    global guessedLetters
    global letters
    
    guessesLeft = 6
    guessedLetters = []
    letters = make_letter_list(pick_word())

    update_screen()

    

def handle_input(guess):
    """
    Function which takes the user's input and first adds the input to the
    guessedLetters list. It then checks the letters array to see if there's a
    match between the user's guess and a letter in the word. If there is, it
    marks the letter as guessed.

    If there is no match, the user loses a try.

    Finally it calls the updateScreen() function to update the information on
    screen.
    """
    global guessesLeft
    global guessedLetters
    global lastGuess
    global letters

    if not guess in guessedLetters:
        lastGuess = "unique"
        guessedLetters.append(guess)

        # Set goodGuess the False by default. If the user's guess is found in 
        # the letters list we'll change goodGuess to True.
        goodGuess = False
        
        for letter in letters:
            if letter[0] == guess:
                letter[1] = True
                goodGuess = True
            else:
                pass

        if goodGuess:
            lastGuess = "hit"
        else:
            guessesLeft -= 1
            lastGuess = "miss"
    else:
        lastGuess = "double"

    update_screen()

    

def update_screen():
    """
    Function which updates the information on the screen.
    """
    global guessesLeft
    global guessedLetters
    global letters

    # Print 40 newline characters to clear the screen.
    print(40 * "\n")

    if lastGuess == "double":
        print("You've already tried that letter!")
    elif lastGuess == "hit":
        print("A good choice! That letter was in there!")
    elif lastGuess == "miss":
        print("Nice try, but that letter does not belong in this word.")
    print(4 * "\n")
    
    print("You have " + str(guessesLeft) + " guesses left.\n")
    print("You tried these letters already: " + str(sorted(guessedLetters)) + "\n\n")
    for letter in letters:
        if letter[1] == True:
            print(" " + letter[0] + " ", end = "")
        else:
            print(" . ", end = "")
    game_loop()

    

def game_loop():
    global guessesLeft
    global guessedLetters
    global letters

    guessedAllLetters = True
    for letter in letters:
        if letter[1] == False:
            guessedAllLetters = False
            break
        else:
            continue
    
    if guessedAllLetters:
        end_game("win")
    elif guessesLeft <= 0:
        end_game("lose")
    else:
        print("\n\nGuess a letter:\n")
        guess = input()
        handle_input(guess)



def end_game(status):
    """
    A function which displays a win or loss message.
    """
    if status == "win":
        print("\n\nCongratz! You are a true Hangman Master!!!")
    elif status == "lose":
        print("\n\nHahaha you're such a loser! :D")

    restart = input("Wanna play again? (y/n)")

    if restart == "y" or restart == "Y":
        initialize_game()
    else:
        pass

    

initialize_game()
