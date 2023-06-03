def abbreviate(words):
    words=words.replace('-',' ').replace(',','').replace('_','')
    myword=''
    newlist=words.split()
    for i in newlist:
        myword+=i[0].upper()
    return myword

#print(abbreviate("The Road _Not_ Taken"))