#!/usr/bin/env python3
# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def move(state, direction):
    #print("\n".join(state))

    old_player_pos = checker(state, direction)
    #print("------old_player_pos-------")
    #print(old_player_pos)

    old_poss_moves = get_possible_directions(state,old_player_pos)
    #print("------old_poss_moves-------")
    #print(old_poss_moves)

    if direction not in old_poss_moves:
        raise Warning("Movement not possible")

    #pos = get_position(state) #list #not used as implemented in checker
    new_player_pos = calc_pos(old_player_pos, direction) #list
    #print("------new_player_pos-------")
    #print(new_player_pos)

    new_field = create_new_field(state,new_player_pos) #list(string)
    #print("------new_field-------")
    #print(new_field)

    new_poss_moves = get_possible_directions(new_field, new_player_pos) #list
    #print("------new_poss_moves-------")
    #print(new_poss_moves)

    return tuple(new_field), tuple(new_poss_moves)

def get_possible_directions(gpd_field, gpd_player_pos):
    gpd_pos = []
    if gpd_player_pos[0] != len(gpd_field)-1 and gpd_field[gpd_player_pos[0]+1][gpd_player_pos[1]] == " ":
        gpd_pos.append("down")

    if gpd_player_pos[1] != 0 and gpd_field[gpd_player_pos[0]][gpd_player_pos[1]-1] == " ":
        gpd_pos.append("left")

    if gpd_player_pos[1] != len(gpd_field[0])-1 and gpd_field[gpd_player_pos[0]][gpd_player_pos[1]+1] == " ":
        gpd_pos.append("right")

    if gpd_player_pos[0] != 0 and gpd_field[gpd_player_pos[0]-1][gpd_player_pos[1]] == " ":
        gpd_pos.append("up")

    return gpd_pos

def calc_pos(cp_pos, cp_direction):
    match cp_direction:
        case "down":
            cp_pos[0] += 1   #[2,3]
        case "left":
            cp_pos[1] -= 1
        case "right":
            cp_pos[1] += 1
        case "up":
            cp_pos[0] -= 1

    return cp_pos

def create_new_field(cnf_state, cnf_player_pos):
    cnf_field = []
    z = 0
    for element in cnf_state:
        zeile = ""
        s = 0
        for item in element:
            if item == "o":
                zeile += " "
            elif z == cnf_player_pos[0] and s == cnf_player_pos[1]:
                zeile += "o"
            else:
                zeile += item
            s += 1
        z += 1
        cnf_field.append(zeile)

    return cnf_field

def get_position(gp_state):
        z = 0
        for element in gp_state[1]:
            s = 0
            for item in element:
                if item == "o":
                    return [z,s]
                s += 1
            z += 1

        raise Warning("This shouldn't happen")

def checker(chk_state, chk_direction):
    if len(chk_state) <= 0 or len(chk_state[0]) <= 0:
        raise Warning("Field size not sensible")

    length = len(chk_state[0])
    player = [-1,-1]
    z=0
    for element in chk_state:
        s=0
        for item in element:
            if item not in " #o":
                raise Warning(f"invalid character: {item}")
            if item == "o":
                if player == [-1,-1]:
                    player = [z,s]
                else:
                    raise Warning("Too many players on the filed!")
            s +=1
        z += 1
        if len(element) != length:
            raise Warning("Field length inconsistent")

    if player == [-1,-1]:
        raise Warning("No Player on Field")

    return player


# The following line calls the function and prints the return
# value to the Console.
s1 = (
    "#####   ",
    "###    #",
    "#   o ##",
    "   #####"
)
#s2 = move(s1, "right")

#print("= New State =")
#print("\n".join(s2[0]))
#print(f"\nPossible Moves: {s2[1]}")
