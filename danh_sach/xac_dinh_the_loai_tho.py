from math import *
l = []
for _ in range(int(input())):
    s = input()
    l.append(len(list(s.split())))
dem = 0
a = []
while len(s) > 0:
    if l[0] == 6:
        a.append(1)
        dem += 1
        while l[0] == 6 or l[0] == 8:
            l.remove(l[0])
            if len(l) == 0: 
                break
    if len(l) == 0: break
    if l[0] == 7 and len(l) >= 4:
        dem += 1
        a.append(2)
        for j in range (4):
            l.remove(7)
print(dem)
for i in a:
    print(i)     
    