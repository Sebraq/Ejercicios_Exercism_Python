def commands(binary_str):
    action=['wink','double blink','close your eyes','jump','']
    NewList=[]
    for index,i in enumerate(binary_str[:0:-1]):
        if i=='1':
            NewList.append(action[index])
    if binary_str[0]=='1':
        return NewList[::-1]
    return NewList
     
#print(commands('11111'))  