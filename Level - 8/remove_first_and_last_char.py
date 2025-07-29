#    Removes the first and last characters from the input string.

def remove_char(s):
    #option 1
    #    return s[1:-1]  # Slice from the second character to the second-last
#option 2
    lst=[]
    for l in s:
        lst.append(l)
    lst[0]=""
    lst[-1]=""    
    return "".join(lst)


print(remove_char("Alian"))   # Output: 'lia'