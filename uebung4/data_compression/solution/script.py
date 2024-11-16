#!/usr/bin/env python3

def compress(data):
    if len(data) == 0:
        return ((), [])

    keys = tuple(sorted(data[0].keys()))

    values = []
    for e in data:
        v = []
        for k in keys:
           v.append(e[k])
        values.append(tuple(v))

    return (keys, values)
