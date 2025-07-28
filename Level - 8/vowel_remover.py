#    Removes all lowercase vowels from the input string.


def shortcut(s):
    vowles=['a','e','i','o','u']
    result = []

    for letter in s:
        if letter not in vowles:
            result.append(letter)
    
    
    return "".join(result)



# Example usage
print(shortcut("Hello"))  # Output: 'Hll'