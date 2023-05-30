def to_rna(dna_strand):
    MyList=list(dna_strand)
    for index,i in enumerate(MyList):
        changeletter(i,index,MyList)
    return ''.join(MyList)
    

def changeletter(i,index,list):
    lettersL=['G','C','T','A']
    replaceL=['C','G','A','U']
    for key,c in enumerate(lettersL):
        if i==c:
            list.pop(index)
            list.insert(index,replaceL[key])
    
print(to_rna('CAT'))
            
"""Another solution:
def to_rna(dna_strand):
    rna = ""
    for letter in dna_strand:
        if letter == "C":
            rna += "G"
        elif letter == "G":
            rna += "C"
        elif letter == "T":
            rna += "A"
        elif letter == "A":
            rna += "U"
    return rna

    Another one:
    LOOKUP = str.maketrans("GCTA", "CGAU") ????? Search this cuz its new for me
def to_rna(dna_strand):
    return dna_strand.translate(LOOKUP)
"""

