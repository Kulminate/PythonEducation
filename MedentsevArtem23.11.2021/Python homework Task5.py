def triangle_sum(a):
    cnt1 = 1
    cnt2 = 1
    for i in range(a):
        summary = 0
        for j in range(cnt2):
            summary += cnt1
            cnt1 += 2
        cnt2 += 1
    print(summary)


try:
    triangle_sum(int(input('Enter your number:')))
except(ValueError, UnboundLocalError):
    print('That is not a digit. Please, rerun the algorithm.')
