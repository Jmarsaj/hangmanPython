def load_word():
    word = "DOG"
    return word

def start_round(loaded_word):
    hidden_word = "_" * len(loaded_word)
    print("Round Started")
    print("\n")
    print(hidden_word)

    guessed = False
    tries = 5

    while not guessed and tries > 0:
        guess = raw_input("Guess a letter or word: ").upper()       # might have to change raw_input to input

        if guess.isalpha() and len(guess) == 1:         # checking if guess is an alphabet
            if guess not in loaded_word:
                print(guess + " is not in the word")
                tries -= 1
            else:
                print(guess + " is in the word")

                word_as_list = list(hidden_word)
                indices = [i for i, letter in enumerate(loaded_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess

                hidden_word = "".join(word_as_list)

        elif len(guess) == len(loaded_word) and guess.isalpha():
            if guess != loaded_word:
                print(guess + " is not the word")
                tries -= 1
            else:
                guessed = True
                hidden_word = loaded_word

        print(hidden_word)

loaded_word = load_word()
start_round(loaded_word)