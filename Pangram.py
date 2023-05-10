def is_pangram(sentence):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for c in alpha:
        if c not in sentence.lower():
            return False
        
    return True

#Help Source :https://www.geeksforgeeks.org/python-program-to-check-if-given-string-is-pangram/