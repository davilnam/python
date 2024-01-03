t = int(input())
while t > 0:
    s = input()
    tmp = s[::-1]
    check = False
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(tmp[i]) - ord(tmp[i - 1])):
            check = True
            break
    if check:
        print("NO")
    else:
        print("YES")    
    t -= 1
