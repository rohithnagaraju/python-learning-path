def leap(year):
    if year%4==0:
        leap= True
        if year%100==0 and year%400!=0:
            leap = False
    return leap



num =  int(input("enter the year you want to check it is leap year or not"))
print(leap(num))



