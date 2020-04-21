#Doubling Effect
#@PracheeNanda
#@ICS3U1
#@9/18/2018

#--------------------#

print ("Welcome to Square-i-nator")

print ()

valid = False
#If user enters a wrong value, it asks again
while valid == False:
    try: 
        square = int (input("Enter number of squares on one side:"))
        #Ensures user can't enter a number above 10 or below 0
        if square >= 0 and square <= 10:
            valid = True
        else:
            print ("Out of Range! You seemed to have entered a number not within the range!")
            valid = False
    #Ensures user enters a number, not letters or symbols
    except ValueError:
        print ("Error! You seemed to have not entered a number!")

#Finds total squares
squares = square * square

print ()

#Variables

grains = 0
totalgrains = 0

#Process

#Determines number of grains on a particular square and then all squares preceding it
while (squares > 0):
    grains = 2 ** (squares - 1)
    print ("Square",squares,"has",grains, "grains of rice.")
    totalgrains = totalgrains + grains
    squares = squares - 1

print ()

#Output

#Prints the total number of grains
print ("The total number of grains he received is "+ str(totalgrains) +".")

#--------------------#