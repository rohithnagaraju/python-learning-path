def even_and_odd_number_for_the_interval(number):
    even = []
    odd = []

    for number in range(from_number,to_number+1):

            if number%2==0:
                even.append(number)
            else:
                odd.append(number)
    return even,odd
from_number =int(input("enter the from number: "))
to_number = int(input("enter the to number: "))
number = from_number,to_number


evenlist,oddlist=even_and_odd_number_for_the_interval(number)
print(sum(oddlist))


def sum(num):
    totalsum=0
    for i in num:
        totalsum=totalsum+i
    return totalsum

