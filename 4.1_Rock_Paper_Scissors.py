print('''                                                                                                                                                                                                                                                                                                                                                                                                                                               
##################################################################################################################################################
 __      __       .__                                  __                                                                             
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____                                                                     
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \                                                                    
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )                                                                   
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/                                                                    
       \/       \/          \/            \/     \/                                                                                                                                                                                                                   
                                                                                                                                      
                                                                                                                                      
__________               __          __________                                ____      _________      .__                           
\______   \ ____   ____ |  | __      \______   \_____  ______   ___________   /  _ \    /   _____/ ____ |__| ______ _________________ 
 |       _//  _ \_/ ___\|  |/ /       |     ___/\__  \ \____ \_/ __ \_  __ \  >  _ </\  \_____  \_/ ___\|  |/  ___//  ___/  _ \_  __ \
 |    |   (  <_> )  \___|    <        |    |     / __ \|  |_> >  ___/|  | \/ /  <_\ \/  /        \  \___|  |\___ \ \___ (  <_> )  | \/
 |____|_  /\____/ \___  >__|_ \  /\   |____|    (____  /   __/ \___  >__|    \_____\ \ /_______  /\___  >__/____  >____  >____/|__|   
        \/            \/     \/  )/                  \/|__|        \/               \/         \/     \/        \/     \/             
                                                                                                                                      
                                                                                                                                
  ________                        __________                   __               __                                                    
 /  _____/_____    _____   ____   \______   \_______  ____    |__| ____   _____/  |_                                                  
/   \  ___\__  \  /     \_/ __ \   |     ___/\_  __ \/  _ \   |  |/ __ \_/ ___\   __\                                                 
\    \_\  \/ __ \|  Y Y  \  ___/   |    |     |  | \(  <_> )  |  \  ___/\  \___|  |                                                   
 \______  (____  /__|_|  /\___  >  |____|     |__|   \____/\__|  |\___  >\___  >__|                                                   
        \/     \/      \/     \/                          \______|    \/     \/                                                       

#################################################################################################################################################################
''')


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_input = int(input())
if(user_input==0):
    print("User Choose :")
    print(rock)
elif(user_input==1):
    print("User Choose :")
    print(paper)
elif(user_input==2):
    print("User Choose :")
    print(scissors)
else:
    print("You entered the wrong Option")
########################################################################################
computer_action = random.randint(0,2)
if(computer_action==0):
    print("Computer Choose :")
    print(rock)
elif(computer_action==1):
    print("Computer Choose :")
    print(paper)
elif(computer_action==2):
    print("Computer Choose :")
    print(scissors)
else:
    print("You entered the wrong Option")
 ######################################################################################   
if(user_input == computer_action):
    print("tie") 
elif(user_input==0 and computer_action==1):
    print("Computer Wins")
elif(user_input==1 and computer_action==2):
    print("Computer Wins")
elif(user_input==2 and computer_action==0):
    print("Computer Wins")
elif(user_input==1 and computer_action==0):
    print("You Win!")
elif(user_input==2 and computer_action==1):
    print("You Win!")
elif(user_input==0 and computer_action==2):
    print("You Win!")
#################################################################################################
    
    
