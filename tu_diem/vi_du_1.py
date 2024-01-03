def solve(s1, s2):
    ans = ""
    size = min(len(s1), len(s2))
    for i in range(size):
        if s1[i] == s2[i]:
            ans += s1[i]
        else:
            break
    return ans

myList = ['pqrefgh', 'pqrsfgh']
ans = 0
res = ""
for i in range(len(myList) - 1):
    for j in range(i + 1, len(myList)):
        tmp = solve(myList[i], myList[j])
        if ans < len(tmp):
            ans = len(tmp)
            res = tmp
print(res)

