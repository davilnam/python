s = input()
if len(s) % 2 ==1:
    s = s[:len(s) - 1]
l = set()
for i in range(0, len(s), 2):
    l.add(int(s[i: i + 2]))
l = list(l)
l.sort()
print(*l)