"""
Write  the function check_positive(number) whose input parameter is a number.
The function checks whether the  set number is positive or negative:

in the case of a positive number the function should be displayed the corresponding message
- " You input positive number: input parameter of function";
in the case of a negative parameter the function should
be raised the exception of your own class MyError and displayed the corresponding message
 - "You input negative number: input parameter of function. Try again.";
in the case of incorrect data the function should be displayed the message - "Error type: ValueError!"
Function example:

check_positive (24)      #output:    "You input positive number: 24"

check_positive (-19)     #output:     "You input negative number: -19. Try again."

check_positive ("38")    #output:    "You input positive number: 38"

check_positive ("abc")  #output:     "Error type: ValueError!"
"""


class MyError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def check_positive(number):
    try:
        if type(int(number)) is not int:
            raise MyError("Error type: ValueError!")
        if float(number) > 0:
            print(f"You input positive number: {float(number)}")
        if float(number) < 0:
            print(f"You input negative number: {float(number)}. Try again.")
    except MyError as me:
        print(me)
    except ValueError:
        print("Error type: ValueError!")


check_positive(8.9)

check_positive(-19)

check_positive(0.7)

check_positive(-0.6)

check_positive("abs")

check_positive("45")

check_positive("-235")
