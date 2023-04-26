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


def check_input():
    user_input = ""
    while user_input != "espresso" and user_input != "latte" and \
            user_input != "cappuccino" and user_input != "off" and user_input != "report":
        user_input = input("What would you like? (espresso($1.50)/latte($2.50)/cappuccino($3.00)): ").lower()
    return user_input


def print_report(current_money):
    for key in resources:
        if key == "coffee":
            print(f"{key.capitalize()}: {resources[key]}g")
        else:
            print(f"{key.capitalize()}: {resources[key]}ml")
    print(f"Money: ${current_money}")


def check_resources(coffee_type):
    coffee_type = coffee_type.lower()
    ingredients = MENU[coffee_type]["ingredients"]
    if coffee_type == "espresso":
        for ingredient in ingredients:
            if ingredients[ingredient] > resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False
    elif coffee_type == "latte":
        for ingredient in ingredients:
            if ingredients[ingredient] > resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False
    elif coffee_type == "cappuccino":
        for ingredient in ingredients:
            if ingredients[ingredient] > resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False
    else:
        return "invalid input"
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters ($0.25)? ")) * 0.25
    dimes = int(input("How many quarters ($0.10)? ")) * 0.10
    nickles = int(input("How many quarters ($0.05)? ")) * 0.05
    pennies = int(input("How many quarters ($0.01)? ")) * 0.01
    total_money = quarters + dimes + nickles + pennies
    return round(total_money, 2)


def check_transaction(money, coffee_type):
    if money < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money > MENU[coffee_type]["cost"]:
        change = money - MENU[coffee_type]["cost"]
        profit = money - change
        print(f"Here is ${round(change, 2)} in change.")
        return profit
    else:
        profit = money  # just making it clear
        return round(profit, 2)


def make_coffee(coffee_type):
    ingredients = MENU[coffee_type]["ingredients"]
    if coffee_type == "espresso":
        for ingredient in ingredients:
            resources[ingredient] = resources[ingredient] - ingredients[ingredient]
        return True
    elif coffee_type == "latte":
        for ingredient in ingredients:
            resources[ingredient] = resources[ingredient] - ingredients[ingredient]
        return True
    elif coffee_type == "cappuccino":
        for ingredient in ingredients:
            resources[ingredient] = resources[ingredient] - ingredients[ingredient]
        return True
    else:
        return "error in make_coffee function"


def main_loop():
    profit = 0
    is_machine_on = True

    while is_machine_on:
        user_input = check_input()
        if user_input == "report":
            print_report(profit)
        elif user_input == "off":
            is_machine_on = False
        else:
            has_resources = check_resources(user_input)
            if has_resources:
                money = process_coins()
                profit = check_transaction(money, user_input)
                if money:
                    make_coffee(user_input)
                    print(f"Here's your {user_input} ☕")


main_loop()