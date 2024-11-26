#!/usr/bin/env python3

import os


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        return False

    with open(path_reading, "r") as fi:
        with open(path_writing, "w") as fo:

            try:
                next(fi)
            except StopIteration:
                return

            content = fi.read()
            fo.write("Firstname,Lastname")

            for line in content.splitlines():
                fo.write("\n")

                if line.find(";") != -1 and len(line)>=4:
                    name=line.split("; ")
                    temp_str = name[1] + "," + name[0]
                    fo.write(temp_str)

                elif line.find(" ") != -1 and len(line)>=3:
                    name=line.split(" ")
                    temp_str = name[0] + "," + name[1]
                    fo.write(temp_str)

                else:
                    fo.write(",")

    # the rest of your implementation


# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "./my_data.txt"
OUTPUT_PATH = "./my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")

