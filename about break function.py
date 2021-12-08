"""this is the of break"""


available = 3
candies = int(input("enter the number of candy you want : "))
for i in range(1,candies+1):
    if i>available:
        print("sorry out of stock")
        break
    print("candy")

print("thank you for using visit next time")





