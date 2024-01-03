n = int(input())
arr = []
for i in range(0, n):
    tmp = [int(j) for j in input().split()]
    arr.append(tmp)

sum1 = 0
sum2 = 0
for i in range(0, n):
    for j in range(0, n):
        if j < n - i - 1:
            sum1 += arr[i][j]
        if j > n - i - 1:
            sum2 += arr[i][j]

k = int(input())
if abs(sum1 - sum2) <= k:
    print("YES")
else:
    print("NO")
print(abs(sum1 - sum2))
