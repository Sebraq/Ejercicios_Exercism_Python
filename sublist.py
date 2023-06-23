SUBLIST = "Sub"
SUPERLIST = "Super"
EQUAL = "Equal"
UNEQUAL = "Unequal"

def sublist(list_one, list_two):

    if list_one==list_two:
        return EQUAL
    if list_one==[] and not list_two==[]:
        return SUBLIST
    if list_two==[] and not list_one==[]:
        return SUPERLIST
    if len(list_one)>len(list_two):
        for i in range(len(list_one)-len(list_two)+1):
            if list_two==list_one[i:i+len(list_two)]:
                return SUPERLIST
    if len(list_one)<len(list_two):
        for i in range(len(list_two)-len(list_one)+1):
            if list_one==list_two[i:i+len(list_one)]:
                return SUBLIST
    return UNEQUAL
 
print(sublist([], [1, 2, 3]))