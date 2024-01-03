t = int(input())
while t > 0:
    n, k = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    max_value = max(arr)
    idx = arr.index(max_value)
    if idx == 0:
        arr.insert(0, k)
    else:
        arr.insert(idx - 1, k)
    arr.sort()
    print(*arr)
    t -= 1