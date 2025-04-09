"""
In this Kata, you will be given an array of unique elements, and your task is to rearrange the values so that the first max value is followed by the first minimum, followed by second max value then second min value, etc. 
"""

def solve(arr):
    answer = []
    if len(arr) % 2 ==0:
        for i in range(int(len(arr)/2)):
            answer.extend([sorted(arr, reverse=True)[i], sorted(arr)[i]])
    else:
        for i in range(int(len(arr)/2)):
            answer.extend([sorted(arr, reverse=True)[i], sorted(arr)[i]])
        
        answer.append(sorted(arr)[int(len(arr)/2)])
    
    return answer



print(solve([78,79,52,87,16,74,31,63,80]))