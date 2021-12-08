# RETURN STATEMENT CAN BE USED TO RETURN SOMETHING FROM THE FUNCTION.
# IN PYTHON , IT IS POSSIBLE TO RETURN ONE OR MORE VARIABLE/VALUE.
# SYNTAX:-
# return(variable or expression)
# examples are shown below:-
""" y = []
    number = int(input("how many number you want to do operation"))
    for r in range(number):
        x = int(input("enter the number"))
    y.append(x)"""


def add_sub_multi(*y):


    sum = 0
    for i in y:
        sum = sum+i
    sub = 0
    for j in y:
        sub = sub-j
    mult = 1
    for k in y:
        mult = mult*k

    return sum,sub,mult

add,sub,mult = add_sub_multi(2,3,4,5,6,7,8)
print(add)
print(sub)
print(mult)




