#!/usr/bin/env python3

def invert(d):
    res = {}
    for k, v in d.items():
        if v not in res: res[v] = []
        res[v].append(k)

    for k in res:
        res[k] = sorted(res[k])

    return res

