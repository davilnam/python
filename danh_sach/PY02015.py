def solve(arr):
    cnt = 0
    while arr.count(arr[0]) != 4:
        tmp = arr.copy()
        for i in range(4):
            arr[i] = abs(tmp[i] - tmp[(i + 1) % 4])
        cnt += 1
    return cnt   

while True:
    arr = [int(x) for x in input().split()]
    tong = sum(arr)
    if tong == 0:
        break
    cnt = solve(arr)
    print(cnt)
