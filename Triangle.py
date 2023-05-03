def equilateral(sides):
    [a,b,c]=sides
    return a==b==c and a==b==c!=0

def isosceles(sides):
    [a,b,c]=sides
    return (equilateral(sides) or (a==b and a!=c) or (a==c and a!=b) or (b==c and c!=a) ) and a+b>=c and b+c>=a and a+c>=b
    
def scalene(sides):
    [a,b,c]=sides
    return a!=b!=c and b!=c!=a and c!=a!=b and a+b>=c and b+c>=a and a+c>=b
    
