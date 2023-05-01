#1
def value_of_card(card,ace=1):
    if card in "JQK":
        card=10
    elif card=='A':
        return ace
    
    return int(card)
#2   
def higher_card(card_one,card_two):
    if value_of_card(card_one)>value_of_card(card_two):
        return card_one
    elif value_of_card(card_one)<value_of_card(card_two):
        return card_two
    elif value_of_card(card_one)==value_of_card(card_two):
        return card_one,card_two
#3  
def value_of_ace(card_one,card_two):
    if (value_of_card(card_one,ace=11)+value_of_card(card_two,ace=11))>11:
        return int(1)
    return int(11)

#4
def is_blackjack(card_one, card_two):
    if value_of_card(card_one,ace=11)+value_of_card(card_two,ace=11)==21:
        value=True
    else:
        value=False

    return bool(value)
#5
def can_split_pairs(card_one,card_two):
    if value_of_card(card_one,ace=11)==value_of_card(card_two,ace=11):
        value=True
    else:
        value=False

    return bool(value)
   
#6
def can_double_down(card_one,card_two):
    if value_of_card(card_one,ace=1)+value_of_card(card_two,ace=1)>11:
        value=False
    elif card_one=='A' and card_two=='A':
        value=False
    else:
        value=True

    return bool(value)


#Source of help: https://exercism.org/tracks/python/exercises/black-jack/solutions/wenngle