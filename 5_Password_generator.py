print('''```
  ____           ____                                     _     ____                           _             
 |  _ \ _   _   |  _ \ __ _ ___ _____      _____  _ __ __| |   / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | |_) | | | |  | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |  | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 |  __/| |_| |  |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |  | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|    \__, |  |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|   \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
        |___/                                                                                                
```''')
#importing random
import random
#Working with letters
letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p','q','r','s','t','u','v','w','x','y','z']
#Working with Symbols
symbols = ['!','@','#','$','%','^','&','*','?','~','|']
##Working with numbers
numbers = ['0','1','2','3','4','5','6','7','8','9']

#program Menu
print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password?")
letter = int(input())
print("How many symbols would you like?")
symbol = int(input())
print("How many numbers would you like?")
number = int(input())
print("Press 1 for unshuffled Password or press 2 for shuffled password")
option = int(input())
#program backend work
if option == 1:
    password = ""
    password1 = ""
    password2 = ""
    password3 = ""
    for ran_character in range(1,letter + 1):
            random_char = random.choice(letters)
            password1 = password1 + random_char
    for ran_symbol in range(1,symbol+1):
            random_symbol = random.choice(symbols)
            password2 = password2 + random_symbol
    for ran_number in range(1,number+1):
            new_number = random.choice(numbers)
            password3 = password3 + new_number
    #Final Displaying work
    password = password1 + password2 + password3
    print(f"Your password is:{password}")

#hard level
elif option == 2:
    password = []
    for ran_character in range(1,letter + 1):
            password.append(random.choice(letters)) 
    for ran_symbol in range(1,symbol+1):
            password.append(random.choice(symbols))
    for ran_number in range(1,number+1):
            password.append(random.choice(numbers))
    random.shuffle(password)
    new_password = "".join(password)
    print(new_password)
#ELSE
else:
    print("Select the correct option")
    