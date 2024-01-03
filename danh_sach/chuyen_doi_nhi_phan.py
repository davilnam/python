rf = open('DATA.in')
t = rf.readline()
f = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
t = int(t)
for _ in range(t):
    k = int(rf.readline())
    if k == 2: k = 1
    elif k == 4:
        k = 2
    elif k == 8:
        k = 3
    else : k = 4
    s = rf.readline().rstrip('\n')
    kq = ""
    i = len(s)
    while i >= k:

        x = s[i - k :i]
        i -= k
        d = 0
        for j in range(k):
            d = d + (int(x[j]) * (2 ** (k - j - 1)))
        kq = f[d] + kq
    if i > 0:
        d = 0
        xxx = s[:i]
        for j in range(len(xxx)):
            d += int(xxx[j]) * (2 ** (len(xxx) - 1 - j))
        kq = f[d] + kq
    print(kq)