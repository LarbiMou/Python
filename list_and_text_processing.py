# Lab 2 Solution Larbi Moukhlis 1/30/2025 

# Ceate a list that has three different elements:
#   an integer, a Boolean value, and a tuple. 
new_list = [16, False, (30, "January")]


print("The original list is: ", new_list)
print("Enter value to add to the list: ")
new_value = input()
#Add line of code to add value to the end of the list
new_list.append(new_value)


print("After adding new value, the list is now: ", new_list)

#Add code in print statement to print out slice of list
print("The 2nd-3rd items in the list are: ", new_list[1:3])

text_entered = input("Please enter some text: ")
#Add code to create list of words in text_entered 

word_list = text_entered.split()

#Add code in print statement to print out number of words in list
print("There are ", len(word_list)," words in the text")

print("The words in the text you entered are: ", word_list)


