t = int(input())
while t > 0:
    n = int(input())
    arr, cnt = {}, 0
    for i in range(n):
        x = int(input())
        if x in arr:
            arr[x] += 1
        else:
            arr[x] = 1
        cnt = max(cnt, arr[x])
    ans = 10000
    for k, v in arr.items():
        if v == cnt:
            ans = min(ans, k)
    print(ans)    
    t -= 1