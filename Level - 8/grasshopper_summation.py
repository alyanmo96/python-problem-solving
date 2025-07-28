#    Calculates the sum of all integers from 1 to the given number (inclusive).

def summation(num):

    result=0
    for i in range(num+1):
        result +=i
    return result

# Example usage
print(summation(2))  # Output: 3