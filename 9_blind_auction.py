logo = print( '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

bids = {}
def highest_bidder(bidding_dictionary):
    highest_bid=0
    for bidder in bidding_dictionary:
        
        bid_amount = bidding_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner = bidder
    print(f"Winner is {winner} with a bid of {highest_bid}.")
    
#---------------------------------------------------------------------
cont_inue = True
while cont_inue:
    Names = input("What is your name? :")
    Prices = int(input("What is your bid : $"))
    bids[Names] = int(Prices)
    cont_inue= input("Do you want to add any other bidder type 'Y' or 'N'\n").lower()
    if cont_inue == 'n':
        cont_inue= False
        highest_bidder(bids)
    elif cont_inue == "y":
        print("\n" *1)
     
    