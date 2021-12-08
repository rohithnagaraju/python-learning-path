def prime_number_using_forloop(n):
    for i in range(2,n):
        if n%i==0:
            print("your number is not prime number")
            break
    else:
        print("your number is a prime number")

n = int(input("entr the number you want to search"))


prime_number_using_forloop(n)











