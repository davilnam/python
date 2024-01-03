dic = {}
for _ in range(int(input())):
    l = input().split()
    if l[3] == "IN":
        if l[4] not in dic:
            dic[l[4]] = 0
        if l[1] == 'Xe_con':
            if l[2] == '5' :
                dic[l[4]] += 10000
            else :
                dic[l[4]] += 15000
        elif l[1] == 'Xe_tai':
            dic[l[4]] += 20000
        else :
            if l[2] == '29':
                dic[l[4]] += 50000
            else :
                dic[l[4]] += 70000
for i in dic:
    print(i + ": " + str(dic[i]))