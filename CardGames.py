#1.Tracking Poker Rounds
def get_rounds(number):
    return [number,number+1,number+2]
print(get_rounds(27))

#2.Keeping all rounds in the same place
def concatenate_rounds(rounds1,rounds2):
    return rounds1+rounds2
print(concatenate_rounds([27, 28, 29], [35, 36]))

#3Finding Prior Rounds
def list_contains_round(rounds,round_number):
    """
    return number in rounds
    """
    if round_number in rounds:
        return True
    return False

print(list_contains_round([27, 28, 29, 35, 36], 30))
print(list_contains_round([27, 28, 29, 35, 36], 29))

#4.Averaging Card Values
def card_avarage(hand):
    return sum(hand)/len(hand)
print(card_avarage([5, 6, 7]))

#5.Alternate Averages
import statistics
def approx_average_is_average(hand):
    a=card_avarage(hand)
    firstLast=(hand[0]+hand[-1])/2
    median=statistics.median(hand)
    if firstLast==a or median==a:
        return True
    return False

print(approx_average_is_average([1, 2, 3, 5, 9]))
print(approx_average_is_average([2, 3, 4, 8, 8]))

#6.More Averaging Techniques
def average_even_is_average_odd(hand):
    """
    return card_average(hand[::2]) == card_average(hand[1::2])
    """
    odd=sum(hand[::2])/len(hand[::2])
    even=sum(hand[1::2])/len(hand[1::2])
    if odd==even:
        return True
    return False

print(average_even_is_average_odd([1, 2, 3]))
print(average_even_is_average_odd([1, 2, 3, 4]))
#7.Bonus Round Rules
def maybe_double_last(hand):
    if hand[-1]==11:
        hand[-1]=hand[-1]*2
    return hand

print(maybe_double_last([5, 9, 11]))
print(maybe_double_last([5, 9, 10]))



