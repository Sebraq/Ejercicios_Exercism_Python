def distance(strand_a,strand_b):
    errors=0
    if len(strand_a)!=len(strand_b):
        raise ValueError("Strands must be of equal length.")
    for c in range(len(strand_a)):
        if strand_a[c]!=strand_b[c]:
            errors+=1
    return errors

print(distance("GGACGGATTCTG","AGGACGGATTCT"))