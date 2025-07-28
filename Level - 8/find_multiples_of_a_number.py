#    Finds all positive multiples of a given integer up to a specified limit.

def find_multiplies(integer, limit):
    result_list=[]
    x = 1
    while x<= int(limit/integer):
        result_list.append(integer * x)
        x+=1

    return result_list


# Example usage
print(find_multiplies(5, 21))  # Output: [5, 10, 15, 20]