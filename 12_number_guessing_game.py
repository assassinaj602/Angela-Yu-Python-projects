import random
logo  = '''
 _______               ___.                    ________                            .__                   ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
'''
easy_level_turns = 10
hard_level_turns = 5
turns = 0
#Function to check answer
def check_answer(user_guess , actual_answer,turns):
    if user_guess>actual_answer:
        print("Too High")
        return turns-1
    elif user_guess<actual_answer:
        print("Too low")
        return turns-1
    else:
        print(f"You guessed it Right! The answer was {actual_answer}")
        
#Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        global turns
        return easy_level_turns
    else:
        return hard_level_turns
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1,100)
    print(f"The correct answer is {answer}")
    turns = set_difficulty()
    
    guess = 0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess number")
        guess = int(input("guess a number : "))
        turns  = check_answer(guess,answer,turns)
        if turns == 0:
            print("you have run out of turns, game Lose!")
            return
        elif guess!=answer:
            print("Guess again")
    
game()