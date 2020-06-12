from word_list import word_sel
import random

def word_choice():
  word = random.choice(word_sel)
  return word.upper()

def format_word_rep(word_rep):
    formatted_word = " "
    word_list = list(word_rep)
    return " ".join(word_list)

def display(word_rep, guesses, letters_guessed):
    print("-" * 50)
    print(f"your guesses left are {guesses}")
    print("Here are all the Letters you have guess")
    print(letters_guessed) # This should be letters_guessed
    print("-" * 50)
    print("What word is this???")
    print(format_word_rep(word_rep))

def find_positions_in_word(letter, word):
    positions = []
    for i in range(len(word)):
        if word[i] == letter:
            positions.append(i)
    return positions

def get_user_guess():
  user_guess = input("What is your guess?\n")
  return user_guess.upper()

# starting a new game
def game():
  current_word = word_choice()
  print(current_word)
  word_rep = "_" * len(current_word)
  guesses = 7
  letters_guessed = []
  print("Starting a new game.")
  print("="*50)
  print(word_rep)
  
  while True:
    #show current state
    display(word_rep, guesses, letters_guessed)

    # get a letter choice
    guess = get_user_guess()
    # find that letter in the word
    if guess in letters_guessed:
        print(f"Sorry, you've already guessed {letter}. Try again.")
    else:
        letters_guessed.append(guess)
        letter_positions = find_positions_in_word(guess, current_word)
        if letter_positions == []:
            guesses -= 1
            print(f"Sorry, {guess} is not in the word")
        else:
            print(f"Nice! There are {len(letter_positions)} {guess}'s in the word!")
            for i in letter_positions:
                word_rep = word_rep[:i] + guess + word_rep[i + 1:]
    # check for win condition
    if not "_" in word_rep:
      print("You won! Good job.")
      break
    # check for loss condition
    if guesses < 1:
        print(f"Sorry, you lost. The word was: {current_word}")
        break

    
  

# reveal appropriate letters 

# repeat

game()