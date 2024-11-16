In this exercise you will write a program that validates IPv4 & IPv6 addresses.

## What is an IP Address?

An [IP address](https://en.wikipedia.org/wiki/IP_address) is a unique string of characters that identifies a computing device using the Internet Protocol (IP) to communicate over a network. Your PC, your phone, your tablet, even your smart thermostat have at least one IP. There are two types of IP addresses: IP version 4 (IPv4) and IP version 6 (IPv6). IPv4 provides an addressing capacity of 4.3 billion addresses while IPv6 provides an addressing capacity of 340 undecillion addresses. IPv4 is the most commonly used IP address. The world is in the (slow) process of transitioning from IPv4 to IPv6.


### IPv4 Format
An IPv4 address is a string in the form `a.b.c.d` where `a`, `b`, `c`, and `d` are integers ("octets") between 0 and 255. For example, `127.0.0.1` is a valid IP address, but `300.0.0.1` is not and `123` is a valid octet but `hello` is not. The IPv4 address is split into four octets by three `.` (dots).


### IPv6 Format

 An IPv6 address is a string in the form `a:b:c:d:e:f:g:h` where `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h` are hexadecimal numbers ("hextets") between 0 and FFFF. For example, `2001:0db8:85a3:0:0000:8a2e:0370:7334` is a valid IP address, but `2001:0db8:85a3:0:0000:8a2e:0370:7334:1234` is not (because it has one too many hextets) and `ff3` is a valid hextet, but `hello!!!` is not. The IPv6 address is split into eight hextets by seven `:` (colons). Note that for this task, you can assume that IPv6 addresses always contain all eight hextets (ignoring the official specification, which allows trailing 0000 to be omitted). On the other hand, you must assume that individual hextets could be shorter than four characters (e.g.: 'FFF' is a valid hextet equivalent to '0FFF', just like `7` is a valid IPv4 octet equivalent to `007`). Character casing should also be ignored.

## Task

You will need to implement the five functions provided as templates in `task/script.py`. Notice how the functions are forming a hierarchy, for exmaple `is_valid_IPv4_octet` validates just an octet (`151`), `is_valid_IPv4` validates an entire IPv4 address (`192.151.1.1`) and `is_valid`IP` validates both IPv4 and IPv6 addresses. This means that the top-level function `is_valid_IP` should call the IP-version-sepcific validation functions, and that those functions should call the octet/hextet validation functions as needed. There is no need to duplicate code.

 1. Implement the lowest-level functions (validating octets/hextets) first
 2. Implement the IPv4 and IPv6 validation functions (where you call the octet/hextet validation functions for each octet/hextet)
 3. Implement the general IP validation function, which just tries both IPv4 and IPv6 validation functions on the input.

## Testing
Rather than messing with a multitude of print statements, you are encouraged to inspect `task/tests.py` and extend the test suite for all possible valid and invalid inputs. Read the comment in `task/tests.py` carefully and fill in the gaps. This will make your life much easier when implementing a solution.

## Hints

- `is_valid_IP` should call the two functions `is_valid_IPv4` and `is_valid_IPv6` to allow IPs of both versions to be validated. Those two functions in turn will have to split the input string into hextets or octets and call `is_valid_IPv4_octet` or `is_valid_IPv6_hextet` respectively for each substring. This forms a function call chain.
- The two functions `is_valid_IPv4` and `is_valid_IPv6` should independently check *all* necessary constraints to determine if the given string is a valid IP of the respective version. The purpose of `is_valid_IP` is to simply allow both valid IPv4 and IPv6 addresses to be validated without the version constraint.
- Each of these functions returns a boolean.
- To split a string, use the [split](https://docs.python.org/3/library/stdtypes.html#str.split) function.
- You can convert strings to integers using the [int](https://docs.python.org/3/library/functions.html#int) function. You might need this to check if the hextets/octets are in the correct range.
- To convert strings to hexadecimal numbers, you can also use the [int](https://docs.python.org/3/library/functions.html#int) function with an additional parameter that specifies the base. For example, the following code will convert the string "fe80" to the hexadecimal number 65152: `int("fe80", 16)`
- There is more than one solution. For example, you could use [Python's Regular Expression library](https://docs.python.org/3/library/re.html) to validate strings: [re], or you could convert the strings to decimal (e.g.: `int("127")`) and hexadcemial (e.g.: `int("fe",16)`) and then compare numbers to ensure the given ones are in the valid range.

