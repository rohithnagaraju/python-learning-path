def factorial(num):
    f = 1
    for i in range(1,num+1):
        f = f*i
    return f




num = int(input("enter the number you want to check for factorial"))


print(factorial(num))

