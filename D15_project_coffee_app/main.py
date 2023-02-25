from helper_module.resources import menu, coins, resources
from helper_module import functions as fc

working = True
while working:

    order = input("What would you like? (espresso/latte/cappuchcino)\n")

    if order == "off":
        exit()
    elif order == "report":
        fc.print_report(resources)
    else:
        cost = fc.show_cost(order, menu)
        
        proceed = fc.check_resources(order, menu, resources)

        if proceed == True:
            pay = 0
            print("Please insert your coins: ")
            quarts = int(input("Quarters: "))
            amount = fc.calculate_money('quarter', quarts, coins)
            pay += amount
            if pay < cost:
                diff = cost-pay
                print(f"${diff} remains")
                dimes = int(input("Dimes: "))
                amount = fc.calculate_money('dime', dimes, coins)
                pay += amount
                if pay < cost:
                    diff = cost-pay
                    print(f"${diff} remains")
                    nickles = int(input("Nickels: "))
                    amount = fc.calculate_money('nickle', nickles, coins)
                    pay += amount
                    if pay < cost:
                        diff = cost-pay
                        print(f"${diff} remains")
                        pennies = int(input("Pennies: "))
                        amount = fc.calculate_money('penny', pennies, coins)
                        pay += amount
                        if pay < cost:
                            print("Sorry, not enough money. Money refunded...")
                            working = False
            resources['money'] += pay
            fc.adjust_resources(order, menu, resources)

            if pay > cost:
                change = cost-pay
                print(f"Your change: ${change}")

        else:
            working = False

