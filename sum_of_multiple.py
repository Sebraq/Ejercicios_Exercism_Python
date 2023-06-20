def sum_of_multiples(limit, multiples):
    numbMult=[]
    for i in multiples:
        for r in range(0,limit):
            if i!=0 and r%i==0:
                numbMult.append(r)
    return sum(set(numbMult))

#print(sum_of_multiples(1, [0])) #what the fuck is divmod???---search