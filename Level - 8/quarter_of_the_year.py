"""
    Returns the quarter of the year for a given month.

    The year is divided into 4 quarters:
    - Q1: January (1) to March (3)
    - Q2: April (4) to June (6)
    - Q3: July (7) to September (9)
    - Q4: October (10) to December (12)

"""


def quarter_of_the_year(month):
    #return int(month/3)
    from math import ceil
    return ceil(month/3)

# Example usage
print(quarter_of_the_year(1))   # 1
print(quarter_of_the_year(2))   # 1
print(quarter_of_the_year(3))   # 1
print(quarter_of_the_year(4))   # 2
print(quarter_of_the_year(5))   # 2
print(quarter_of_the_year(6))   # 2
print(quarter_of_the_year(7))   # 3
print(quarter_of_the_year(8))   # 3
print(quarter_of_the_year(9))   # 3
print(quarter_of_the_year(10))  # 4
print(quarter_of_the_year(11))  # 4
print(quarter_of_the_year(12))  # 4