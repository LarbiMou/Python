# Lab 4 Solution 2/13/25 Larbi Moukhlis

#prompt user to enter some text amd then text to find within the text
string_entered = input("Please enter some text: ")
substring = input("Enter text to find within that text, or 'end': ")

#Add code for loop to allow user to count multiple text examples

while substring != "end":

    num_times = 0

    #Add code for loop to count how many times text example is in text
    for index in range(len(string_entered)):
        if string_entered[index:index+len(substring)] == substring:
            num_times = num_times + 1
                
    #report how many times text example is in text
    print(substring,"is in the text entered:",num_times, "times")

    #prompt user to enter another text example or end

    substring = input("Enter text to find within that text, or 'end':")

print("Thank you, have a great day!")

