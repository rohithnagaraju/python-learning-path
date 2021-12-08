score =[]
n = int(input("enter the number of score you want to store"))
for i in range(n):
    x = int(input("enter the score"))
    score.append(x)
maximuum_score = max(score)
counting_max_score = score.count(maximuum_score)
for j in range(counting_max_score):
    score.remove(maximuum_score)
print(max(score))