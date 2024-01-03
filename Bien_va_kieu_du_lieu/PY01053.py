t = int(input())
while t > 0:
    s = [int(i) for i in input() if i != '0'] 
    tich = 1
    for i in s:
        tich *= i
    print(tich)
    t -= 1
