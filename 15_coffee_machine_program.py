choice = ""
water = 300
milk = 200
coffee = 100
money = 0
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "report":
        
        report = print(f"Report:\nwater = {water}ml \nmilk = {milk}ml \ncoffee = {coffee}g \nmoney = {money}$")            
    elif choice == "espresso":
        espresso_price = 1.50
        espresso_water = 15
        espresso_coffee = 18
        if water>espresso_water and coffee>espresso_coffee:
            print(f"Enter the amount of 1.50$")
            quarter = int(input("Enter the amount in quarters = "))
            dime = int(input("Enter the amount in dimes = "))
            nickle = int(input("Enter the amount in nickles = "))
            pennies = int(input("Ente the amount in pennies = "))
            total_money = (quarter*0.25)+(dime*0.1)+(nickle*0.05)+(pennies*0.01)
            print(f"The Total amount entered is = {total_money}")
            if(total_money > espresso_price):
                change_of_Money = total_money - espresso_price
                print(f"Here is the change of : {change_of_Money:.2f}$")
                print("Here is your espresso. Enjoy!.")
                water -= espresso_water
                coffee -= espresso_coffee
                money += espresso_price
            elif total_money == espresso_price :
                print("Here is your espresso. Enjoy!.")
                water -= espresso_water
                coffee -= espresso_coffee
                money += espresso_price
            else:
                print("Your money returned due to insufficient amount entered")
        elif water<espresso_water and coffee>espresso_coffee:
            print("Sorry there is not enough water in the machine.")
        elif(water>espresso_water and coffee<espresso_coffee):
            print("Sorry there is not enough coffee in the machine")  
        else:
            print("Sorry there are not enough water and coffee in the machine.")  
        # new_water = water-espresso_water
        # new_coffee = coffee-espresso_coffee
        # new_report = f"water = {new_water}\nmilk = {milk}\ncoffee = {new_coffee}\nmoney = {(money + espresso_price)}"
    
    elif(choice=="latte"):
        latte_price = 2.50
        latte_water = 200
        latte_coffee = 24
        latte_milk = 150

        if water>latte_water and coffee>latte_coffee:
            print(f"Enter the amount of 2.50$")
            quarter = int(input("Enter the amount in quarters = "))
            dime = int(input("Enter the amount in dimes = "))
            nickle = int(input("Enter the amount in nickles = "))
            pennies = int(input("Ente the amount in pennies = "))
            total_money = (quarter*0.25)+(dime*0.1)+(nickle*0.05)+(pennies*0.01)
            print(f"The Total amount entered is = {total_money}")
            if(total_money > latte_price):
                change_of_Money = total_money - latte_price
                print(f"Here is the change of : {change_of_Money:.2f}$")
                print("Here is your latte. Enjoy!.")
                water -= latte_water
                coffee -= latte_coffee
                milk -= latte_milk
                money += latte_price
            elif total_money == latte_price :
                print("Here is your Latte. Enjoy!.")
                water -= latte_water
                coffee -= latte_coffee
                milk -= latte_milk
                money += latte_price
            else:
                print("Your money returned due to insufficient amount entered")
        elif water<latte_water and coffee>latte_coffee:
            print("Sorry there is not enough water in the machine.")
        elif(water>latte_water and coffee<latte_coffee):
            print("Sorry there is not enough coffee in the machine")  
        else:
            print("Sorry there are not enough water and coffee in the machine.") 
            
    elif choice == "cappuccino":
        cappuccino_price = 3.00
        cappuccino_water = 250
        cappuccino_coffee = 24
        cappuccino_milk = 100
        
        if water>cappuccino_water and coffee>cappuccino_coffee:
            print(f"Enter the amount of 2.50$")
            quarter = int(input("Enter the amount in quarters = "))
            dime = int(input("Enter the amount in dimes = "))
            nickle = int(input("Enter the amount in nickles = "))
            pennies = int(input("Ente the amount in pennies = "))
            total_money = (quarter*0.25)+(dime*0.1)+(nickle*0.05)+(pennies*0.01)
            print(f"The Total amount entered is = {total_money}")
            
            if(total_money > cappuccino_price):
                change_of_Money = total_money - cappuccino_price
                print(f"Here is the change of : {change_of_Money:.2f}$")
                print("Here is your cappuccino. Enjoy!.")
                water -= cappuccino_water
                coffee -= cappuccino_coffee
                milk -= cappuccino_milk
                money += cappuccino_price
            
            elif total_money == cappuccino_price :
                print("Here is your cappuccino. Enjoy!.")
                water -= cappuccino_water
                coffee -= cappuccino_coffee
                milk -= cappuccino_milk
                money += cappuccino_price
            else:
                print("Your money returned due to insufficient amount entered")
        
        elif water<cappuccino_water and coffee>cappuccino_coffee:
            print("Sorry there is not enough water in the machine.")
        elif(water>cappuccino_water and coffee<cappuccino_coffee):
            print("Sorry there is not enough coffee in the machine")  
        else:
            print("Sorry there are not enough water and coffee in the machine.") 
    
    elif choice == "off".lower():
        is_on = False
    else:
        print("You entered a wrong name of coffee try again")
        
            
            
        
          
        
            
    
            
            
    
    