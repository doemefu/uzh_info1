#!/usr/bin/env python3

def median(numbers):

    if not numbers:
        return None

    numbers = sorted(numbers)

    middle_idx = len(numbers) // 2
    if len(numbers) % 2:
        return numbers[middle_idx]
    else:
        l = numbers[middle_idx-1]
        r = numbers[middle_idx]
        return (l+r)/2