n =  int(input("enter the number"))
score = []
for i in range(n):
    num = int(input("enter the score"))
    score.append(num)
max_score = score[0]
for j in range(len(score)):
    if score[j]>max_score:
        max_score = score[j]






