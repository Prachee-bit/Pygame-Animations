#Zodiac Compatibilty
#@PracheeNanda
#@ICS3U1
#@11/26/2018

#--------------------#

def getDate (): #gets valid input from user
    valid = False
    while valid == False:
        try:
            print ("Please enter the date as MonthDate. Eg: Mar16")
            date = input("Enter date (mm/dd): ")
            month = date [0:3]   #divides input into month and day
            day = int(date [4:6])
            replies = ["Jan","Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            if month in replies:
                valid = True
            else:
                print ("Not Valid!")
                valid = False
            if day >= 0 and day <= 31:
                valid = True
            else:
                print ("Out of Range! You seemed to have entered a number not within the range!")
                valid = False
        except ValueError:
            print ("Error! You seemed to have not entered a valid response!")
            valid = False
    return month,day

def getBirthday (month, date):
    user = 0 #gets the zodiac sign
    if month == "Jan":
        if date > 20:
            user = ("Capricorn")
        elif date < 20:
            user = ("Sagittarius")
    elif month == "Feb":
        if date > 16:
            user = ("Aquarius")
        elif date < 16:
            user = ("Capricorn")
    elif month == "Mar":
        if date > 11:
            user = ("Pisces")
        elif date < 11:
            user = ("Aquarius")
    elif month == "Apr":
        if date > 18:
            user = ("Aries")
        elif date < 11:
            user = ("Pisces")
    elif month == "May":
        if date > 13:
            user = ("Taurus")
        elif date < 13:
            user = ("Aries")
    elif month == "Jun":
        if date > 21:
            user = ("Gemini")
        elif date < 21:
            user = ("Taurus")
    elif month == "Jul":
        if date > 20:
            user = ("Cancer")
        elif date < 21:
            user = ("Gemini")    
    elif month == "Aug":
        if date > 21:
            user = ("Leo")
        elif date < 21:
            user = ("Cancer")
    elif month == 'Sep':
        if date > 16:
            user = ("Virgo")
        elif date < 16:
            user = ("Leo")
    elif month == "Oct":
        if date > 30:
            user = ("Virgo")
        elif date < 30:
            user = ("Libra")
    elif month == "Nov":
        if date < 23:
            user = ("Libra")
        elif date > 23 and date < 29:
            user = ("Scorpio")
        elif date > 29:
            user = ("Ophiuchus")
    elif month == ("Dec"):
        if date < 17:
            user = ("Ophiuchus")
        elif date > 17:
            user = ("Saggitarius")
    return user

def getCompatibility (signone, signtwo): #gets compatibilty
    fire = ["Aries", "Leo", "Saggitarius"]
    earth = ["Capricorn", "Taurus", "Virgo"]
    water= ["Pisces", "Cancer", "Scorpio"]
    air = ["Gemini", "Aquarius", "Libra"]
    
    if signone in fire:
        if signtwo in fire: #checks to see if they are in the same list to determine compatibility
            answer = ("They are compatible")
        else:
            answer = ("They are not compatible")
    elif signone in water:
        if signtwo in water:
            answer = ("They are compatible")
        else:
            answer = ("They are not compatible")
    elif signone in air:
        if signtwo in air:
            answer = ("They are compatible")
        else:
            answer = ("They are not compatible")
    elif signone in earth:
        if signtwo in earth:
            answer = ("They are compatible")
        else:
            answer = ("They are not compatible")
            
    elif signone == ("Ophiuchus"): #only compatible with themselves
        if signtwo == ("Ophiuchus"):
            answer = ("They are compatible")
        else:
            answer = ("They are not compatible")
            
    return answer

#main
monthone, dayone = getDate()
monthtwo, daytwo = getDate()

signone = getBirthday (monthone, dayone)
signtwo = getBirthday (monthtwo, daytwo)

print ("Your sign was", signone+ ". The sign of your other half was",signtwo+".") 

compatible = getCompatibility (signone, signtwo)
print (compatible)
