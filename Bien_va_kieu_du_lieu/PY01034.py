t = int(input())
while t > 0:
    n = [i for i in input()]
    res = n.copy()
    i = len(n) - 2
    while i >= 0 and int(n[i]) <= int(n[i + 1]):
        i -= 1
    if i == -1:
        print(-1)
    else:
        for j in range(len(n) - 1, i - 1, -1):
            if int(n[j]) <= int(n[i]):
                n[i], n[j] = n[j], n[i]
        tmp = n[i + 1:]
        n[i + 1:] = tmp[::-1]
        s1 = "".join(n)
        s2 = "".join(res)
        if len(str(int(s1))) < len(n) or int(s1) == int(s2):
            print(-1)
        else:
            print(s1)
    t -= 1
        