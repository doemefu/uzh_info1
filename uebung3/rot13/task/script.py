#!/usr/bin/env python3

# perform a ROTn encoding
def rot_n(plain_text, shift_by):
    textList = list(plain_text)
    newString = ""

    for myChar in textList:

        temp = ord(myChar)+shift_by

        if 65 <= ord(myChar) <= 90:
            newString += chr((temp-65) % 26 + 65)
        elif 97 <= ord(myChar) <= 122:
            newString += chr((temp-97) % 26 + 97)
        else:
            newString += myChar

    return newString

print(rot_n("abz", 190))

