"""
A Nice array is defined to be an array where for every value n in the array, there is also an element n - 1 or n + 1 in the array.
"""

def is_nice(arr):
    if not arr:
        return False

    return all([False if not i - 1 in arr and not i + 1 in arr else True for i in arr])
  

print(is_nice([1,2, 5]))