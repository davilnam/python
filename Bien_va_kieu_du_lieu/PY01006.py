t = int(input())
while t > 0:
    n = input()
    cnt = len([i for i in n if i == '4' or i == '7'])
    if cnt == len(n):
        print("YES")
    else:
        print("NO")
    t -= 1
