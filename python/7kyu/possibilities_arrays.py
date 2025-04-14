"""
A non-empty array a of length n is called an array of all possibilities if it contains all numbers between 0 and a.length - 1 (both inclusive).

Write a function that accepts an integer array and returns true if the array is an array of all possibilities, else false.
"""

def is_all_possibilities(arr):
    return [i for i in range(len(arr))] == sorted(arr)


print(is_all_possibilities([3,2,1,0]))