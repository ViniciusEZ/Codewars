"""
Given a number n, you should find a set of numbers for which the sum equals n. This set must consist exclusively of values that are a power of 2 (eg: 2^0 => 1, 2^1 => 2, 2^2 => 4, ...).

The function powers takes a single parameter, the number n, and should return an array of unique numbers.
"""

def powers(n):
    powers_of_two = []
    answer = []

    for i in range(n):

        if 2**i > n:
            break

        powers_of_two.append(2**i)
    
    while powers_of_two:
        answer.append(powers_of_two[-1])
        n = n - powers_of_two[-1]
        powers_of_two = [i for i in powers_of_two if n >= i]         

    return sorted(answer)


print(powers(10))