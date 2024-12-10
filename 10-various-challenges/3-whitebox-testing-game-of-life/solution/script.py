#!/usr/bin/env python3

def validate(world, steps):
    """Performs all necessary validation"""
    # ensure world is a tuple of strings
    if not isinstance(world, tuple):
        raise Warning("world must be a tuple")
    for row in world:
        if not isinstance(row, str):
            raise Warning("all elements in world must be strings")
    # ensure world rows are all the same length
    row_lengths = set([len(row) for row in world])
    if len(row_lengths) != 1:
        raise Warning("all rows in the world must have the same length")
    # ensure world has sensible size
    if list(row_lengths)[0] < 3 or len(world) < 3:
        raise Warning("world dimensions including frame must be at least 3x3")
    # ensure world only contains allowed characters
    for char in world[0]:
        if char != '-':
            raise Warning("first world line must only contain '-'")
    for char in world[-1]:
        if char != '-':
            raise Warning("last world line must only contain '-'")
    for row in world[1:-1]:
        if row[0] != '|':
            raise Warning("first character of rows 1 to -1 must be '|'")
        if row[-1] != '|':
            raise Warning("last character of rows 1 to -1 must be '|'")
    cells = [line[1:-1] for line in world[1:-1]]
    for row in cells:
        for char in row:
            if char not in [" ", "#"]:
                raise Warning("game cells within the frame may only contain spaces and '#'")
   # ensure steps is a positive integer
    if not isinstance(steps, int) or steps < 1:
        raise Warning("steps must be a positive integer")

def step(world):
    """returns the next step for a given world"""
    # make a copy for the next step (all cells will eventaully be overwritten)
    result = []
    for row in world:
        result.append([char for char in row])
    # for every game cell, count the surrounding alive cells
    for y in range(1,len(world)-1): # for every line (without the frame)
        for x in range(1, len(world[0])-1): # for every char (without the frame)
            neighbor_coords = [(x-1, y-1), (x, y-1),   (x+1, y-1),
                               (x-1, y),               (x+1, y),
                               (x-1, y+1), (x, y+1),   (x+1, y+1)]
            neighbors = [world[yy][xx] for xx, yy in neighbor_coords]
            alive = neighbors.count("#")
            if alive < 2 or alive >= 4:
                result[y][x] = " "
            elif alive == 3:
                result[y][x] = "#"
            else:
                result[y][x] = world[y][x]
    # new world as a tuple of strings
    return tuple(["".join(row) for row in result])

def display(world):
    """prints the world (useful for debugging)"""
    for row in world:
        print(row)

def evolve(world, steps):
    """validates, performs steps and counts survivors"""
    validate(world, steps)
    for i in range(steps):
        #display(world)
        world = step(world)
    alive = "".join(world).count("#")
    return world, alive



field = (
    "--------------",
    "|            |",
    "|            |",
    "|    ###     |",
    "|    #       |",
    "|     #      |",
    "--------------"
)
steps = 8

result, alive_cells = evolve(field, steps)

print(f"Game of Life after {steps} moves:")
display(result)
print(f"{alive_cells} are alive.")

