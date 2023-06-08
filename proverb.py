def proverb(*args,qualifier):
    if not args:
        return [*args]
    list=[f"For want of a {args[i]} the {args[i+1]} was lost." for i in range(0,len(args)-1)]
    
    if qualifier==None:
        list.append(f"And all for the want of a {args[0]}.")
        return list
    
    list.append(f"And all for the want of a {qualifier} {args[0]}.")
    return list  

#input=['car','sea']
#print(proverb(*input,qualifier='horseshoe'))