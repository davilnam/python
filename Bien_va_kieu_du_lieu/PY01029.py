import math
t = int(input())
while t > 0:
    n = input()
    n_rev = n[::-1]
    if math.gcd(int(n), int(n_rev)) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1