# Number Guessing Game
from random import randint
from art import logo
print(logo)

EASY_MODE = 10
HARD_MODE = 5

chances = 0
# Checking user's guess with answer
def check_ans(guess, answer, chances):
  """To check guess with answer. Shows number of chances left."""
  if guess > answer:
    print("Guess is high.")
    return chances - 1
  elif guess < answer:
    print("Guess is low.")
    return chances - 1
  else:
    print(f"Congrats. You guessed the correct number: {answer}")

# Game difficulty function
def set_difficult():
  game_mode = input("Select your difficulty. 'easy' or 'hard': ")
  if game_mode == "easy":
    return EASY_MODE
  else:
    return HARD_MODE

def game():
  # Welcome message!
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  
  # Selecting a number between 1 and 100.
  answer = randint(1, 100)
  
  chances = set_difficult()
  
  guess = 0
  while guess != answer:
    print(f"You have {chances} remaining chances to guess.")
    
    # User guesses the number
    guess = int(input("Please make a guess: "))
    chances = check_ans(guess, answer, chances)

game()