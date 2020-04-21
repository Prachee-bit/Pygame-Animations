#Story Generator
#@PracheeNanda
#@ICS3U1
#@9/18/2018

#User has to input four details: Name, Year, Place of Birth, Random Word
name = input ("Enter your name: ")
year = input ("Enter a year: ")
placebirth = input ("Enter your place of birth: ")
random = input ("Enter any word: ")

#Prints out a combination of letters and numbers 
print (name[3:-1]+year[2:4]+placebirth[4:-2]+random[2:-1].upper())