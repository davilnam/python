t = int(input())
while t > 0:
    s = input()
    tong = 0
    tich = 1
    cnt = 0
    idx = 0
    for i in range(0, len(s)):
        if i % 2 != 0:
            tong += int(s[i])
        else:
            idx += 1
            if s[i] == '0':
                cnt += 1
            else:
                tich *= int(s[i])
    if idx == cnt:
        tich = 0
    print(tich, tong)

    t -= 1
