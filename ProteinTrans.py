#1st attempt:

def proteins(strand):
    separate=[strand[i:i+3]for i in range(0,len(strand),3)]
    NewList=[]
    for c in separate:
        if c=='AUG':
            NewList.append('Methionine')
        if c in ('UUC','UUU'):
            NewList.append('Phenylalanine')
        if c in ('UUA','UUG'):
            NewList.append('Leucine')
        if c in ('UCU', 'UCC', 'UCA', 'UCG'):
            NewList.append('Serine')
        if c in ('UAU', 'UAC'):
            NewList.append('Tyrosine')
        if c in ('UGU', 'UGC'):
            NewList.append('Cysteine')
        if c in ('UGG'):
            NewList.append('Tryptophan')  
        if c in ('UAA', 'UAG', 'UGA'):
            break   
    return NewList

#print(proteins('AUGUUC'))

#2nd attempt:
def proteinsVer2(strand):
    separate=[strand[i:i+3]for i in range(0,len(strand),3)]
    dict1={'AUG':'Methionine','UUU':'Phenylalanine','UUC':'Phenylalanine','UUA':'Leucine','UUG':'Leucine','UCU':'Serine', 'UCC':'Serine', 'UCA':'Serine', 'UCG':'Serine','UAU':'Tyrosine', 'UAC':'Tyrosine','UGU':'Cysteine', 'UGC':'Cysteine','UGG':'Tryptophan'}
    NewList=[]
    for c in separate:
        for i in dict1:
            if c in i:
                NewList.append(dict1.get(i))
        if c in ('UAA', 'UAG', 'UGA'):
            break
    return NewList

#print(proteinsVer2('AUGUUC'))
