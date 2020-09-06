"""As input data, you have a list of strings.

Write a method double_string() for counting the number of strings from the list,
represented in the form of the concatenation of two strings from this list"""


def double_string(data):
    count = 0
    for i in range(len(data) - 1):
        if data[i]*2 == data[i + 1]:
            count += 1

    return count




data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
print(double_string(data))

data = ['aa', 'abc', 'qwerqwer']
print(double_string(data))