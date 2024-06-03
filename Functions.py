#functions to add two nos.

def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
a=9
b=8
calculateGmean(a,b)

def CalculateSum(a,b):
    addition=a+b
    print(addition)
a=8
b=4
CalculateSum(a,b)

def isGreater(a,b,c):
    if (a>b) and (a>c):
        print("a is greatest")
    elif (b>c) and (b>a):
        print("b is greatest")
    elif (c>a and c>b):
        print("c is greatest")
    else:
        print("a b and c are equal")
a=8
b=8
c=8
isGreater(a,b,c)

