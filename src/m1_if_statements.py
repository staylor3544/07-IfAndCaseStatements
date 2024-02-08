txt = "The quick brown fox jumps over the lazy dog."

###############################################################################
# DONE: 1. (2 pts)
#
#   Write a function called is_positive() that takes one parameter:
#     - number (float)
#   that returns True if the number given is either 0 or positive and returns
#   False if the number given is negative.
#
#   Your solution should use an if statement and should return the actual
#   values True or False (not just strings that say "True" or "False")
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def is_positive(float):
    if float >= 0:
        return True
    elif float < 0:
        return False
    
###############################################################################
# DONE: 2. (2 pts)
#
#   Write a function called contains() that takes two parameters:
#     - str (string)
#     - substr (string)
#   and checks if the substring *substr* is contained within the string *str*
#
#   The function should return the value True if the substring is within the
#   string and False if it is not within the string.
#
#   You should use an if statement in your solution.
#
#   You can test your function by calling it using the string I have provided
#   at the top of this file or by creating your own strings to use.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def contains(substr):
    if substr in txt:
        return True
    if substr not in txt:
        return False
    
print(contains("lazy dog"))
###############################################################################
# DONE: 3. (3 pts)
#
#   Write a function called display_rating() that takes one parameter:
#     - rating (float)
#   that displays a short description for each rating that one might get on a
#   review for something like a product or a service.
#
#   For example, if the function gets a 4.8 it should print something like:
#
#       "Contratulations! You received a score of 4.8!"
#
#   or if it gets a rating of 1.2 it would print something like:
#
#       "You could use some improvement. You received a score of 1.2."
#
#   You should have a different message for each of these ranges of ratings:
#     - less than or equal to 5 and greater than or equal to 4
#     - less than 4 and greater than or equal to 3
#     - less than 3 and greater than or equal to 2
#     - less than 2 and greater than or equal to 1
#
#   If it receives anything outside those ranges, it should print:
#
#       "Invalid score given."
#
#   You can test this function by calling it with various ratings.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def display_rating(float):
    if float <= 5 and float >= 4:
        return "WOW you are an amazing sparkly princess!"
    elif float < 4 and float >= 3:
        return "You are a slightly ok sparkly princess."
    elif float < 3 and float >= 2:
        return "Um... you are quite a bad princess. You dont deserve sparkles."
    elif float < 2 and float >= 1:
        return "You need to reevaluate you life and aspirations to be a sparkly princess. Never show your face here again."
    else:
        return "Invalid score given."
    
print(display_rating(2.8))
    

    