print('''
***************************************************************
 _                                                           
| |                                                          
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
| __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                      | |    
                                                      |_|    

****************************************************************

                 _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `\
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\
//
****************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("Where you want  to go? Left or Right?\npress L for left and R for Right")
where = str(input())
if(where == "L"):
    print("You've come to a lake. There is an island in the middle of the lake.  Type 'W' to wait for a boat. Type 'S' to swim across.")
    action= str(input())
    if(action=="W"):
        print("You arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue. Which colour do you choose?")
        print("Type 'Y' for yellow door, 'R' for Red door, 'B' for Blue door")
        color=str(input())
        if(color=="Y"):
            print("You win! You Found the treasure!")
        elif(color=="R"):
            print("You entered a wrong room full of ghosts./nGAME OVER!")
        elif(color=="B"):
            print("You enetered a Criminal's room and killed./nGAME OVER!")
        else:
            print("You enterd the wrong color.\nGame become disturbed")

    elif(action=="S"):
        print("You get attacked by an angry trout./nGAME OVER!")
    else:
        print("You enterd the wrong action.\nGame become disturbed")
elif(where=="R"):
    print("You fell into a hole./nGAME OVER!")
else:
    print("You enterd the wrong location.\nGame become disturbed")