# Lab 1: Part A, Larbi Moukhlis 1.23.2025
import convert_ftoc as ftc 

# Ask user to enter temperature in Fahrenheit
temp_f = input("Please enter a temperature in Fahrenheit: ")
print("The temperature entered was: " + temp_f)

# code that uses fahr_to_celsius function to determine
#  temperature in Celsius from user entered temperature

temp_c = ftc.fahr_to_celsius(float(temp_f))


#The following line of code displays result
print(temp_f + " Degrees Fahrenheit is equivalent to " + 
       str(temp_c) + " degrees Celsius")


