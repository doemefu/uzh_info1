#!/usr/bin/env python3

def is_valid_IP(ip):
    return is_valid_IPv6(ip) or is_valid_IPv4(ip)

def is_valid_IPv4(ip):
    octets = ip.split(".")
    return (len(octets) == 4 and
            sum([is_valid_IPv4_octet(octet) for octet in octets]) == 4)

def is_valid_IPv6(ip):
    hextets = ip.split(":")
    return (len(hextets) == 8 and
            sum([is_valid_IPv6_hextet(hextet) for hextet in hextets]) == 8)

# Here are three different solutions for both of the remaining methods.

# Solution 1 uses only concepts already discussed in the lecture. It checks
# multiple conditions to prevent crashing on invalid input.
# Note that the backslash (\) allows starting a new line without a SyntaxError
def is_valid_IPv4_octet(octet):
    return 1 <= len(octet) <= 3 and \
           sum([1 for char in octet if char.isdigit()]) == len(octet) and \
           0 <= int(octet) <= 255

def is_valid_IPv6_hextet(hextet):
    valid_chars = "0123456789abcdef"
    return 1 <= len(hextet) <= 4 and \
           sum([1 for char in hextet if char.lower() in valid_chars]) == len(hextet) and \
           0 <= int(hextet, 16) < int("ffff", 16)

# Solution 2 uses all() instead of sum()
def is_valid_IPv4_octet(octet):
    return 1 <= len(octet) <= 3 and \
           all([True for char in octet if char.isdigit()]) and \
           0 <= int(octet) <= 255

def is_valid_IPv6_hextet(hextet):
    valid_chars = "0123456789abcdef"
    return 1 <= len(hextet) <= 4 and \
           all([True for char in hextet if char.lower() in valid_chars]) and \
           0 <= int(hextet, 16) < int("ffff", 16)


# Solution 3 uses try/except when invalid values are encountered rather than
# preventing any errors by doing all the checking like in solution 1.
# This approach is short, robust, and readable: It will deal with any potential
# breakage by (correctly) returning False. The downside is that this could hide
# problems, making the whole program harder to debug.
def is_valid_IPv4_octet(octet):
    try:
        return 0 <= int(octet) <= 255
    except:
        return False

def is_valid_IPv6_hextet(hextet):
    try:
        return 0 <= int(hextet, 16) < int("ffff", 16)
    except:
        return False

# Solution 4 uses regex (you could also apply this to the other functions above)
import re
def is_valid_IPv4_octet(octet):
    pattern = r'^(?:[0-9]|1[0-9]{1,2}|2[0-4][0-9]|25[0-5])$'
    return bool(re.match(pattern, octet))

def is_valid_IPv6_hextet(hextet):
    pattern = r'^(0x)?([0-9a-fA-F]{1,4})$'
    return bool(re.match(pattern, hextet))

# Solution 5 is as conventional as possible but lacks succinctness and clarity.
def is_valid_IPv4_octet(octet):
    if not 1 <= len(octet) <= 3:
        return False
    for char in octet:
        if not char.isdigit():
            return False
    return 0 <= int(octet) <= 255

def is_valid_IPv6_hextet(hextet):
    valid_chars = "0123456789abcdef"
    if not 1 <= len(hextet) <= 4:
        return False
    for char in hextet:
        if char not in valid_chars:
            return False
    return 0 <= int(hextet, 16) < int("ffff", 16)

