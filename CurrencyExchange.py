#1.
def exchange_money(budget,exchange_rate):
    """This function should return the value of the exchanged
    budget : The amount of money you are planning to exchange.
    exchange_rate : The amount of domestic currency equal to one unit of foreign currency.
    """
    return budget/exchange_rate
#2
def get_change(budget,exchanging_value):
    """
    This function should return the amount of money that is left from the budget
    """
    return budget-exchanging_value
#3
def get_value_of_bills(denomination,number_of_bills):
    """
    This exchanging booth only deals in cash of certain increments.
    The total you receive must be divisible by the value of one "bill" 
    or unit, which can leave behind a fraction or remainder. 
    Your function should return only the total value of the bills 
    (excluding fractional amounts) the booth would give back. Unfortunately, 
    the booth gets to keep the remainder/change as an added bonus.
    """
    return denomination*number_of_bills
#4
def get_number_of_bills(budget,denomination):
    """
    This function should return the number of currency bills that you can receive within the given budget. 
    In other words: How many whole bills of currency fit into the amount of currency you have in your budget? 
    Remember -- you can only receive whole bills, not fractions of bills, so remember to divide accordingly.
    Effectively, you are rounding down to the nearest whole bill/denomination.
    """
    return budget//denomination
#5
def get_leftover_of_bills(budget,denomination):
    """
    This function should return the leftover amount that cannot be exchanged from your budget given the denomination of bills.
    It is very important to know exactly how much the booth gets to keep.
    """
    return budget%denomination
#6
def exchangeable_value(budget,exchange_rate,spread,denomination):
    """
    This function should return the maximum value of the new currency after calculating the exchange rate plus the spread.
    Remember that the currency denomination is a whole number, and cannot be sub-divided.
    """
    fees=exchange_rate+(exchange_rate*(spread/100))
    change=budget//fees
    real=change//denomination
    return int(real*denomination)


