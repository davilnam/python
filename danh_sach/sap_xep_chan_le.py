n = int(input())
k = []
while True:
    x = list(int(i) for i in input().split())
    k += x
    if len(k) == n: break
chan = []
le = []
dd = [0] * n
for i in range(n):
    if k[i] % 2 == 0:
        chan.append(k[i])
        dd[i] = 1
    else:
        le .append(k[i])
chan.sort()
le.sort()
chan = chan[::-1]
for i in range(n):
    if dd[i] == 1:
        print(chan[-1], end = " ")
        chan.pop()
    else:
        print(le[-1], end = " ")
        le.pop()
