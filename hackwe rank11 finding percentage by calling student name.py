"""n = int(input("enter the number"))
student_marks = {}
for i in range(n):
    name, line = input().split()
    score = list(map(float,line))
    student_marks[name] = score
query_name = input("enter the name of student")

s = 0
for i in student_marks[query_name]:
    s = s+i
print(s/3)"""

student = dict()
n = int(input("how many students data you want to store:"))
for i in range(n):
    student_name = input("enter the student name: ")
    student_marks = []
    s = int(input("enter how many marks you want to add"))
    for j in range(s):
        marks = float(input("enter the student marks: "))
        student_marks.append(marks)
    total_marks = int(input("enter the total marks"))
    student[student_name]=student_marks
to_find_avgofstudent = input("enter the student name")
s= 0
for i in student[to_find_avgofstudent]:
    s = s+i
percentge_of_student = (s/total_marks)*100
print("the average marks of",to_find_avgofstudent,"is",percentge_of_student)

