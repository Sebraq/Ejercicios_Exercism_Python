def find_anagrams(word,candidates):
    NewList=[]
    for i in candidates:
        if len(word.lower())==len(i.lower()) and sorted(word.lower())==sorted(i.lower()) and word.lower()!=i.lower():
            NewList.append(i)
    return NewList

#print(find_anagrams("good",["dog", "goody"]))
