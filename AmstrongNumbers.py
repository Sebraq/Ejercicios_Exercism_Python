def is_armstrong_number(number):
    num=len(str(number)) #number of digits
    original=number
    result=0
    while (number!=0):
        digit=number%10
        result+=digit**num
        number=number//10
    return result==original

#Help source : https://youtu.be/fdxtmMOfdrc
#Help source 2: https://youtu.be/W_dtihcaR5g