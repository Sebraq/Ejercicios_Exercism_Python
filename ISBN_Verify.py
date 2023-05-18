def is_valid(isbn):
    letters='ABCDEFGHIJKLMNOPQRSTUVWYXZ'
    x=list(isbn.replace('-',''))
    total=0;n=10
    if len(x)!=10:return False
    
    if x[-1]=='X':x[-1]='10'

    for c in x:
        if c in letters:
            return False
        
    while n>1:
        for i in x:
            total+=int(i)*n
            n-=1
    return bool(total%11==0)