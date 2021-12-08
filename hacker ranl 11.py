def average_of_marks_of(name):
    s = 0
    for i in marks:
        s = s+i
        avarage = (s/3)
    return avarage
marks =[(20,20,20),(30,30,30),(40,40,40)]
name =["rohith","likith","ajay"]

avarage_marks_name = average_of_marks_of(marks)

average_marks_name = []
for i in range(len(marks)):
    if marks[i]==name[i]:
        average_marks_name.append(marks)
        print(marks)




