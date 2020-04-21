def getInput ():     #gets a valid input
    valid = False
    while valid == False:
        try: 
            word = input ("Type done or enter a word: ")
            valid = True
        except ValueError:
            print ("Error! You seemed to have not entered a valid response!")
            valid = False
    return word
           
def getCase (word):
    newSentence = "" #creates a variable to store new sentence
    i = 0 #an index counter
    
    for letter in word: #divides sentence into letters
        if letter == " ": #if it is a space
           i = 2          #index counter is reset for next word
           newSentence = newSentence + " "
           
        else:
            if i % 2 == 0 : #if it is the first letter, then turns it into lower
                newSentence = newSentence + letter.lower()
                
            else:    #if it is the not the first letter, then turns it into upper
                newSentence = newSentence + letter.upper()
                
            i = i + 1
    return newSentence

word = getInput()

while word != "done":
    print (getCase(word))
    word = getInput()

print ("Have a nice day!")
