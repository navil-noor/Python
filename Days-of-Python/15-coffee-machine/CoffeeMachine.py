MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_enough(order_ingredients):
    """Returns True when order can be processed, False when resources are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, not enough {item} for this order.")
            return False
    return True


def process_coins():
    """Returns total coins inserted"""
    print("Please insert coins!")
    total = int(input("how many 1 euro cents?: ")) * 0.01
    total += int(input("how many 2 euro cents?: ")) * 0.02
    total += int(input("how many 5 euro cents?: ")) * 0.05
    total += int(input("how many 10 euro cents?: ")) * 0.1
    total += int(input("how many 20 euro cents?: ")) * 0.2
    total += int(input("how many 50 euro cents?: ")) * 0.5
    return total


def is_money_enough(coin_inserted, drink_cost):
    """Return True for enough coins, False when not enough coins"""
    if coin_inserted >= drink_cost:
        change = round(coin_inserted - drink_cost, 2)
        if change > 0:
            print(f"Here is your ${change}, enjoy your drink!")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, this is not enough money. Refunded coins!")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct ordered ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_enough(drink["ingredients"]):
            payment = process_coins()
            if is_money_enough(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
