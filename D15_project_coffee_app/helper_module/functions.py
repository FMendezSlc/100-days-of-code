def print_report(resources):
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: ${resources['money']}"
    )

def show_cost(order, menu):
    print(f"That'll be ${menu[order]['cost']}")
    return menu[order]['cost']

def check_resources(order, menu, resources):
    item = menu[order]["ingredients"]

    if item['water'] <= resources['water']:
        return True
    elif item['water'] > resources['water']:
        print("Sorry, not enough water.")
        return False
    if item['milk'] <= resources['milk']:
        return True
    elif item['milk'] > resources['milk']:
        print("Sorry, not enough milk.")
        return False
    if item['coffee'] <= resources['coffee']:
        return True
    elif item['coffee'] > resources['coffee']:
        print("Sorry, not enough coffee.")
        return False
    return False

def calculate_money(coin, amount, coins):
    value = coins[coin]
    return value * amount

def adjust_resources(order, menu, resources):

    item = menu[order]["ingredients"]
    for key, value in item.items():
        resources[key] -= value