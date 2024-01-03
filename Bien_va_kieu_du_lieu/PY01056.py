def nt(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(s):
    for i in range(0, len(s)):
        if i % 2 == 0:
            if int(s[i]) % 2 != 0:
                return False
        else:
            if int(s[i]) % 2 == 0:
                return False
    return True

t = int(input())
while t > 0:
    s = input()
    tmp = [int(i) for i in s]
    tong = sum(tmp)
    if nt(tong) and check(s):
        print("YES")
    else:
        print("NO")
    t -= 1
