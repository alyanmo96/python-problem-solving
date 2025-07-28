#    Splits a string into words and appends the length of each word next to it.

def add_length(str_):
    str_list = str_.split()
    length_list=[]
    for word in str_list:
        length_list.append(word+ ' ' + str(len(word)))

    return length_list

# Example usage
print(add_length("apple ban"))  # Output: ['apple 5', 'ban 3']