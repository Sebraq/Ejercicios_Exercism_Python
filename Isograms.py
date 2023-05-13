def is_isogram(string):
    letters="abcdefghijklmnopqrstuvwxyz"
    string=string.lower()
    for c in letters:
        if string.count(c)>1:
            return False
    return True

print(is_isogram("six-year-old"))

#NOT MINE:
def is_isogram(string):
    string = string.lower().replace(' ', '').replace('-', '')
    return len(string) == len(set(string))