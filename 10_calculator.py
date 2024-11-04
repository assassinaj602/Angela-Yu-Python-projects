logo = print('''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|''')

# part 1
def add(a1, a2):
    return a1 + a2

def sub(a1, a2):
    return a1 - a2

def mul(a1, a2):
    return a1 * a2

def div(a1, a2):
    return a1 / a2

# part 2
operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

# part 3 and part 4
def repeat():
    should_accumulate = True
    num1 = float(input("What's the first number?: "))
    
    while should_accumulate:
        for symbol in operation:
            print(symbol)
        op = input("Pick an operation: ")

        # Validate that the operation is in the dictionary
        if op not in operation:
            print("Invalid operation. Please pick a valid operation.")
            continue
        
        # Validate that the input for num2 is a valid float
        while True:
            try:
                num2 = float(input("What's the next number?: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
        answer = operation[op](num1, num2)
        print(f"{num1} {op} {num2} = {answer}")
        
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)

repeat()
