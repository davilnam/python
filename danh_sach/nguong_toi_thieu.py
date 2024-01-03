from collections import Counter
s = input()
if len(s) % 2 == 1:
    s = s[:len(s) - 1]
l = []
for i in range(0, len(s), 2):
    l.append(int(s[i:i + 2]))
l = Counter(l)
x = []
for i in l.items():
    x.append(i)
x.sort(key = lambda  l : (l[0]))
muc = int(input())
nho = 0
for i in x:
    if i[1] >= muc:
        print(str(i[0]) + " " + str(i[1]))
        nho = 1
if nho == 0 :
    print("NOT FOUND")
