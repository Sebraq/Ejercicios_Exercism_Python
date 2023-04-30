def square(number):
    if number<1 or number>65 :
        raise ValueError("square must be  between 1 and 64")
    return 2**(number-1) #2^2-1=2 2^3-1=4
def total():
    return 2**64-1