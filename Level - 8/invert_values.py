#    Inverts the sign of each number in the input list.

def invert(lst):
    returned_list=[]
    for number in lst:
                # Invert the sign by multiplying by -1 or using the unary minus operator

        returned_list.append(-number)
    return returned_list


print(invert([1,2,3,4,5]))
print(invert([-1,-2,-3,-4,-5]))
print(invert([]))