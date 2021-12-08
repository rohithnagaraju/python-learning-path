def fibonacchi(number):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,number):
        c = a+b
        a = b
        b = c
        print(c)
number = int(input("enter the the the number you want to check for fibomacchi: "))
fibonacchi(number)