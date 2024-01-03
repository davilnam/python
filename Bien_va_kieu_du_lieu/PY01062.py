def nt(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

t = int(input())
while t > 0:
    s = input()
    a = len(s)
    b = [i for i in s if nt(int(i))]
    if nt(a) and len(b) > len(s) - len(b):
        print("YES")
    else:
        print("NO")
    t -= 1
