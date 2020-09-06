"""
Write  the function check_day_week(day) whose input parameter is a number. The function returns the
corresponding day of the week if the input parameter is in the range of 1 to 7, namely

· in the case when the input parameter is 5 the function should be displayed the message – "Friday"
· in the case when the input parameter is not in the range of 1 to 7 the function should be displayed the message – "There is no such day of the week!Please try again."
· in the case of incorrect data the function should be displayed the message - "You did not enter a number!Please try again."

Note: in the function you must use the "try except" construct.



Function example:

check_day_week(2)                       # output:   "Tuesday"

check_day_week(11)                     # output:  "There is no such day of the week!Please try again."

check_day_week("Monday")       # output:   "You did not enter a number!Please try again."
"""


def check_day_week(day):
    data = {'1': "Monday", '2': "Tuesday", '3': 'Wednesday', '4': 'Thursday', '5': "Friday", '6': 'Saturday',
            '7': 'Sunday'}
    str_day = str(day)
    try:
        if type(day) is not int:
            raise ValueError("You did not enter a number!Please try again.")
        elif str_day in data:
            print(data.get(str_day))
        elif str_day not in data:
            raise IndexError("There is no such day of the week!Please try again.")


    except IndexError as ie:
        print(ie)
    except ValueError as ve:
        print(ve)


check_day_week(5)
check_day_week(1)
check_day_week(-1)
check_day_week("Monday")
