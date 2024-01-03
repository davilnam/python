from math import *
def snt(n):
    if n < 10:
        return False
    a = str(n)
    b = a[::-1]
    if a != b:
        return False
    return True
n, m = map(int, input().split())
l = []
nt = -1
for i in range(n):
    l1 = [int(j) for j in input().split()]
    l.append(l1)
    for j in l1:
        if snt(j):
            nt = max(nt, j)
if nt != -1:
    print(nt)
    for i in range(n):
        for j in range(m):
            if l[i][j] == nt:
                print("Vi tri [" + str(i) + '][' + str(j) + "]")
else:
    print("NOT FOUND")