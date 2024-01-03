from math import *
n = int(input())
l = []
for i in range(n):
    l.append(input())
hang = [0] * n
cot = [0] * n
for i in range(n):
    for j in range(n):
        if l[i][j] == 'C': 
            hang[i] += 1
            cot[j] += 1
dem = 0
for i in hang:
    if i > 1:
        dem += comb(i, 2)
for i in cot:
    if i > 1:
        dem += comb(i, 2)
print(dem)