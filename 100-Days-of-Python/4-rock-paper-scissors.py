rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
option = [rock, paper, scissors]

print("Welcome to the Rock Paper Scissors Game!\n")

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print("\nYou chose:")
print(option[player])

computer = int(random.randint(0, 2))
print("\nComputer chose:")
print(option[computer])

if player == computer:
  print("Both chose the same, it's a tie!")

elif player == 0 and computer == 1:
  print("Bad luck, computer chose Paper and you lost!")

elif player == 0 and computer == 2:
  print("Hurray! Computer chose Scissors and you won!")

elif player == 1 and computer == 0:
  print("Hurray! Computer chose Rock and you won!")

elif player == 1 and computer == 2:
  print("Bad luck, computer chose Scissors and you lost!")

elif player == 2 and computer == 0:
  print("Bad luck, computer chose Rock and you lost!")

elif player == 2 and computer == 1:
  print("Hurray! Computer chose Paper and you won!")

else:
  print("You did not select 0, 1, or 2 so you lose!")