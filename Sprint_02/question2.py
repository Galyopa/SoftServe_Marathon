# def morse_number(digits):
#     s = ""
#     for d in digits:
#         if d == "0":
#             s = s +  "-----"+ " "
#         if d == "1":
#             s = s +  ".----"+ " "
#         if d == "2":
#             s = s  +  "..---"+ " "
#         if d == "3":
#             s = s  +  "...--"+ " "
#         if d == "4":
#             s = s  +  "....-"+ " "
#         if d == "5":
#             s = s  + "....."+ " "
#         if d == "7":
#             s = s  + "--..."+ " "
#         if d == "8":
#             s = s  + "---.."+ " "
#         if d == "9":
#             s = s + "----." + " "
#
#     return s

def morse_number(number):
    morse_code = ''
    for key in number:
        morse_char = ''
        for x in range(5):
            if int(key) - 5 <= 0:
                if x < int(key):
                    morse_char += '.'
                else:
                    morse_char += '_'
            else:
                if x < int(key) - 5:
                    morse_char += '_'
                else:
                    morse_char += '.'
        morse_code += ''.join([morse_char, ' '])
    return morse_code


print(morse_number("295"))

print(morse_number("005"))

print(morse_number("513"))

print(morse_number("784"))

morse = {
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}
