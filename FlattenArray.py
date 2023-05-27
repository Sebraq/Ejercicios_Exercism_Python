def flatten(iterable):
    newlist=[]
    for c in iterable:
        if type(c) is list:
            c=flatten(c)
            newlist.extend(c)
        elif c is not None:
            newlist.append(c)
    return newlist
