"""
Determines if three integers form a Pythagorean triple.

    A Pythagorean triple consists of three positive integers a, b, and c,
    such that a² + b² = c² (the Pythagorean theorem).


"""


def pythagorean_triple(integers):
   
    sorted_list=sorted(integers)
    print(sorted_list)
    a = pow(sorted_list[0],2)
    b = pow(sorted_list[1],2)
    c = pow(sorted_list[2],2)
    if a + b == c:
       return True 
    return False



# Example usage
print(pythagorean_triple([5, 4, 3]))  # Output: True