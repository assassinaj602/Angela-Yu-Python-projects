print("Welocme to the tip calculator")
bill = input("What was the total bill in $?")
tip = input("what amount of tip would you like to give i.e 12$ ,15$ ,20$")
new_tip = int(bill) * int(tip) / 100
total_money = new_tip + int(bill)
split = input("How many people do you want to split the money with = ")
each_bill = total_money / float(split)
print("Each person should pay : " + str(each_bill) + "$")