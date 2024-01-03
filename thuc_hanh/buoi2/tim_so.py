import gmpy2
import math


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print("Case #" + str(i) + ":", end=" ")
    result = math.pow((3 + math.sqrt(5)), n)
    arr = str(result).split(".")
    res = arr[0][-3:]
    if(len(res) == 3):
        print(res)
    else:
        res = (3 - len(res)) * '0' + res
        print(res)
        