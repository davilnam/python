for _ in range(int(input())):
    s1 = input()
    s2 = input()
    dem = 0
    while len(s1) >= len(s2):
        if s1[0:len(s2)] == s2:
            dem += 1
            s1 = s1[len(s2):]
        else:
            s1 = s1[1:]
    print(dem)