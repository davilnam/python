from collections import Counter
n, m = map(int, input().split())
l = [int(i) for i in input().split()]
x = Counter(l)
pp = []
nho = 0
for i in x.items():
    pp.append(i)
pp.sort(key=lambda pp: (-pp[1], pp[0]))
nhung = pp[0][1]
for i in range(len(pp)):
    if pp[i][1] < nhung:
        nho = 1
        print(pp[i][0])
        break
if nho == 0:
    print('NONE')
