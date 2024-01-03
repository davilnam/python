n = int(input())
l = []
for i in range(n):
    l.append([int (i) for i in input().split()])
tong = 0
tren = 0
cheo = 0
for i in range(n):
    for j in range(n):
        tong += l[i][j]
        if i < j:
            tren += l[i][j]
        if i == j:
            cheo += l[i][j]
duoi = tong - tren - cheo
chenh = abs(duoi - tren)
k = int(input())
if chenh <= k:
    print('YES')
else :
    print("NO")
print(chenh)

