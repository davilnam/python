n, m = [int(i) for i in input().split()]
a = []
min_v = 100000
max_v = 0
for i in range(0, n):
    tmp = [int(x) for x in input().split()]
    a.append(tmp)
    res1 = max(a[i])
    max_v = max(res1, max_v)
    res2 = min(a[i])
    min_v = min(res2, min_v)

mm = max_v - min_v
ok = False
for i in range(0, n):
    for j in range(0, m):
        if a[i][j] == mm:
            ok = True
            break
if not ok:
    print("NOT FOUND")
else:
    print(mm)
    for i in range(0, n):
        for j in range(0, m):
            if a[i][j] == mm:
                print(f"Vi tri [{i}][{j}]")
                
