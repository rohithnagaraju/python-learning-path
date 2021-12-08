
from array import*
def cout(list):
    even = 0
    odd = 0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    print("NO OF EVEN NUMBER IN LIST IS =",even)
    print("NO ODF ODD NUMBER IN LIST IS =",odd)

list = array('i',[])
n = int(input("hoe many numbers you wanr to search?"))
for i in range(n):
    x = int(input("enter the number"))
    list.append(x)





cout(list)


