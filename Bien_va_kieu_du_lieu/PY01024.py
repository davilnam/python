def check(s):
    sum = int(s[-1])
    for i in range(0, len(s) - 1):
        sum += int(s[i])
        if abs(int(s[i]) - int(s[i + 1])) != 2:
            return False
    return sum % 10 == 0


t = int(input())
while t > 0:
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
    t -= 1
    
