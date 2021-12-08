"""so there are so many inbuilt functions in python but not every thing !
 so there is an option called def here we can create the function we want """
"""examples are :-"""
"""if we need to greet user like hi good morning instead of creating this string again and again we can create a 
    function shown below
"""
def greet():
    print("hi")
    print("good morning user")
""" so the functione is defined we can use it anyware we want"""

greet()

"""lets creat another function for addition """
def add_sub_multi(x,y):
    a = x+y
    b = x-y
    c = x*y

    print("addition",a)
    print("subtraction",b)
    print("multiplication",c)
add_sub_multi(32376868,527478836)
###
def persentage(x,y):
    c = (x/y)*100
    print("your persentage is",c)
persentage(564,625)


