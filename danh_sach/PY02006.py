t = int(input())
while t > 0:
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a = sorted(a)
    b = sorted(b)
    ok = True
    for i in range(0, n):
        if b[i] < a[i]:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
    t -= 1