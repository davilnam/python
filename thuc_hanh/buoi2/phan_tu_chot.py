

t = int(input())
while t > 0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    tim_min = [-1] * n
    tim_max = [-1] * n
    lon = -1
    nho = 1e10
    for i in range(0, n):
        lon = max(lon, arr[i])
        tim_max[i] = lon
        if nho > arr[n - i - 1]:
            nho = arr[n - i - 1]
            tim_min[n - i - 1]  = nho
    
    ans = 0
    for i in range(n):
        if(arr[i] == tim_max[i] and arr[i] == tim_min[i]):
            ans += 1
    print(ans)
    t -= 1
