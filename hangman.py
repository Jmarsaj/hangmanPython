def load_word():
    word = "DOG"
    return word

def start_round(loaded_word):
    hidden_word = "_ " * len(loaded_word)
    print("Round Started")
    print("\n")
    print(hidden_word)

    guessed = False
    tries = 5

    while not guessed and tries > 0:
        guess = raw_input("Guess a letter or word: ")       # might have to change raw_input to input

        if guess.isalpha() and len(guess) == 1:         # checking if guess is an alphabet
            if guess not in loaded_word:
                print(guess + " is not in the word")
                tries -= 1

loaded_word = load_word()
start_round(loaded_word)