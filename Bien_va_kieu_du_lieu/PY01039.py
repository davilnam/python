def check(n):
    a = n.count(n[0])
    b = n.count(n[1])
    if a + b != len(n):
        print("NO")
        return
    for i in range(0, len(n) - 2):
        if n[i] != n[i + 2]:
            print("NO")
            return
    print("YES")    

t = int(input())
while t > 0:
    n = input() 
    check(n)
    t -= 1