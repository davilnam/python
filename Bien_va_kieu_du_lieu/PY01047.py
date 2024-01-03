def nt(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

t = int(input())
while t > 0:
    s = input()
    a = int(s[-4:])
    if nt(a):
        print("YES")
    else:
        print("NO")
    t -= 1
