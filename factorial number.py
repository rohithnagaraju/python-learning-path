def foctorial_number_for_n_number(number):
    fac = 1
    for i in range(1,number+1):
        fac = fac*i
    return fac

number = int(input("enter the number you want to check for factorial"))

print(foctorial_number_for_n_number(number))