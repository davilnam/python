n, m = map(int, input().split())
l = []
for i in range(n):
    l.append([int(i) for i in input().split()])
kq = []
if n > m:
    k = n - m
    for i in range(n):
        if k > 0 and i % 2 == 0:
            k -= 1
            continue
        else:
            kq.append(l[i])
    for i in range(m):
        for j in range(m):
            print(kq[i][j], end=' ')
        print()
elif n < m:
    k = m - n
    for i in range(n):
        hang = []
        x = k
        for j in range(m):
            if x > 0 and j % 2 == 1:
                x -= 1
                continue
            else:
                hang.append(l[i][j])
        kq.append(hang)
    for i in range(n):
        for j in range(n):
            print(kq[i][j], end=' ')
        print()
else:
    for i in range(n):
        for j in range(n):
            print(l[i][j], end = ' ')
        print()