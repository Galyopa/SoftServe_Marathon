""""Given a string, check if its characters can be rearranged to form a palindrome. Where a palindrome is a string that reads the same left-to-right and right-to-left.

Example

"trueistrue" -> false;
"abcab" -> true because "abcba" is a palindrome
[input] string s (min 1 letters)

[output] boolean"""


def isPalindrome(str):
    result = {}
    for i in str:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    odd_count = 0

    for item in result:
        if result[item] % 2 != 0:
            odd_count += 1

    return True if odd_count <= 1 else False


print(isPalindrome("abb"))
# True
print(isPalindrome("23332"))
# True
print(isPalindrome("trueitrue"))
# True
print(isPalindrome("trueistrue"))
# False
print(isPalindrome("123123"))
# True
print(isPalindrome("12312"))
# True
print(isPalindrome("qqqrrr"))
# False
print(isPalindrome("qqqrrrwww"))
# False
print(isPalindrome("A"))
# True
