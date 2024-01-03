t = int(input())
while t > 0:
    n, d = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    res = a[d:] + a[:d]
    print(*res)
    t -= 1
