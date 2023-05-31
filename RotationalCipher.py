def rotate(text,key):
    letters='abcdefghijklmnopqrstuvwxyz'
    cipher=''
    for i in text:
        if i ==' ':
            cipher+=' '
        if i.isupper():
            letters=letters.upper()
        else:
            letters=letters.lower()

        if not i==' ':
            index=letters.find(i)
            if index==-1:#letter not present
                cipher+=i
            else:
                index+=key
                if index>=26:
                    index-=26
                cipher+=letters[index]
    return cipher



