BASE = [i for i in range(0, 100000)]

def check(n, k):
    ans = []
    while n != 0:
        a = n % k
        n = n // k
        ans.append(BASE[a])
    if ans[::-1] == ans:
        return True
    else:
        return False
        
a, b, k = [int(i) for i in input().split()]
cnt = 0
for i in range(a, b + 1):
    if check(i, k):
        cnt += 1
print(cnt)
