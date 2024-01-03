t = int(input())
while t > 0:
    s = [int(i) for i in input()]
    tong = sum(s)
    tmp = str(tong)
    if tong == int(tmp[::-1]) and len(tmp) > 1:
        print("YES")
    else:
        print("NO")
    t -= 1
