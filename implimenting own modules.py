"""from m1_calculator import *
c = add(2,3,4,5,6,7,8)
d= sub(2,3,4,5,6,7,8,9)
e = divi(2,3,4,5,6,7,8,9)
f = multi(23,4,5,6,7,68,5)
g = percent(564,625)
print("addotion of values = ",c)
print("subtraction of values=",d)
print("division of values=",e)
print("miltiplication of values=",f)
print("precentage of the value =",g)"""



from m1_calculator import *
print("select the operation you want")
print("1 = addition")
print("2 = subtraction")
print("3 =multiplication")
print("4= division")
print("5 = percentage")
choise = int(input("enter your choise"))
num_1 = int(input("enter the 1st number"))
temp = input("enter second number in formate 1,2,3..... ")
num_2 = (temp.split(','))
num_2= list(map(int,num_2))

if choise == 1:
    a = add(num_1,num_2)
    print(a)
elif choise ==2:
    b = sub(num_1,num_2)
    print(b)
elif choise == 3:
    c = multi(num_1,num_2)
    print(c)
elif choise == 4:
    d = divi(num_1,num_2)
    print(d)
elif choise == 5:
    e =percent(num_1,num_2)
    print(e)
else:
    print("invalide syntax")



