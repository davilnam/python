n, k = map(int, input().split())
l = [int(i) for i in input().split()]
l.sort()
d = 1
for i in range(n - 1):
    if l[i + 1] - l[i] > k:
        d += 1
print(d)