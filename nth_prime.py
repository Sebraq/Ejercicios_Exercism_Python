def isprime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def prime(number):
    if number==0:
        raise ValueError('there is no zeroth prime')
    
    counter=0
    num=2
    while True:
        if isprime(num):
            counter+=1
            if counter==number:
                return num
        num+=1

    