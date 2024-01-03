t = int(input())
while t > 0:
    s = input()
    s += 'a'
    tmp = 0
    ans = 1e18
    for i in range(0, len(s)):
        if s[i].isdigit():
            tmp = tmp * 10 + int(s[i])
        else:
            if tmp > 0:
                ans = min(ans, tmp)
                tmp = 0
    print(ans)
    t -= 1