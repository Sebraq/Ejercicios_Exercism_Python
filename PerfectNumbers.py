def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    sum=0
    if number<=0:
        raise ValueError("Classification is only possible for positive integers.")
    for i in range(1,number):
        if number%i==0:
            sum+=i
    if sum==number:return "perfect"
    if sum>number:return "abundant"
    if sum<number:return "deficient"