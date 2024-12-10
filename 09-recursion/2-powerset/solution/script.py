#!/usr/bin/env python3

def powerset(nums):
    if len(nums) == 0:
        return [[]]
    nums = list(set(nums))

    base = powerset(nums[:-1])
    return base + [(b + nums[-1:]) for b in base]
