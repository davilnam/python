import math
n = int(input())
arr = [int(i) for i in  input().split()]
for i in range(0, len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if math.gcd(arr[i], arr[j]) == 1:
            print(arr[i], arr[j])
