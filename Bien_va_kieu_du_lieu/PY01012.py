s1 = input()
s2 = input()
p = int(input())
ans = ""
for i in range(0, len(s1)):
    if(i == p - 1):
        ans += s2
    ans += s1[i]
print(ans)