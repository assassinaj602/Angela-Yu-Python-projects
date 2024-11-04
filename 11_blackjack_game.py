import random
def print_logo():
    logo = print(""" 
 ____  _            _          _            _       ____                      
| __ )| | __ _  ___| | __     | | __ _  ___| | __  / ___| __ _ _ __ ___   ___ 
|  _ \| |/ _` |/ __| |/ /  _  | |/ _` |/ __| |/ / | |  _ / _` | '_ ` _ \ / _ \
| |_) | | (_| | (__|   <  | |_| | (_| | (__|   <  | |_| | (_| | | | | | |  __/
|____/|_|\__,_|\___|_|\_\  \___/ \__,_|\___|_|\_\  \____|\__,_|_| |_| |_|\___|y
                       
             
    """)

# Function for dealing cards
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Function for calculating the score
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    while sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Function to compare user and computer scores
def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a Draw!"
    elif c_score == 0:
        return "You lose, opponent wins with a Blackjack!"
    elif u_score == 0:
        return "You win with a Blackjack!"
    elif u_score > 21:
        return "You went over. You lose!"
    elif c_score > 21:
        return "Computer went over. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

# Main game function
def play_blackjack():
    print_logo()  # Display the logo at the start of the game

    user_cards = []
    computer_cards = []
    game_over = False

    # Deal two initial cards to both players
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to draw another card, or 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")    
    print(compare(user_score, computer_score))

# Loop to allow the user to play multiple games
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_blackjack()
