"""
Create function create_account(user_name: string, password: string, secret_words: list).
This function should return inner function check.

The function check compares the values of its arguments with password and secret_words:
 the password must match completely, secret_words may be misspelled (just one element).

Password should contain at least 6 symbols including one uppercase letter, one lowercase letter,
 special character and one number.

Otherwise function create_account raises ValueError.



For example:

tom = create_account("Tom", "Qwerty1", ["1", "word"]) raises Value error



If tom = create_account("Tom", "Qwerty1_", ["1", "word"])

then

tom("Qwerty1_",  ["1", "word"]) return True

tom("Qwerty1_",  ["word"]) return False due to different length of   ["1", "word"] and  ["word"]

tom("Qwerty1_",  ["word", "12"]) return True

tom("Qwerty1!",  ["word", "1"]) return False because "Qwerty1!" not equals to "Qwerty1_"
"""
import re


def create_account(user_name, password, secret_words):
    tempDict = {'up': 0, 'low': 0, 'dig': 0, 'spec': 0}
    tempDict['up'] = len(re.findall(r'[A-Z]', password)) != 0
    tempDict['low'] = len(re.findall(r'[a-z]', password)) != 0
    tempDict['dig'] = len(re.findall(r'\d{1}', password)) != 0
    tempDict['spec'] = len(re.findall(r'[|!|@|#|$|%|^|&|*|(|)|_|+|=]', password)) != 0
    for key in tempDict:
        if not tempDict[key]:
            raise ValueError

    def check(own_password, checklist):
        if own_password == password and len(checklist) == len(secret_words):
            temp = [] + secret_words
            for item in checklist:
                if item in temp:
                    temp.pop(temp.index(item))
            return len(temp) <= 1
        else:
            return False

    return check


tom = create_account("Tom", "Qwerty1_", ["1", "word"])
check1 = tom("Qwerty1_", ["1", "word"])
check2 = tom("Qwerty1_", ["word"])
check3 = tom("Qwerty1_", ["word", "2"])
check4 = tom("Qwerty1!", ["word", "12"])

print(check1,check2,check3,check4)
