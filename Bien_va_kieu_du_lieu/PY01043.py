def check(n):
    if n != n[::-1] or len(n) % 2 != 0:
        return False
    for i in n:
        if int(i) % 2 != 0:
            return False
    return True

t = int(input())
while t > 0:
    n = int(input())
    for i in range(22, n):
        if check(str(i)):
            print(i, end=" ")
    print()
    t -= 1