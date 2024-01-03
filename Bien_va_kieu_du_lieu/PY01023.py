def pt(n):
    print("1 * ", end="")
    for i in range(2, int(n ** 0.5) + 1):
        cnt = 0
        if n % i == 0:
            while n % i == 0:
                cnt += 1
                n = n // i
            print(f"{i}^{cnt}", end="")
            if n != 1:
                print(" * ", end="")
    if n != 1:
        print(f"{n}^1")  
    print()     


t = int(input())
while t > 0:
    n = int(input())
    pt(n)
    t -= 1
