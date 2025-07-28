#    Converts time (hours, minutes, seconds) to milliseconds.

def past(h,m,s):
 
 return 1000 * ((3600 *h) + (60 * m) + (s))


# Example usage
print(past(10, 3, 3))  # Output: 36183000