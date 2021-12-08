"""def return_second_min_score(score):
    minScore = min(score)
    minScoreCount = score.count(minScore)
    for i in range(minScoreCount):
        score.remove(minScore)
    return min(score)


if __name__ == '__main__':
    name =[]
    score = []
    n = int(input("enter the number"))
    for _ in range(n):
        x = input("enter the input")
        y = float(input("enter the number"))
        name.append(x)
        score.append(y)




    dummyScore = score[:]
    second_min_score = return_second_min_score(dummyScore)

    namesWithSecondMinScore = []
    for i in range(len(score)):
        if score[i] == second_min_score:
            namesWithSecondMinScore.append(name[i])


    namesWithSecondMinScore.sort()
    # print output
    for name in namesWithSecondMinScore:
        print(name)"""
def return_second_minimum_score(score):
    minimum_score = min(score)
    count_of_min_score = score.count(minimum_score)
    for i in range(count_of_min_score):
        score.remove(minimum_score)
    return min(score)

score = []
name = []
n = int(input("enter the number of data you want to store"))
for i in range(n):
    x = input("enter the student name")
    y = float(input("enter the student marks"))
    name.append(x)
    score.append(y)



second_min_number = return_second_minimum_score(score)
name_second_min_number = []
for i in range(len(score)):
    if score[i]==second_min_number:
        name_second_min_number.append(name[i])
name_second_min_number.sort()
for name in name_second_min_number:
    print(name)








