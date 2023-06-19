def is_paired(input_string):
    openlist=['[',"{","("]
    closelist=[']','}',')']

    newlist=[]

    for i in input_string:
        if i in openlist:
            newlist.append(i)
        elif i in closelist:
            if len(newlist)>0 and openlist[closelist.index(i)]==newlist[len(newlist)-1]:
                newlist.pop()
            else:
                return False
    return len(newlist)==0
   


print(is_paired("([{}({}[])])"))

