while True:
    t = int(input())
    if t == 0:
        break
    l = []
    for i in range(t):
        l.append(int(input()))
    l = sorted(i for i in l)
    if l[0] == l[t - 1]:
        print('BANG NHAU')
    else:
        print(l[0], l[t - 1])

