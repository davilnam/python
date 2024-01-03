def solve(s):
    if len(s) % 2 == 0 or s[0] == s[1]:
        print("NO")
        return
    for i in range(0, len(s) - 2, 2):
        if s[i] != s[i + 2]:
            print('NO')
            return
    print("YES")

t = int(input())
while t > 0:
    s = input()
    solve(s)
    t -= 1
