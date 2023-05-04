
def add_prefix_un(word):#Passed
    return "un"+word

def make_word_groups(vocab_words):
    return (" :: "+vocab_words[0]).join(vocab_words)

def remove_suffix_ness(word):#Passed
    word=word[:-4]
    num=len(word)
    if word[num-1]=='i':
        word=word[:-1]
        return word+'y'
    return word

def adjective_to_verb(sentence,index): #Passed
    word=sentence.split()[index]
    num=len(word)
    if word[num-1]=='.':
        word=word[:-1]
    return word+'en'

