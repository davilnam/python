n = int(input())
l = list(int(i) for i in input().split())
m = 10 ** 9
p = -1
for i in l:
    x = 0
    for j in l:
        x += abs(i - j)
    if x < m:
        m = x
        p = i
print(m, p)
