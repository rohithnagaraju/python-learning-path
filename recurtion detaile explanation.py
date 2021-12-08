#THIS IS ITERATIVE METHOD
# WE CAN REDUCE THIS FUNCTION USING
"""def sum_mult_n_nmuber(n):
    sum = 0
    mult =1
    for i in range(1,n+1):
        sum+=i
    for j in range(1,n+1):
        mult*=j
    return sum,mult
if __name__ == "__main__":
    n = int(input("enter the number you want to find the some operation"))
    add,mult = sum_mult_n_nmuber(n)
    print(mult)"""

def sum_mult_n_nmuber(n):
    #if n == 1:
        #return 1

    return n+sum_mult_n_nmuber(n-1)
n = int(input("enter the number"))
add = sum_mult_n_nmuber(n)
print(add)




