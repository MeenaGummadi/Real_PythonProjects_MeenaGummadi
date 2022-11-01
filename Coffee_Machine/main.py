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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins(amount):
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many Pennies?: ")) * 0.
    if total >= amount:
        change = round((total - amount), 2)
        print(f"Here is your {change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(ingredients):
    for item in ingredients:
        resources[item] = resources[item] - ingredients[item]


price = 0


def coffee_machine():
    is_on = True
    global price
    while is_on:
        prompt = input("What would you like? (espresso, latte, cappuccino): ")
        if prompt == "off":
            is_on = False
        elif prompt == "report":
            print(f"Water: {resources['water']} ml")
            print(f"Milk: {resources['milk']} ml")
            print(f"Coffee: {resources['coffee']} gm")
            print(f"Money: {price}")
        else:
            drink = MENU[prompt]
            if resource_sufficient(drink["ingredients"]):
                if process_coins(drink['cost']):
                    price += drink['cost']
                    make_coffee(drink["ingredients"])
                    print(f"Enjoy your {prompt}")


coffee_machine()
