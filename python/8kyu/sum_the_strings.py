"""
Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string)
"""

def sum_str(a, b):
    # if a and b:
    #     return str(int(a) + int(b))
    # elif a:
    #     return a
    # elif b:
    #     return b
    # else:
    #     return str(0)
    return str(int(a or 0) + int(b or 0))

print(sum_str("9",""))