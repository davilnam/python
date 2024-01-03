for _ in range(int(input())):
    s = input()
    if len(s) > 100:
        k = s[:100]
        if s[100] != ' ' and s[99] != ' ':
            while k[len(k) - 1] != " ":
                k = k[:len(k) - 1]
        s = k
    print(s)