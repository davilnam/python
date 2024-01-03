n = int(input())
arr = [float(i) for i in input().split()]
arr.sort()
tong = sum(arr) - arr[0] * arr.count(arr[0]) - arr[-1] * arr.count(arr[-1])
ans = tong / (n - arr.count(arr[0]) - arr.count(arr[-1]))
print("{:.2f}".format(ans))