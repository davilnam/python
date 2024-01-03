def gt(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
t = int(input())
while t > 0:
    s = input()
    tong = 0
    for i in s:
        tong += gt(int(i))
    if tong == int(s):
        print("Yes")
    else:
        print("No")
    t -= 1