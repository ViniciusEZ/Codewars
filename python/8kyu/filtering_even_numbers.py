"""
The method is supposed to remove even numbers from the list and return a list that contains the odd numbers.

However, there is a bug in the method that needs to be resolved
"""


def kata_13_december(lst): 
    return [i for i in lst if i%2==1]

print(kata_13_december([1, 2, 2, 2, 4, 3, 4, 5, 6, 7]))