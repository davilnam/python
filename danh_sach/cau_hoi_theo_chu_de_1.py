dic = {}
l = []
for _ in range(int(input())):
    a = input()
    l.append(a)
dic[l[0]] = 0
b = l[0]
for i in range(1, len(l)):
    if l[i] != "":
        if l [i - 1] == "":
            dic[l[i]] = 0
            b = l[i]
        else:
            dic[b] += 1
for i in dic:
    print(i + ": " + str(dic[i]))