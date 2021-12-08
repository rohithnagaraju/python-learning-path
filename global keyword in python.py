"""WHAT IS GLOBAL KEYWORD?"""
"we are creating the function in that function we create some varialbe that is local variable out side of the " \
"function if we mentioned a variable that is called a global variable,,,,let's see the example"


a = 10
def something():
    a = 9
    print(a)

print(a)
"here we got an ans 10 because we are not calling the defined function"
something()
print(a)
"know we got the function value .....so we can use the global variable where we want in the procedure" \
"whith out calling the funtion"
### CAN WE CHANGE THE VALUE OF GLOBAL VARIABLE IN FUNTION?
##  YES.
a= 100
def myfunction():
    global a
    a = 200
    print('inside',a)

myfunction()
print('outside',a)
"""knoe we have an access of global variale in function """
### it is possible to use the two variable in function and global?
## yes by using globals function


a = 21

print(id(a))
def xxx():

    a = 31

    x = globals()['a']
    print(id(x))
    globals()['a']=555
    print('local',a)
xxx()
print('outside',a)
"""so here with the use of globals function we can change the value of global variable in function"""