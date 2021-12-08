def addition(x,y):
    c= x+y
    print(c)
addition(2,3)
"""we have two argument #formal argument and #actual argument"""
"what is formal argument?"
"so i assigned variable x,y are the formal argument"
"then what is actual argument?"
"the value we given as a input is the actual argument."
"is there any types for argument?"
"yes, in actual argument we have 4 types"
"position"
"keyword"
"default"
"variable length"
                    ### WHAT IS POSITION ARGUMENT?###
"""IT IS NOTHING BUT THE POSITION OF THE VALUE WHICH WE ASSIGNED"""
"FOR AN EXAMPLE"
def personal_details(name,age):
    print(name)
    print(age)
personal_details("rohith",21)
"""by seeing this a question arise that if we change the position will it make that much sence ......NO....but """
def personal_details1(name,age):
    print(name)
    print(age)
personal_details1(21,"rohith")
"""we get an error so by this we come to know that positioning is important but if i forgot the position of defined 
variable what to do means we use the function that is ###KEYWORD###"""
"THEN WHAT IS KEY WORD MEANS it is simply mentioned the variable like"
def personal_details1(name,age):
    print(name)
    print(age-5)
personal_details1(age=28,name='rohit')
"""yes it works by this we can assigned the correct value as input"""
"""then what is default? """
"""for an example we need the two information necessarily but user was not supposed to provide
    like for some application it is mandatory to give age but user is not supposed to give that info means 
     we can set a default value like"""
def personal_details_for_fb(name,age=18):
    print(name)
    print(age)
personal_details_for_fb("rohith",45)
"""if user give the info it take that or else it take the default value which is determined"""
### WHAT IS VARIABLE LENGTH?###
"assume we determined a function for addition in that we give the two variable to store the data " \
"if user want to give n number of data for an operation we use the variable length function"
def n_number_of_addition(x,*y):
    c = x
    for i in y:
        c = c*i
    print(c)

n_number_of_addition(1,2,3,4,5,6,7,8,9)
"""this is the function of variable length argumment"""


