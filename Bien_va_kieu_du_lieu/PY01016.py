t = int(input())
while t > 0:
    ans = ''
    s = input()
    for i in range(0, len(s)):
        if s[i].isdigit():
            ans = ans + (s[i - 1] * int(s[i]))
    print(ans)
    t -= 1
