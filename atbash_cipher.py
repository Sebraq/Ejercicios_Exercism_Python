plain='abcdefghijklmnopqrstuvwxyz'
cipher='zyxwvutsrqponmlkjihgfedcba'
table=str.maketrans(plain,cipher)

def encode(plain_text):
    plain_text=plain_text.replace(' ','').replace(',','').lower().strip('.')
    div=[plain_text.translate(table)[i:i+5] for i in range(0,len(plain_text),5)]
    return " ".join(div)

def decode(ciphered_text):
    ciphered_text=ciphered_text.replace(' ','').lower()
    return ciphered_text.translate(table)

#print(decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"))
#print(encode('Truth is fiction.'))