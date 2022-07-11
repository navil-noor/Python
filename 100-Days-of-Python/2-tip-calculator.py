#Tip Calculator

print("Welcome to the tip calculator!")

total_bill = input("\nWhat was the total bill? ")

tip = input("\nHow much tip would you like to give? 10, 12, or 15? ")

tip_percent = 1 + (int(tip) / 100)

total_people = input("\nHow many people to split the bill? ")

each_pays = (float(total_bill) * tip_percent) / int(total_people)

round_pay = str(round(each_pays, 2))
# also can use "{:.2f}".format(each_pays) to round up to 2 decimal place

print(f"\nEach person should pay: ${round_pay}")
