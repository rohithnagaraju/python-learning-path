def add(x,y):
    sum = x
    for i in y:
        sum = sum+i
    return sum
def sub(x,*y):
    a =x
    for i in y:
        a = a-i
        return a
def multi(x,*y):
    a = x
    for i in y:
        a =a*i
    return a
def divi(x,*y):
    a =x
    for i in y:
        a = a/i
    return a
def percent(x,y):
    return ((x/y)*100)



