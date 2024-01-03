def tang(a):
    for i in range(0, len(a) - 1):
        if a[i] >= a[i + 1]:
            return False
    return True

def giam(a):
    for i in range(0, len(a) - 1):
        if a[i] <= a[i + 1]:
            return False
    return True

t = int(input())
while t > 0:
    n = input()
    if len(n) < 3:
        print("NO")
    else:
        ok = 0
        for i in range(1, len(n) - 1):
            a, b = n[:i], n[i:]
            if tang(a) and giam(b):
                ok = 1
                break
        if ok:
            print("YES")
        else:
            print("NO")
    t -= 1