t = int(input())
while t > 0:
    s = input()
    ans = ""
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
        else:
            ans += i
    ans = sorted(list(ans))
    ans = "".join(ans) + str(sum)
    print(ans)
    t -= 1