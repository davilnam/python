n = int(input())
l = []
k = [0] * n
for i in range(n):
    x = [int(j) for j in input().split()]
    l.append(x)

if n == 1:
    print(*l)
elif n == 2:
    print(l[0][1] // 2, l[0][1] // 2)
else:
    k[0] = (l[0][-1] - l[1][-1] + l[0][1]) // 2
    for i in range(1, n):
        k[i] = l[0][i] - k[0]
    print(*k)