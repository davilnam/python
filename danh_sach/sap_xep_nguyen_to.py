from math import *
def ktsnt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
l = [int(i) for i in input().split()]
k = [0] * n
l1 = []
l2 = []
for i in range(n):
    if ktsnt(l[i]):
        k[i] = 1
        l1.append(l[i])
    else:
        l2.append(l[i])
l1.sort()
l1 = l1[::-1]
l2 = l2[::-1]
for i in range(n):
    if k[i] == 1:
        print(l1[-1], end = ' ')
        l1.pop()
    else:
        print(l2[-1], end = ' ')
        l2.pop()