# should return thr rounderd to the smallest value

"""
    Calculates the amount of water (in liters) John should drink based on the time spent cycling.

    John drinks 0.5 liters of water every hour (or 1 liter every 2 hours).
    This function returns the total amount of water he should drink,
    rounded down to the nearest whole number.
"""

def liters(time):
    #return time//2
    #return int(time/2)
    return int(float(time/2))


# Example usage
print(liters(3))
print(liters(6.7))
print(liters(11.8))