#    Returns the minimum value in the array using functools.reduce.

from functools import reduce


def minimum(arr):
    #option 1
    #return min(arr)
    #option 2
    return sorted(arr)[0]

def maximum(arr):
    #option 1
    #return max(arr)
    #option 2
    return sorted(arr)[-1]


# Example usage
print(minimum([8, 9, -7, 11, -1444, 65]))  # Output: -1444
print(maximum([8, 9, -7, 11, -1444, 65]))  # Output: 65
