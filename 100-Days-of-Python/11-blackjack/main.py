############### Blackjack Project #####################

############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
#Exclude replit function as it will not work without replit
from replit import clear

#Deals a random card from the list
def deal_card():
  """This returns a random card from the cards list"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  chosen_card = random.choice(cards)
  return chosen_card

#Compares the cards to figure out the result of the game
def compare_score(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You passed over 21, you lose!"
  if user_score == computer_score:
    return "The game is a tie!"
  elif computer_score == 0:
    return "You lost. Computer has blackjack!"
  elif user_score == 0:
    return "You won with a blackjack!"
  elif user_score > 21:
    return "You passed over 21, you lose!"
  elif computer_score > 21:
    return "Computer went over 21, you win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lost!"


def calculate_score(cards):
  """Outputs total score by the cards in hand"""
  #Blackjack during first deal result
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #If score goes over 21 then 11 becomes 1 (value of A)
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)  
  return sum(cards)

#Starting the blackjack game
def blackjack_game():
  """Starts the entire blackjack game"""
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    #Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, score is: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score > 21 or user_score == 0 or computer_score == 0:
      is_game_over = True
    else:
      user_deal = input("Type 'y' to get another card, or 'n' to pass: ")
      if user_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  #Once the user is done, the computer keeps drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  #Showing the cards at hand of player and one of computer's
  print(f"You have in your hand: {user_cards}, you scored: {user_score}")
  print(f"The computer has: {computer_cards}, the computer's score is: {computer_score}")
  print(compare_score(user_score, computer_score))


#Ask the user if they want to restart the game
while input("Want to play blackjack? Type 'y' for yes or 'n' for no. "):
  #Exclude clear function as it will not work without replit
  clear()
  blackjack_game()