s = input()
t = 0
for i in s:
    if i.islower():
        t += 1
if t >= len(s) - t:
    print(s.lower())
else:
    print(s.upper())