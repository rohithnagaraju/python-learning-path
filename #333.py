def second_min_number(num):
    minimum = -99999
    second_minimum = -99999
    for i  in num:
        if i>=minimum:
            if i!=minimum:
                second_minimum =minimum
            minimum = i
        elif i>second_minimum:
            second_minimum = i

    return second_minimum

num = [57,57,-57,57]
print(second_min_number(num))








