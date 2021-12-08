
number_list = []
n = int(input("how many number you want to add: "))
for i in range(n):
    num = int(input("enter the nmuber: "))
    number_list.append(num)
maximum_num = number_list[0]
for j in range(len(number_list)):
    if number_list[j]>maximum_num:
        maximum_num = number_list[j]
print(maximum_num)

