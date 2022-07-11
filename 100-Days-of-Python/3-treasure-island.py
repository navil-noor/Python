print('''
            $$ $             
             \O/$            
            $ |              
             /_\             
           _|___|_           
         _|___|___|_         
       _|___|___|___|_       
     _|___|___|___|___|_     
   _|___|___|___|___|___|_   
 _|___|___|___|___|___|___|_ 
|___|___|___|___|___|___|___|
 \o/ \o/ \o/ \o/ \o/ \o/ \o/ 
  |   |   |   |   |   |   |  
 / \ / \ / \ / \ / \ / \ / \ 
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ')
if first == "left":
  second = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')

  if second == "wait":
    third = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")

    if third == "yellow":
      print("You found the treasure! You Win!")
    elif third == "red":
      print("It's a room full of fire. Game Over.")
    elif third == "blue":
      print("You enter a room of beasts. Game Over.")

  else:
    print("You get attacked by an angry trout. Game Over.")

else:
  print("You fell into a hole. Game Over.")
