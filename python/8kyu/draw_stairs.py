"""
Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.
"""

def draw_stairs(n):
    string = ''
    for i in range(n):
        string += f'{"I": >{i+1}}\n'
    
    return string.rstrip()
    


print(draw_stairs(10))
