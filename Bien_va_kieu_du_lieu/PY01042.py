t = int(input())
while t > 0:
    s = list(input())
    ans = [1 for i in s if (i == '0' or i == '1' or i == '2')]
    if sum(ans) == len(s):
        print("YES")
    else: 
        print("NO")
    t -= 1