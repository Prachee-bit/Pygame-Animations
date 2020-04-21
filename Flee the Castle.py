#Story Generator
#@PracheeNanda
#@ICS3U1
#@9/18/2018

#--------------------#

print ("Flee The Castle".center(50,'-'))

print ("")

#User inputs name
user = input("Enter your name: ")

print ("")

print ("Hey", user+"! Welcome to Flee the Castle")

print ('')

print ("Storyline: You are,", user+ ", the princess of Crawford which a country that is currently under attack! All guards are busy fending the enemy off, so it is up to you to flee the castle")

print()

print ("Objective: Escape the kingdom or fall with it...")

print()

replies = ("A", "a" , "B" , "b")

#First Choice: User decides if they are ready for an exciting adventure. Options include Yes or No

print ("Are you ready for an exciting adventure?")

choice = input("A for Yes or B for No?: ")

print ("")

if choice == "A" or "a":
    print ("Great!")
elif choice == "B" or "b": 
    print ("Doesn't matter! You will be doing this anyway")

print ("")

print ("Mage: Princess! You must leave now! Escape through the underground tunnel. You know the way, my liege!")

print()

print("'You go down the secret entrance but have forgotten to close the door!'")

print ()

print("You: Oh no! What am I going to do?")

#Second Choice: User decides if they want to close door. If user chooses to close the door, the game ends. If not, it continues.
closedoor = input("Type A to go back and close the door or Type B to continue walking")

if closedoor == "A":
    print ("'You go back to close the door.'")
    print ()
    
    print ("Guard 1: There she is! Get her, now!")
    print ("'You get killed.'")
    print ()
    print ("-----------Game Over, You LOSE!-----------") 
    
#Note: Everything after this is a nested loop.
elif closedoor == "B":
     print ("'You keep walking and reach an intersection'")
     print ()
     
     print ("Prince of Abek:",user+"! What are you doing here? You should be out of here long ago!")
     print()
     
     print("You: It's a long story...Do you know where the escape route is?")
     print()
     
     print("Prince of Abek: Yes, It's this way but shouldn't you know that? After all, the mages made sure you did...")
     print()
     
     print("You: Didn't really pay attention to them.")
     print()
     
     print("'Suddenly, you notice the sound of footsteps from where he was going. Before you can do anything, the prince is captured by the guards. They don't notice you as you are in the dark.'")
     
#Third choice: User chooses to either leave or save the prince. One choice will end the game (to leave the prince) while the other one will let it continue!
     capture = input ("Type A to save the prince and go or Type B to leave in the other direction")
     
     if capture == "A":
        print ("'You stand still at the same spot, but for not too long.The Prince of Abek rats you out to the guards. You have been captured.")
        print ()
        print ("-----------Game Over, You LOSE!-----------") 

     elif capture == "B":
        print ()
        print ("'You promise yourself you will be back to save him but for now you will have to leave. You take the other route'")
        print()
        print ("Mage: Princess,  you have finally arrived! Your parents were gett-")
        print()
        print ("You: Yes, I know but you have to first save the Prince of Abek. He was captured by the enemies!")
        print()
        print ("Mage: But your liege, he is the man who issued the attacks!")
        print()
        
#Fourth choice: User chooses from three option. The game will end if they choose to help the prince or they will win if they choose to take revenge or send their troops.
        finale = input ("What would you like to do? Type A to send troops immediately, B to forgive him or C to take revenge.")
        
        if finale == "A":
            print ("'You send in the remaining troops where you last saw him!'")
            print()
            
            print ("'You defeat his troops!'")
            print()
            print ("-----------Game Over, You win!-----------")
            
        elif finale == "B":
            
            print ("'You forgive him and send 50,000 gold coins to call it truce'")
            print()
            print ("'He doesn't take accept it. Instead, he orders another attack and wipes out your kingdom")   
            print ()
            print ("-----------Game Over, You LOSE!-----------") 
        elif finale == "C":
            print ("'You decide to take revenge by destroying his country'")
            print ("'You are successful and have decided to use his riches to rebuild yours!'")
            print ("-----------Game Over, You win!-----------") 

#If the user doesn't enter an expected answer!
else:
    print ("Error!")
    
#--------------------#
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    