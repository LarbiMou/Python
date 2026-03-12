# Description: This program analyzes students grades by sorting them in a predetermined list
# and allowing the user to input their own grade. It then compares the user's 
# grade to some key statistics, including the minimum, median, and maximum values.
# The program also includes a nested condition to check how close the user's grade isto the median
# Program: Grade Comparison
# Author: Larbi Moukhlis
# Date: 02/13/2025

# A list of students grades
grades = [72, 85, 90, 67, 88, 76, 95, 89, 80, 91]

# Using a list method; Sort the list
grades.sort()

# Use a built-in function: Find min, max, and median
minimum = min(grades)
maximum = max(grades)
# Finding median assuming the list length is odd
median = grades[len(grades) // 2]  

# Get user input
user_grade = float(input("Enter your grade to compare with the class statistics: "))

# Compare user input with min, median, and max using if-elif-else statements
if user_grade < minimum:
    print(f"Your grade {user_grade} is lower than the lowest grade in the class ({minimum}).")
    
elif user_grade == minimum:
    print(f"Your grade {user_grade} is exactly the lowest grade in the class ({minimum}).")
    
elif user_grade < median:
    print(f"Your grade {user_grade} is greater than the lowest grade but below the class median ({median}).")
    
    # Nested if statement: Checking if the grade is close to the median
    if median - user_grade <= 5:
        print("You're very close to the median!")
    else:
        print("You're quite a bit below the median.")


elif user_grade == median:
    print(f"Your grade {user_grade} is exactly the median grade ({median}).")
    
elif user_grade < maximum:
    print(f"Your grade {user_grade} is above the median but below the highest grade ({maximum}).")
    
elif user_grade == maximum:
    print(f"Your grade {user_grade} is exactly the highest grade in the class ({maximum}).")
    
else:
    print(f"Your grade {user_grade} is higher than the highest grade in the class ({maximum}).")
