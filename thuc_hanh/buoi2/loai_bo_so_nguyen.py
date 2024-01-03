def ktra(n):
    k = 0
    for i in n:
        if not i.isdigit():
            return True
        k = k * 10 + int(i)
    if k <= 2147483647 and k >= -2147483647:
        return False
    return True
file = open('DATA.in', 'r')

a = []
for line in file:
       
    for i in line.split():
        if ktra(i): a.append(i)

for i in sorted(a):
    print(i, end=" ")                   


            
