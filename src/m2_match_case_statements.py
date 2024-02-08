###############################################################################
# DONE: 1. (3 pts)
#
#   Write a function called color_picker() that prints out a message to a user.
#
#   This function should do the following:
#     1. Prompt the user to enter the name of a color.
#     2. Using case statements, if it matches the color that they picked, it should print out a success message like so:
#           "Success! You picked red."
#        Do NOT use f-strings here. Just use regular strings and use the case statement to pick which string to print.
#     3. You should have a case for at least 5 colors of your choosing.
#     3. If the user picks a color that you do not have a case for, it should print:
#           "Unknown Color!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def color_picker(): 
    color = input("What is the name of the color you want to pick? (ps. they might be very specific colors involving pink, purple, sparkly pink, and rainbows) : ")
    print("")
    match color:
        case "pink":
            print("You picked the best color!")
        case "purple":
            print("You picked the second best color!")
        case "sparkly pink":
            print("You picked the best color thats even better cause sparkles!")
        case "rainbow":
            print("You picked every color which makes you the best!")
        case _:
            print("Unknown Color! But good try though!")

color_picker()


    
###############################################################################
# DONE: 2. (3 pts)
#
#   Write a function called grade() that tells a student what letter grade they
#   got on an assignment based on the percentage they indicate.
#
#   This function should do the following:
#     1. Prompt the user to enter a percentage. They should enter the
#        percentage as a decimal (so an 85% should be entered as 0.85)
#     2. Using case statements, check which range the percentage is in and print a statement telling the user what grade they got on the assignment. It should look something like:
#           "You received a(n) A."
#     3. Your ranges should match a standard grading scale where greater than or equal to 90% is an A, etc.
#     4. If the user enters an invalid percentage, the function should print:
#           "Invalid Score!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def grade():
    grade = float(input("What is your grade percentage? Make sure you enter your grade as a decimal : "))
    print("")
    if .9 <= grade <= 1.0:
        print("You should have recieved an A! Good Job")
    elif .8 <= grade < .9:
        print("You should have recieved a B. OK job.")
    elif .7 <= grade < .8:
        print("You should have recieved a C... Do better.")
    elif .6 <= grade < .7:
        print("You managed to get a D. Thats just sad.")
    elif .0 <= grade < .6:
        print("You FAILED! HOW COULD YOU")
    else:
        print("Invalid score! You either lied, got extra credit, or did not read instructions.")

grade()

