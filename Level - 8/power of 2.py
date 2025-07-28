#    Generates a list of powers of 2 from 0 up to n (inclusive).

def powers_of_two(n):
    result=[]

    x=0
    while x<=n:
        result.append(pow(2,x))
        x+=1

    return result



# Example usage
print(powers_of_two(0))  # Output: [1]
print(powers_of_two(1))  # Output: [1, 2]
print(powers_of_two(2))  # Output: [1, 2, 4]