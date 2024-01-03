t = int(input())
while t > 0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    myDict, cnt = {}, 0
    for i in arr:
        if i in myDict.keys():
            myDict[i] += 1
        else:
            myDict[i] = 1
        cnt = max(cnt, myDict[i])

    mid = n // 2
    if cnt <= mid:
        print("NO")
    else:
        ans = 1000000
        for k, v in myDict.items():
            if v == cnt:
                ans = min(ans, k)
        print(ans)
    t-=1