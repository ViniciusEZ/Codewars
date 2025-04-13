"""
Positive integers have so many gorgeous features. Some of them could be expressed as a sum of two or more consecutive positive numbers.
Consider an Example :

    10 could be expressed as the sum of 1 + 2 + 3 + 4 .
    Task

Given Positive integer, N , return true if it could be expressed as a sum of two or more consecutive positive numbers , otherwise return false .
Notes

    Guaranteed constraint : 2 ≤ N ≤ (2^32) -1 .
"""

def consecutive_ducks(n):
    return n & n-1 != 0


print(consecutive_ducks(648))


