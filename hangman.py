import random

def load_word():
    wordList = ["DOG", "CAT", "TABLE", "CHAIR", "HOUSE"]   
    word = random.choice(wordList) 
    word = word.upper()
    return word

def start_round(loaded_word):
    hidden_word = "_" * len(loaded_word)
    print("Round Started")
    print("\n")
    print(hidden_word)

    guessed = False
    tries = 5
    guessed_letters = []
    guessed_words = []

    while not guessed and tries > 0:
        guess = raw_input("Guess a letter or word: ").upper()       # might have to change raw_input to input

        if guess.isalpha() and len(guess) == 1:  
            
            if guess in guessed_letters:
                print("Letter already guessed: " + guess)

            elif guess not in loaded_word:
                print(guess + " is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess + " is in the word")
                guessed_letters.append(guess)

                word_as_list = list(hidden_word)
                indices = [i for i, letter in enumerate(loaded_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess

                hidden_word = "".join(word_as_list)

                if "_" not in hidden_word:
                    guessed = True

        elif guess.isalpha():
            if guess in guessed_words:
                print("Word already guessed: " + guess)

            elif guess != loaded_word:
                print(guess + " is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                hidden_word = loaded_word

        else:
            print("Invalid Guess")

        print(hidden_word)

loaded_word = load_word()
start_round(loaded_word)

while raw_input("Restart game? y/n: ").upper() == "Y":
    loaded_word = load_word()
    start_round(loaded_word)