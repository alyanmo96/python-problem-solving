#    Repeats a given string a specified number of times.

def repeat_str(repeat,string):
    #option 1 (shorter):
    #return string * repeat

    #option 2(manual loop):

    repeated_string = ""
    for i in range(repeat):
        repeated_string+=string
    
    return repeated_string


# Example usage
print(repeat_str(6, "I"))  # Output: IIIIII