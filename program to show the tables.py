def tables_for_n_number(num):
    for i in range(1,end_number+1):
        print(num,'X',i,'=',num*i)




num = int(input("enter the number of tables you want: "))
end_number = int(input("what is the range of tables you want: "))


tables_for_n_number(num)