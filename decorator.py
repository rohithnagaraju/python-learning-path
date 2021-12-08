def division(a,b):
    print(a/b)
def modifing_division_function(function):
    def inner_function(a,b):
        if a<b:
            a,b = b,a
            return function(a,b)
    return inner_function

new_division = modifing_division_function(division)

new_division(2,4)








