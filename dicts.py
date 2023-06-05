def create_inventory(items):
    mydict={}
    for i in items:
        mydict[i]=items.count(i)
    return mydict

#print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))

def add_items(inventory,items):
    for i in create_inventory(items):
        if i in inventory:
            inventory[i]+=create_inventory(items).get(i)
        if i not in inventory:
            inventory[i]=create_inventory(items).get(i)
    return inventory

#print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))
def decrement_items(inventory,items):
    for i in create_inventory(items):
        if i in inventory:
            inventory[i]-=create_inventory(items).get(i)
            if inventory[i]<0:
                inventory[i]=0
    return inventory
#print(decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"]))

def remove_item(inventory,item):
    if item not in inventory:
        return inventory
    inventory.pop(item)
    return inventory

#print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))

def list_inventory(inventory):
    newlist=[]
    inventory=inventory.items()
    for i in inventory:
        if i[1]>0:
            newlist.append(i)
    return newlist

#print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))
