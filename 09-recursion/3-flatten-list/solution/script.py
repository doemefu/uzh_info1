#!/usr/bin/env python3

def flatten_list(nested_list):
    if not isinstance(nested_list, list):
        raise TypeError("Expected argument has to be a list.")

    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
