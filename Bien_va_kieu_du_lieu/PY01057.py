def nt(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

def solve(s):
    for i in range(0, len(s)):
        if nt(int(s[i])) and (not nt(i)):
            print("NO")
            return
        elif (not nt(int(s[i]))) and nt(i):
            print("NO")
            return
    print("YES")

t = int(input())
while t > 0:
    s = input()
    solve(s)
    t -= 1
    
