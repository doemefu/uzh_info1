#!/usr/bin/env python3
import re


# Change the functions below to determine if the given input is a palindrome.

def is_palindrome(s):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    if len(cleaned) == 2 or len(cleaned) == 3:
        if cleaned[0] == cleaned[len(cleaned)-1]:
            return True
        else:
            return False
    else:
        return is_palindrome(cleaned[1:len(cleaned)-1])


# The following lines call the function and prints the return
# value to the Console. This way you can check what it does.
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("No lemon, no melon"))
print(is_palindrome("This is not a palindrome"))
