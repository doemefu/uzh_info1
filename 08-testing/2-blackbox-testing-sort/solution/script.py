#!/usr/bin/env python3

def sort(it):
    "Inspired by Bubble-Sort algorithm"

    if not hasattr(it, "__iter__"):
        return None
    it = list(it)

    num_elems = len(it)
    was_changed = True
    while was_changed:
        was_changed = False
        # every iteration, there is one item less to check
        num_elems -= 1
        for i in range(num_elems):
            if it[i] > it[i + 1]:
                tmp = it[i]
                it[i] = it[i + 1]
                it[i + 1] = tmp
                was_changed = True

    return it
