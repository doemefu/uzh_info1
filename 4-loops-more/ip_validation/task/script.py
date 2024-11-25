#!/usr/bin/env python3

def is_valid_IPv4_octet(octet):
    """Returns True if octet represents a valid IPv4 octet, False otherwise"""
    if len(octet) == 0:
        return False

    if not octet.isdigit():
        return False

    if len(octet) > 1 and octet[0] == '0':
        return False

    return 0 <= int(octet) <= 255


def is_valid_IPv4(ip):
    """Returns True if ip represents a valid IPv4 address, False otherwise"""
    ip = str(ip)

    if len(ip) == 0:
        return False

    pos1 = ip.find(".")
    pos2 = ip.find(".", pos1 + 1)
    pos3 = ip.find(".", pos2 + 1)
    pos4 = ip.find(".", pos3 + 1)

    if pos1 == -1 or pos2 == -1 or pos3 == -1 or pos4 != -1:
        return False

    if pos2 - pos1 <= 1 or pos3 - pos2 <= 1:
        return False

    return is_valid_IPv4_octet(ip[0:pos1]) and is_valid_IPv4_octet(ip[pos1 + 1:pos2]) and is_valid_IPv4_octet(
        ip[pos2 + 1:pos3]) and is_valid_IPv4_octet(ip[pos3 + 1:len(ip)])


def is_valid_IPv6_hextet(hextet):
    """Returns True if hextet represents a valid IPv6 hextet, False otherwise"""
    hextet = str(hextet)

    if len(hextet) == 0 or len(hextet) > 4:
        return False

    for a in hextet:
        if a not in "abcdefABCDEF1234567890":
            return False

    return True


def is_valid_IPv6(ip):
    """Returns True if ip represents a valid IPv6 address, False otherwise"""
    if len(ip) == 0:
        return False

    pos1 = ip.find(":")
    pos2 = ip.find(":", pos1 + 1)
    pos3 = ip.find(":", pos2 + 1)
    pos4 = ip.find(":", pos3 + 1)
    pos5 = ip.find(":", pos4 + 1)
    pos6 = ip.find(":", pos5 + 1)
    pos7 = ip.find(":", pos6 + 1)
    pos8 = ip.find(":", pos7 + 1)

    if pos1 == -1 or pos2 == -1 or pos3 == -1 or pos4 == -1 or pos5 == -1 or pos6 == -1 or pos7 == -1 or pos8 != -1:
        return False

    if pos2 - pos1 <= 1 or pos3 - pos2 <= 1 or pos4 - pos3 <= 1 or pos5 - pos4 <= 1 or pos6 - pos5 <= 1 or pos7 - pos6 <= 1:
        return False

    return is_valid_IPv6_hextet(ip[0:pos1]) and is_valid_IPv6_hextet(ip[pos1 + 1:pos2]) and is_valid_IPv6_hextet(
        ip[pos2 + 1:pos3]) and is_valid_IPv6_hextet(ip[pos3 + 1:pos4]) and is_valid_IPv6_hextet(
        ip[pos4 + 1:pos5]) and is_valid_IPv6_hextet(ip[pos5 + 1:pos6]) and is_valid_IPv6_hextet(
        ip[pos6 + 1:pos7]) and is_valid_IPv6_hextet(ip[pos7 + 1:len(ip)])


def is_valid_IP(ip):
    """Returns True if ip represents a valid IPv4 or IPv6 address False otherwise"""
    if ":" in ip:
        return is_valid_IPv6(ip)
    elif "." in ip:
        return is_valid_IPv4(ip)
    else:
        return False


# You should look at task/test.py and extend the test suite we provided!

print(is_valid_IPv4_octet("a"))