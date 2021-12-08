def prime_number_for_given_interval(number):
    for number in range(lowe_case,upper_case+1):
        if number>1:
            for i in range(2,number):
                if number%i==0:
                    break
            else:
                print(number)









lowe_case = int(input("enter the from number"))
upper_case = int(input("enter the to number"))
number = lowe_case,upper_case

