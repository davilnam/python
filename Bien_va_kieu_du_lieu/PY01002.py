s = input()
sum = 0
for i in range(0, len(s) - 1):
    if s[i].isdigit():
        sum += int(s[i])
if sum == int(s[len(s) - 1]):
    print("YES")
else:
    print("NO")

