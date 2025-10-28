import random

def choosing_secret_word():

  words_file = open("words.txt",'r')
  words_list = []
  words_lines = words_file.readlines()

  words_lines = str(words_lines)
  words_list = words_lines.split(' ')

  SecretWord = random.choice(words_list)
  SecretWord = str(SecretWord)

  return SecretWord

# ------------------- #

def is_word_guessed(secret_word, letters_guessed):
    sw = []
    for elem in secret_word:
        sw.append(str(elem))
    x = True
    i=len(sw)
    for elem in letters_guessed:
        if elem in sw:
            x = True
            i -= 1
        else:
            x = False
            return False
    if i <= 0 and x == True:
        return x
    else:
        return False

# ------------------- #

def get_guessed_word(secret_word, letters_guessed):
    s = ""
    for i in secret_word:
        if i in letters_guessed:
            s += i
        else:
            s += "_"
    print(s)
    return s

# ------------------- #

def validate(user_input):
  user_input = str(user_input)
  x = user_input.isalpha()
  if x == False:
    return False

# ------------------- #

def get_available_letters(letters_guessed):
    string = "abcdefghijklmnopqrstuvwxyz"
    temp = ""
    for i in string:
        if i not in letters_guessed:
            temp += i
    return temp

# ------------------- #

def available_vowels(guess):
  vowels_available = ["a","e","i","o","u"]
  if guess in vowels_available:
    vowels_available.pop(vowels_available.index(guess))
  vowels_available_str = ""
  for i  in vowels_available:
    vowels_available_str  += i
  return vowels_available_str

# ------------------- #

def hangman():
    secretWord = choosing_secret_word()
    secretWord = secretWord.lower()

    print("Welcome to the game, Hangman!")
    print("I'm thinking of a word that is " + str(len(secretWord)) + " letters long.")

    lettersGuessed = ''
    guessesLeft = 6

    print()
    print("------------")
    print()

    while True:
        print("You have " + str(guessesLeft) + " guesses left.")
        print("Available letters: " + get_available_letters(lettersGuessed))

        guess = str(input("Please guess a letter: "))
        guess = guess.lower()

        print("Available vowels:" + available_vowels(guess))

        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print("Good guess: " + get_guessed_word(secretWord, lettersGuessed))

        elif validate(guess) == False:
          print("Invalid character! Please try again.")
          guessesLeft -= 1

        elif guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + get_guessed_word(secretWord, lettersGuessed))
            guessesLeft -= 1

        elif guess.isalpha() == True:
            print("Oops! That letter is not in my word: " + get_guessed_word(secretWord, lettersGuessed))
            guessesLeft -= 1

        print()
        print("------------")
        print()

        if guessesLeft <= 0:
            print("Sorry, You've ran out of guesses. The word was " + secretWord + ".")
            break
        LG = []
        for i in lettersGuessed:
            LG.append(str(i))
        if is_word_guessed(secretWord, LG):
            print("Congratulations! You've won!")
            break

hangman()