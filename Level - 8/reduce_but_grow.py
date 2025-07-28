
#    Multiplies all the numbers in the list and returns the product.

def grow(lst):
    
    result = 1
    for n in lst:
        result *=n

    return result

# Example usage
print(grow([1, 2, 3, 4]))  # Output: 24