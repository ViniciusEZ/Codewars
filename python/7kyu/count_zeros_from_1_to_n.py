"""
Create an algorithm to count the number of zeros that appear between 1 and N.
"""

def count_zeros(x):
    # n = 0
    # for i in range(1, x+1):
    #     n += int(str(i).count('0'))

    return sum([int(str(i).count("0")) for i in range(1, x+1)])


print(count_zeros(200))