#    Counts the number of positive integers and calculates the sum of negative integers in a list.
def count_positive_sum_negative(arr):
    result_list=[]
    count_of_positive=0
    sum_of_negative=0
    for number in arr:
        if number > 0:
            count_of_positive+=1
        if number <=0:
            sum_of_negative+=number

    result_list.append(count_of_positive)
    result_list.append(sum_of_negative)            

    return result_list



# Example usage
print(count_positive_sum_negative([1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]))  
# Output: [10, -65]