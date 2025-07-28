#    Determines whether a number is even or odd.

def even_or_odd(number):

    if number % 2==0:
        return "even"
    else:
        return "odd"

# Example usage
print(even_or_odd(2))  # Output: 'even'
print(even_or_odd(1))  # Output: 'odd'