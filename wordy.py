def answer(question="What is 53 plus 2?"):
    operator={'plus':'+','minus':"-",'multiplied':"*",'divided':'/'}

    if not question.startswith('What is') or 'cubed' in question:
        raise ValueError("unknown operation")
    
    question=question.strip('?').replace('What is','').replace('by','').split()

    for index,i in enumerate(question):
        if i in operator:
            question.insert(index,operator[i])
            question.remove(i)
    
    for i in range(0,len(question)-1):
        if question[i]==question[i+1]:
            raise ValueError("syntax error")
        
    if len(question)==5:
        question.insert(0,"(")
        question.insert(4,")")
        
    try:
        return int(eval(' '.join(question)))
    except:
        raise ValueError("syntax error")

#print(answer("What is 1 plus 1 plus 1?"))