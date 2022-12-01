#Calculations
from art import logo
print(logo)

#add
def add(n1, n2):
  return n1 + n2

#subtract
def sub(n1, n2):
  return n1 - n2

#multiply
def mult(n1,n2):
  return n1 * n2

#divide
def div(n1, n2):
  return n1/n2

#dictionary to keep all operation functions
operations = {
  "+" : add,
  "-" : sub,
  "*" : mult,
  "/" : div,
}

def calculator():
  #user inputs - the first number for calculations
  num1 = float(input("Type the first number: "))
  
  #loop through operations then choosing the operation
  for symbol in operations:
    print(symbol)
  
  continue_calc = True
  while continue_calc:
    chosen_symbol = input("Select an operation: ")
    
    #user inputs - the second number for calculations
    num2 = float(input("Type the next number: "))
    
    calculation_function = operations[chosen_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {chosen_symbol} {num2}, result = {answer}")
  
    player_continue = input(f"Type 'y' for more calculation with {answer} or 'n' to make another calculation: ")
    if player_continue == 'y':
      num1 = answer
    else:
      continue_calc = False
      calculator()

calculator()