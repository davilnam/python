ds = [-4,-5,1000, -3, 0, -100, 6]
sum = 0
ans = 1e9
for i in range(0, len(ds)):
    sum += ds[i]
    if sum > 0: sum = 0

    ans = min(ans, sum)

print(ans)