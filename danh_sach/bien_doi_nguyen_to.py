from math import *
l = []
def ktnt(n):
    if n < 2: return 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return 0
    return 1
for i in range (10001):
    if ktnt(i) == 1:
        l.append(i)
def tinh(p):
    x = p
    while p > 0:
        if ktnt(p) == 1:
            return x - p
        else:
            p -= 1
def tinh2(p):
    x = p
    while ktnt(p) != 1:
            p += 1
    return p - x
n = int(input())
k = list(int(i) for i in input().split())
m = 0
for i in k:
    a = min(tinh(i), tinh2(i))
    m = max(m, a)
print(m)