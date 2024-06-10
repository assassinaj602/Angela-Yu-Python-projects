print("Thank you for choosing Python Pizza Deliveries!")
print("What size pizza do you want? S, M, or L")
size = input()
print("Do you want pepperoni? Y or N")
add_pepperoni = input()
print("Do you want extra cheese? Y or N")
extra_cheese = input()

if (size == "L"):

    if (add_pepperoni == "Y" and extra_cheese == "Y"):
        price = 29
        print(f"Your final bill is:{str(price)} $.")
    elif (add_pepperoni == "N" and extra_cheese == "Y"):
        price = 26
        print(f"Your final bill is:{str(price)} $.")
    elif (add_pepperoni == "Y" and extra_cheese == "N"):
        price = 28
        print(f"Your final bill is:{str(price)} $.")
    elif (add_pepperoni == "N" and extra_cheese == "N"):
        price = 25
        print(f"Your final bill is:{str(price)} $.")

if (size == "M"):

    if (add_pepperoni == "Y" and extra_cheese == "Y"):
        price = 24
        print(f"Your final bill is:{str(price)} $.")
    elif (add_pepperoni == "N" and extra_cheese == "Y"):
        price = 21
        print(f"Your final bill is:{str(price)} $.")
    elif (add_pepperoni == "Y" and extra_cheese == "N"):
        price = 23
        print(f"Your final bill is:{str(price)} $.")
    elif (add_pepperoni == "N" and extra_cheese == "N"):
        price = 20
        print(f"Your final bill is:{str(price)} $.")

if (size == "S"):

    if (add_pepperoni == "Y" and extra_cheese == "Y"):
        price = 18
        print(f"Your final bill is:{str(price)} $.")
    elif (add_pepperoni == "N" and extra_cheese == "Y"):
        price = 16
        print(f"Your final bill is:{str(price)} $.")
    elif (add_pepperoni == "Y" and extra_cheese == "N"):
        price = 17
        print(f"Your final bill is:{str(price)} $.")
    elif (add_pepperoni == "N" and extra_cheese == "N"):
        price = 15
        print(f"Your final bill is:{str(price)} $.")
