def probsep(word):
    listvow=['a','e','i','o','u','xr','yt']
    listcons=['squ','qu','sch','ch','thr','th','y','rh']
    for v in listvow:
        if word.startswith(v):
            return word+'ay'
    for c in listcons:
        if word.startswith(c):
            return word[len(c):]+ c + 'ay'
    
    return word[1:]+word[0]+'ay'

def translate(text):
    return ' '.join([probsep(w) for w in text.split()])


print(translate('xray'))

    
    