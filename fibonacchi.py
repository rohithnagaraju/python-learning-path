def fibonachi(number):



    a = 0
    b = 1
    if number==1:
        print(a)
    elif number<1:
        print("invalid number")
    else:

        print(a)
        print(b)

        for i in range(2,number):
            c = a+b
            a = b
            b = c
            print(c)



number = int(input("enter the number you want to check"))


fibonachi(number)


