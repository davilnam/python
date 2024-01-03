BASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    str = input()
    if str == '0':
        break
    k, s = str.split()
    k = int(k)
    ans = ""
    for i in range(0, len(s)):
        ans += BASE[(BASE.index(s[i]) + k) % 28]
    print(ans[::-1]) 