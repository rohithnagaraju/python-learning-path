"""from array import *
arry = array("u",[])
n = int(input("how many number of input you want to add: "))
for i in range(n):
    x = int(input("enter the value: "))
    arry.append(x)
print(arry)
value = int(input("enter the value you want to search: "))
k = 1
for s in arry:
    if s == value:
        print(k)
        break
    k+=1"""











"""def obtaining_the_value():
    #obtaining the value from the user and printing a list of number and also find the number value(index)
    array = []
    name_range = int(input("how many names you want to store" ))
    for i in range(name_range):
        name = input("enter the name")
        array.append(name)
    print(array)
    value = input("enter the name")
    length=1
    for s in array:
        if value==s:
            print(length)
            break
        length+=1"""


def all_student_deatils():
    my_list = []
    number_details = int(input("enter how many number of detail you want to store"))
    for i in range(number_details):
        student_name = input("enter the name")
        age = input("enter the age")
        address = input("enter the address")
        studying_class = input("enter the present class which student was studied ")
        details = student_name,age,address,studying_class
        my_list.append(details)

    finding_details = input("enter the student name")
    length =1
    for j in details:
        if finding_details == j:
            print(length)
            break
        length+=1
    return my_list

print(all_student_deatils())







