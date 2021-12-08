def prime_number_using_whileloop(num):
    i = 2
    while i<num:
        if num%i==0:
            print("your number is not prime number")
            break
        i+=1

    else:
        print("your number is prime number")


num = int(input("entr the number you want to check"))



prime_number_using_whileloop(num)
