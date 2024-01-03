def cmp(a):
    return a[0] - a[1]

n, k = map(int, input().split())
save1 = []
save2 = []
save1 = list(map(int, input().split()))
save2 = list(map(int,input().split()))

ans = []
for i in range(n):
    ans.append((save1[i],save2[i]))

ans = sorted(ans, key = cmp )
sum = 0


for i in range(0,n):
    if i < k :
        sum += ans[i][0]
    else :
        if ans[i][0] - ans[i][1] < 0:
            sum += ans[i][0]
            k += 1

for i in range(k, n) : sum += ans[i][1]

print(sum)