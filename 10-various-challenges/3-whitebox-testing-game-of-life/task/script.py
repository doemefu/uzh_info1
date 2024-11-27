#!/usr/bin/env python3

def evolve(world, steps):
    check_field_formal(world)
    check_field_inside(world)
    if type(steps) != int or steps < 1:
        raise Warning("Choose at least one step")

    new_field = populate_new_field(world, steps)

    return new_field, count_cells(new_field) # placeholder

def populate_new_field(old_field, pnf_steps):

    for q in range(pnf_steps):
        tmp_field = [old_field[0]]

        for x in range(1,len(old_field)-1):
            tmp_str = "|"
            for y in range(1,len(old_field[x])-1):
                n = get_neighbours(x, y, old_field)
                if old_field[x][y] == "#" and n <= 1:
                    tmp_str += " "
                elif old_field[x][y] == "#" and n >= 4:
                    tmp_str += " "
                elif old_field[x][y] == "#":
                    tmp_str += "#"
                elif old_field[x][y] == " " and n == 3:
                    tmp_str += "#"
                else:
                    tmp_str += " "

            tmp_str += "|"
            #print(tmp_str)
            tmp_field.append(tmp_str)
            #print(tmp_field)
        tmp_field.append(old_field[-1])

        old_field = tmp_field

        for row in old_field:
            print(row)

        print("xxxxxxxxxxxxxxxxxxx")

    return tuple(old_field)

def check_field_formal(cff_field):
    if type(cff_field) != tuple:
        raise Warning("Field isn't a tuple")

    if len(cff_field) < 3 or len(cff_field[0]) < 3:
        raise Warning("Field to little")

    field_len = len(cff_field[0])
    for line in cff_field:
        if type(line) != str:
            raise Warning("Field doesn't consist of strings")
        if len(line) != field_len:
            raise Warning("Field width inconsistent")

def check_field_inside(cfi_field):
    for char in cfi_field[0]:
        if char != "-":
            raise Warning("Upper border is wrong")
    for char in cfi_field[-1]:
        if char != "-":
            raise Warning("Lower border is wrong")

    for n in range(1,len(cfi_field)-1):
        if cfi_field[n][0] != "|":
            raise Warning("Left border is wrong")
        if cfi_field[n][-1] != "|":
            raise Warning("Right border is wrong")

        for q in range(1,len(cfi_field[n])-1):
            if cfi_field[n][q] not in " #":
                raise Warning(f"Bad field content: {cfi_field[n][q]}")

def get_neighbours(x,y,gn_field):
    gn_sum = 0

    for xx in range(-1,2):
        for yy in range (-1,2):
            if gn_field[x+xx][y+yy] == "#":
                gn_sum += 1

    if gn_field[x][y] == "#":
        gn_sum -= 1

    return gn_sum

def count_cells(cc_field):
    cc_sum = 0

    for line in cc_field:
        for char in line:
            if char == "#":
                cc_sum += 1

    return cc_sum

field = (
    "--------------",
    "|            |",
    "|            |",
    "|   ##       |",
    "|   #        |",
    "|            |",
    "--------------"
)
steps = 4

result, alive_cells = evolve(field, steps)

print(f"Game of Life after {steps} moves:")
for row in result:
    print(row)
print(f"{alive_cells} are alive.")