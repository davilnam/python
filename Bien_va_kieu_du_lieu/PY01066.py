t = int(input())
while t > 0:
    s = input()
    s_rv = s[::-1]
    ok = True
    for i in range(0, len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) == abs(ord(s_rv[i]) - ord(s_rv[i + 1])):
            continue
        else:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
    t -= 1
