def roman(number):
    numbers=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    symbols=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    newstring=''
    i=12
    while number: #Execute if number!=0 or !=None
        n=number//numbers[i]
        number=number%numbers[i]
        
        while n:#Execute if number!=0 or !=None
            newstring+=symbols[i]
            n-=1
        i-=1
    return newstring
#print(roman(3001))

