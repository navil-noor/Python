#Importing the files
from art import logo, vs
from game_data import data
import random
import os

#Formating the data from game_data.
def format_data(acc):
  """Convert game data to printed data"""
  acc_name = acc["name"]
  acc_descrp = acc["description"]
  acc_country = acc["country"]
  return f"{acc_name}, a {acc_descrp}, from {acc_country}"

def check_answer(guess, a_follow, b_follow):
  """Takes user guess and follower counts then returns if user is correct."""
  if a_fol_acc > b_fol_acc:
    return guess == 'a'
  else:
    return guess == 'b'


#Display art
print(logo)
score = 0
game_continue = True
#Generate random account from game data.
acc_b = random.choice(data)

#Game repeats until user guesses right.
while game_continue:
  #Make previous B account to A account in the next question.
  acc_a = acc_b
  acc_b = random.choice(data)
 
  while acc_a == acc_b:
    acc_b = random.choice(data)
  
  print(f"Compare A: {format_data(acc_a)}.")
  print(vs)
  print(f"Against B: {format_data(acc_b)}.")
  
  #Ask the user for a guess.
  guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()
  
  #Check answer of user.
  #Get follower account of each account.
  a_fol_acc = acc_a["follower_count"]
  b_fol_acc = acc_b["follower_count"]
  is_correct = check_answer(guess, a_fol_acc, b_fol_acc)

  #Clear screen between each question.
  os.system('cls')
  print(logo)
  
  #Give reply depending on guess.
  #Score updating.
  if is_correct:
    score += 1
    print(f"You got it right! Current score is: {score}\n")
  else:
    game_continue = False
    print(f"Woops, you guessed wrong! Final score was: {score}")