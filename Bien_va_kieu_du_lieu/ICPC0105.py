t = int(input())
while t > 0:
    s = input()
    s += 'a'
    tmp = 0
    res = -1e18
    ans = -1e18
    for i in range(0, len(s)):
        if (s[i] >= '0' and s[i] <= '9'):
            tmp = tmp * 10 + int(s[i])
        else:
            if tmp > 0: 
                res = tmp
                ans = max(ans, res)
                tmp = 0
    print(ans)
    t -= 1
