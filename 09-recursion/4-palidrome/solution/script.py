#!/usr/bin/env python3
import re


# Change the functions below to determine if the given input is a palindrome.

def is_palindrome(s):
    # Clean the string by removing non-alphanumeric characters and converting to lowercase
    s = re.sub(r"[^A-Za-z0-9]", "", s).lower()

    # Base case: if the length of the string is 0 or 1, it's a palindrome
    if len(s) <= 1:
        return True
    # Recursive case: if the first and last characters match, call is_palindrome on the middle part
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    # Non-palindrome case: first and last characters don't match
    else:
        return False


# The following lines call the function and prints the return
# value to the Console. This way you can check what it does.
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("No lemon, no melon"))
print(is_palindrome("This is not a palindrome"))
