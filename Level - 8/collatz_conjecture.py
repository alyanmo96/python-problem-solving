#    Calculates the number of steps required to reach 1 in the Collatz sequence.

def hotpo(n):
    number_of_steps = 0
    if n <=0:
        return False

    
    while n!=1:
        if n % 2 ==0:
            n=n/2
           
        else:
            n=(3*n)+1
      
        number_of_steps += 1
    return number_of_steps



# Example usage
print(hotpo(1))  # Output: 0
print(hotpo(5))  # Output: 5
print(hotpo(6))  # Output: 8