def rebase(input_base, digits, output_base):
    outputlist=[]
    if input_base < 2 :
        raise ValueError('input base must be >= 2')
    if output_base <2 :
        raise ValueError('output base must be >= 2')
    
    if any(d < 0 for d in digits):
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if any(d>=input_base for d in digits):
            raise ValueError("all digits must satisfy 0 <= d < input base")

    number=sum(dig*input_base**index for index,dig in enumerate(digits[::-1]))
    
    print(number)
    if number==0:
        return [0]
    
    while number>=1:
        outputlist.append(number%output_base)
        number=number//output_base
        

    outputlist.reverse()

    return outputlist
      
print(rebase(2, [1, 0, 1, 0, 1, 0], 10))
