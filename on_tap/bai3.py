def solve(s):
    res = 0
    ans = 0
    s += 'a'
    for i in s:
        if i.isdigit():
            res = res * 10 + int(i)
        else:
            if res != 0:
                ans = max(ans, res)
            res = 0
    return ans


t = int(input())
while t > 0:
    s = input()
    res = solve(s)
    print(res)
    t -= 1