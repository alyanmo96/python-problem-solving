"""
    Calculates the total cost of mangoes with a "buy 2, get 1 free" offer.

    For every 3 mangoes, the 3rd one is free.

 """    
def mango(quantity,price):
    lst=[]
    for i in range(1,quantity+1):
        if i % 3 != 0:
            lst.append(i)
    
    
    
    return len(lst)*price



# Example usage
print(mango(2, 3))   # Output: 6
print(mango(3, 3))   # Output: 6
print(mango(5, 3))   # Output: 12
print(mango(9, 5))   # Output: 30