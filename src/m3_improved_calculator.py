def addition(num1, num2):
    result= num1 + num2
    return result

def subtraction(num1, num2):
    result= num1 - num2
    return result

def multiplication(num1, num2):
    result= num1 * num2
    return result
    
def division(num1, num2):
    result= num1 / num2
    return result

def remainder(num1, num2):
    import math
    result= math.remainder(num1,num2)
    return result

###############################################################################
# DONE: 1. (4 pts)
#
#   In this module, we will improve upon the calculator that we built in the
#   Session 5 coding exercises.
#
#   First, you will need to grab the functions that you wrote for each of the
#   four main operations:
#     - add
#     - subtract
#     - multiply
#     - divide
#
#   You can simply copy and paste them into this file at the top (above this
#   _TODO_)
#
#   For this _TODO_, we will be rewriting our main() function.
#
#   First, copy your main() function from Session 5 m3 todo #2 and rename it
#   to if_calc().
#
#   Next, make these modifications
#     1. Add another prompt for the user asking which operation they want to
#        do. Make sure to show the user this key in the prompt.
#           (+) Add
#           (-) Subtract
#           (*) Multiply
#           (/) Division
#
#        The user should then enter one of the operators to indicate which
#        operation they want to do. Make sure you save this to a variable.
#
#     2. Now, using if statements, check which operator the user put and only
#        do the calculation that the user specified instead of all of them. If
#        the user, put something other than one of the operators, print:
#           "Invalid Operation!"
#
#   Your solution should still function just like it did in Session 5 (except
#   for the changes outlined above)   
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def if_calc():
    num1= float(input("Hello! I'm ur new calculator! What is your first number?: " ))
    num2= float(input("What is your second number?: " ))
    operation = input("What order of operation would you like to do? addition, subtraction, multiplication, division, or remainder: ")
    if operation == "addition":
        print("You chose addition, and your answer is", addition(num1, num2))
    elif operation == "subtraction":
        print("You chose subraction, and your answer is", subtraction(num1, num2))
    elif operation == "multiplication":
        print("You chose multiplication and your answer is", multiplication(num1, num2))
    elif operation == "division":
        print("You chose division and your answer is", division(num1, num2))
    elif operation == "remainder":
        print("You chose to find the remainder and your answer is", remainder(num1,num2))
    else:
        print("Invalid Operation")
    print("Thank you for using me today!")

if_calc()
###############################################################################
# DONE: 2. (4 pts)
#
#   Now, do the same thing that you did in _TODO_ 1, but this time, use case
#   statements in your solution instead of if statements.
#
#   This time rename your function to case_calc(). Also, you do *not* need to
#   re-copy your operation functions. You can simply use them again.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def case_calc():
    num1= float(input("Hello! I'm ur new calculator! What is your first number?: " ))
    num2= float(input("What is your second number?: " ))
    operation = input("What order of operation would you like to do? addition, subtraction, multiplication, division, or remainder: ")
    match operation:
        case "addition":
            print("You chose addition, and your answer is", addition(num1, num2))
        case "subtraction":
            print("You chose subraction, and your answer is", subtraction(num1, num2))
        case "multiplication":
            print("You chose multiplication and your answer is", multiplication(num1, num2))
        case "division":
            print("You chose division and your answer is", division(num1, num2))
        case "remainder":
            print("You chose to find the remainder and your answer is", remainder(num1,num2))
        case _:
            print("Invalid Operation")
    print("Thank you for using me today!")

case_calc()
