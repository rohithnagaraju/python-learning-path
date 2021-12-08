number = int(input("enter the number you want to check: "))
i = 2
while i<number:


    if number%i==0:
        print(number,"is not prime")
        break
    i+=1

else:
    print(number, "is prime number")




