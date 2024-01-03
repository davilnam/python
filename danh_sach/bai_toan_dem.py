n = int(input())
l = []
while True:
    if len(l) == n:
        break
    l1 = [int(i) for i in input().split()]
    for i in l1:
        l.append(i)
x = [0] * (l[-1] + 1)
for i in range(n):
    x[l[i]] = 1
k = 0
for i in range(1, l[-1] + 1):
    if x[i] == 0:
        print(i)
        k = 1
if k == 0:
    print('Excellent!')
