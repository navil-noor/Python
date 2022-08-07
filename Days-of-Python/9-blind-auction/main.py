from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bidding = {}
bidding_ends = False

def find_winner(bids_made):
  highest_bid = 0
  winner = ""
  for bidder in bids_made:
    bid_amount = bids_made[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"\nThe winning bid goes to {winner} with a bid of ${highest_bid}.")

while not bidding_ends:
  name = str(input("What is your name?: "))
  bid = int(input("\nPlace your bid!: $"))
  bidding[name] = bid
  more_bids = input("\nAre there any more bidders? Type 'yes' for more or 'no' to end. ")
  if more_bids == 'no':
    bidding_ends = True
    find_winner(bidding)
  elif more_bids == "yes":
    clear()