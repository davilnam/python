t = int(input())
while t > 0:
    s = input()
    n = input()
    tmp = int(n)
    sz = len(n)
    i = 0
    cnt = 0
    while i < len(s):
        if s[i] == n[0]:
            if s[i:(i + sz)] == n:
                cnt += 1
                i = i + sz
        i += 1
    print(cnt)
    t -= 1