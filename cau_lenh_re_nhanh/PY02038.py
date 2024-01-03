import math

n = int(input())
cnt = 0
my_list = []

for _ in range(0,n):
    row = [i for i in input()]
    my_list.append(row)

tmp = [[my_list[j][i] for j in range(n)] for i in range(n)]

for i in range(0,n):
    a = my_list[i].count('C')
    b = tmp[i].count('C')
    cnt += math.comb(a, 2) + math.comb(b, 2)

print(cnt)
