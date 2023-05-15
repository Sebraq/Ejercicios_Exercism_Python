def score(x,y):
    """
    We got P1(0,0) and P2(X,Y) so we apply distance between points.
    d=sqrt((X-0)^2+(Y-0)^2)
    """
    distance=(x**2 + y**2)**0.5
    if distance<=1:
        return 10
    if distance<=5:
        return 5
    if distance<=10:
        return 1
    

    return 0
