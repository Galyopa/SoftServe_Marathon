"""
Write  the function check_odd_even (number) whose input parameter is an integer number.
The function checks whether the  set number is even or odd:

in the case of an even number the function should be displayed the corresponding message - "Entered number is even";
in the case of an odd number the function should be displayed the corresponding message -  "Entered number is odd";
in the case of incorrect data the function should be displayed the message - "You entered incorrect data. Please try again."
Note: in the function you must use the "try except" construct.
"""


def check_odd_even(number):
    try:
        if type(number) is not int:
            raise ValueError("You entered incorrect data. Please try again.")
        elif number % 2 == 0:
            print("Entered number is even")
        else:
            print("Entered number is odd")
    except ValueError as ev:
        print(ev)


check_odd_even(15)

check_odd_even(-6)

check_odd_even(0)

check_odd_even("plp")

check_odd_even(36)


def sum_two_smallest_numbers(numbers):
    print(sum(sorted(numbers)[:2]))


sum_two_smallest_numbers([5, 8, 12, 18, 22])
# sum_two_smallest_numbers([7, 15, 12, 18, 22])
# sum_two_smallest_numbers([25, 42, 12, 18, 22])
