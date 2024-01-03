s = input()
a = ["688", "68", "6"]
for i in a:
    s = s.replace(i, "")
if len(s) == 0:
    print("YES")
else:
    print("NO")