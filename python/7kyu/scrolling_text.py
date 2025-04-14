"""
Let's create some scrolling text!

Your task is to complete the function which takes a string, and returns an array with all possible rotations of the given string, in uppercase.
"""

def scrolling_text(text):
    answer = []
    word = text

    while len(answer) != len(text):
        word = list(word)
        letter = word.pop()
        word = letter + ''.join(word)   
        answer.append(word.upper())



    return answer[::-1]

print(scrolling_text("abc"))

