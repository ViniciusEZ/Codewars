"""
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
"""

def maps(a):
    return [n*2 for n in a]


print(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))