# WHAT IS FILTER?
"""filter take two argument 1 is function & 2 is iterable(given value or sequance) and filter job is to seperate the iterable with
respect to function and condition or filter allows you to process an iterable and extract those iteams thats satisfy the given condition
                    example"""
            ###
"""def seperate_even(numbers):
    return numbers%2==0

numbers =[1,2,3,4,5,6,7,8,9,10]
even = list(filter(seperate_even,numbers))
print(even)"""
                ###
"""can we use lambda here .....yes"""
            ###
"""numbers =[1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda numbers : numbers%2==0,numbers))
print(even)
                ###
# what is map?"""
"""map is a inbuilt function that allows you to process and transform all the iteam in an iterable withoute using 
an explit loop this technique is commanly known as mapping map() is usefull when you need to apply a transformation 
function to each iteam in a iterable
                        example shown below"""
            ###
"""def double_1(n):
    return n*2
numbers =[1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda n : n%2==0,numbers))
print(even)
double = list(map(double_1,even))
print(double)"""
                ###

"""numbers =[1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda n : n%2==0,numbers))
print(even)
double = list(map(lambda n:n*2,even))
print(double)"""
            ###
"what is reduce?  "
"""reduce() is a in build function which required two value one is function and another one is iterable (the sequence or 
operation values) what is its use means reduce function implement a mathematical technique called folding or reduction 
reduce() is use full when u need to apply a function to a iterable and reduce it to a single cumulative value"""
"examples are shown below"
# reduce are ready build we need to import it by functool.

"""from functools import reduce
def sum(a,b):
    return a+b
numbes =[1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda n:n%2==0,numbes))
print(even)
double = list(map(lambda n:n*2,even))
print(double)
sum = reduce(sum,double)
print(sum)"""

"""can we use lamda here .....yes"""
from functools import reduce
number = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda n:n%2==0,number))
print(even)
double = list(map(lambda n:n*2,even))
print(double)
sum = reduce(lambda a,b:a+b,double)
print(sum)

                    #thank you#