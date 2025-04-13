"""
Write a function which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits. 
"""

def sum_digits(number):
    return sum([int(n) for n in list(str(number)) if n.isnumeric()])


print(sum_digits(-32))