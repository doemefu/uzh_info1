#!/usr/bin/env python3


# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def hamming_dist(signal_1, signal_2):
    if len(signal_1["data"]) != len(signal_2) or len(signal_2) == 0:
        return "Empty signal on at least one of the sensors"

    returnList = []

    for a in range(0,len(signal_2)):
        value1 = signal_1["data"][a]
        value2 = signal_2[a]
        if len(value1) != len(value2):
            return("Sensor defect detected")
        elif value1 != value2:
            c = 0
            for b in range(0,len(value1)):
                if value1[b] != value2[b]:
                    c += 1
            returnList.append((value1, value2, c))

    return returnList




# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
print(hamming_dist(signal_sensor_1, signal_sensor_2))
