"""
    Sums two numbers given as strings and returns the result as a string.

    If either input is an empty string, it is treated as "0".
"""
def sum_str(a,b):
    a=0 if a=="" else int(a)
    b=0 if b=="" else int(b)
    return str(a + b)


# Example usage
print(sum_str("4", "5"))  # Output: '9'
print(sum_str("", "7"))   # Output: '7'
print(sum_str("", ""))    # Output: '0'