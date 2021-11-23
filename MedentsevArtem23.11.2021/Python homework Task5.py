def triangle_sum(a):
    cnt1 = 1
    cnt2 = 1
    summary = 0
    for i in range(a):
        for j in range(cnt2):
            summary += cnt1
            cnt1 += 2
        cnt2 += 1
    print(summary)



triangle_sum(int(input()))
