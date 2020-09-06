"""
Create function create with one string argument.
This function should return anonymous function that checks
 if the argument of function is equals to the argument of outer function.

For example:

 tom = create("pass_for_Tom")

 tom("pass_for_Tom") returns true

 tom("pass_for_tom") returns false
"""


def create(text):
    return lambda text1: text == text1
    # return lambda text1: True if (text == text1) else False # ошибка джунов



print(firstValue("secret"))

print(firstValue("SECRET"))

print(secondValue("SecreT"))

print(list(get_names(create)))
user2 = create("___")
print(user2("__"))