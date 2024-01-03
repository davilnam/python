from collections import *
from math import *
def ktsnt (n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
l = [int(i) for i in input().split()]
l = Counter(l)
l = [i for i in l.keys()]
tong = 0
nho = 0
for i in l:
    tong += i
for i in range(len(l)):
    tong1 = 0
    for j in range(i + 1):
        tong1 += l[j]
    if ktsnt(tong1) and ktsnt(tong - tong1):
        print(i)
        nho = 1
        break
if nho == 0:
    print('NOT FOUND')