def nt(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

t = int(input())
while t > 0:
    s = input()
    prime = [2, 3, 5, 7]
    tmp = [i for i in s if int(i) in prime]
    if nt(len(s)) and len(tmp) > len(s) - len(tmp):
        print("YES")
    else:
        print("NO")
    t -= 1
