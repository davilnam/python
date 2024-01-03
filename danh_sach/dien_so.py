for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    a = [0] * 1009
    l.sort()
    d = 0
    for i in l:
        a[i] = 1
    for i in range(l[0], l[-1]):
        if a[i] == 0:
            d += 1
    print(d)