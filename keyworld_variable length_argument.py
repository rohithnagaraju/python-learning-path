def personal_data(**data):
    for i , j in data.items():
        print(i,j)
personal_data(name='rohith',age=21,address='agraharapalya',phoneNo=9113089878,college='sapthagiri')



def personal_data2(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)



personal_data2(name='rohith',age=21,address='agraharapalya')