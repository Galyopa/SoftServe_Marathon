"""" As input data, you have a string that consists of words that have duplicated characters at the end of it.

All duplications may be in the next format:

wordxxxx
wordxyxyxy
wordxyzxyzxyz
, where x, xy or xyz repeated ending of the word

Using re module write function pretty_message() that remove all duplications
"""

import re


def pretty_message(data):
    pattern = r'([a-z])\1{2,}|(..)\2+|(...)\3+\b'
    result = re.sub(pattern, r'\1\2\3', data)
    return result


# def pretty_message(data):
#     ace = re.sub(r'(ace)+?\b', r'ace', data)
#     s = re.sub(r'[s]+?\b', r's', ace)
#     i_s = re.sub(r'(is)+?\b', r'is', s)
#     o = re.sub(r'[o]+?\b', r'o', i_s)
#     g = re.sub(r'[g]+?\b', r'g', o)
#     ed = re.sub(r'(ed)+?\b', r'ed', g)
#
#     return ed


data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
print(pretty_message(data))
