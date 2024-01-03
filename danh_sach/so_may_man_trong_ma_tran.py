n, m = map(int, input().split())
l = []
be = 100005
lon = -1
for i in range(n):
    l1 = [int(j) for j in input().split()]
    l.append(l1)
    lon = max(lon, max(l1))
    be = min(be, min(l1))
nt = lon - be
k = 0
dd = 0
for i in range(n):
    for j in range(m):
        if l[i][j] == nt:
            if k == 0:
                print(nt)
                k = 1
            dd = 1
            print("Vi tri [" + str(i) + '][' + str(j) + "]")
if dd == 0:
    print("NOT FOUND")