s1 = input().lower().split()
hop = s1.copy()
s2 = input().lower().split()
giao = []

for i in s2:
    if i not in s1:
        hop.append(i)
    else:
        giao.append(i)
hop = sorted(list(set(hop)))
print(" ".join(hop))
giao = sorted(list(set(giao)))
print(" ".join(giao))

    


