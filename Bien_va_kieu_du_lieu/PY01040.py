BASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def tong(s):
    sm = 0
    for i in s:
        sm += BASE.index(i)
    return sm

def rotate(s):
    k = tong(s)
    ans = ""
    for i in range(0, len(s)):
        ans += BASE[(BASE.index(s[i]) + k) % 26]
    return ans

t = int(input())
while t > 0:
    str = input()
    n = len(str) // 2
    s1 = str[:n]
    s2 = str[n:]
    s1 = rotate(s1)
    s2 = rotate(s2)
    ans = ""
    for i in range(0, len(s1)):
        ans += BASE[(BASE.index(s1[i]) + BASE.index(s2[i])) % 26]
    print(ans)
    t -= 1

    