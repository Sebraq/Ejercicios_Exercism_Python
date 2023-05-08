# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

listSiu=[ONES,TWOS,THREES,FOURS,FIVES,SIXES]

def score(dice, category):
    order=sorted(dice)
    maxment=max(dice,key=dice.count)
    maxoccur=dice.count(maxment)

    if category in listSiu:
        return dice.count(category)*category
    elif category==YACHT and maxoccur==5:
        return 50
    elif category==CHOICE:
        return sum(dice)
    elif category==BIG_STRAIGHT and order==[2,3,4,5,6]:
        return 30
    elif category==LITTLE_STRAIGHT and order==[1,2,3,4,5]:
        return 30
    elif category==FOUR_OF_A_KIND and maxoccur>=4:
        return maxment*4
    elif category==FULL_HOUSE and maxoccur==3:
        return sum(dice)
    else:
        return 0