from collections import Counter
s = input()
if len(s) % 2 == 1:
    s = s[:len(s) - 1]
l = []
for i in range(0, len(s), 2):
    l.append(int(s[i:i+2]))
l = Counter(l)
for i in l.keys():
    print(i, end = ' ')
