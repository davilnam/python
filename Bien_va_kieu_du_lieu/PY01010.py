t = int(input())
while t > 0:
    s = input()
    x = int(s[0:2])
    y = int(s[-2:])
    if x == y:
        print("YES")
    else:
        print("NO")
    t -= 1