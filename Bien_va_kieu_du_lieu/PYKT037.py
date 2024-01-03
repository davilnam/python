BASE = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = int(input())
while t > 0:
    n, k = [int(i) for i in input().split()]
    ans = []
    while n != 0:
        a = n % k
        n = n // k
        ans.append(BASE[a])
    print("".join(ans[::-1])) 
    t -= 1