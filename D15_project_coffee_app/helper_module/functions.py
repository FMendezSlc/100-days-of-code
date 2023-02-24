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
    else:
        print("Sorry, not enough water.")
    if item['milk'] <= resources['milk']:
        return True
    else:
        print("Sorry, not enough milk.")

    if item['coffee'] <= resources['coffee']:
        return True
    else:
        print("Sorry, not enough coffee.")
    return False

def calculate_money(coin, amount, coins):
    value = coins[coin]
    return value * amount

def adjust_resources(order, menu, resources):

    item = menu[order]["ingredients"]
    for key, value in item.items():
        resources[key] -= value