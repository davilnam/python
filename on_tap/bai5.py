t = int(input())
while t > 0:
    n, m = input().split()
    s1 = input()
    s2 = input()
    num1 = int(s1.replace(n, m)) + int(s2.replace(n, m))
    num2 = int(s1.replace(m, n)) + int(s2.replace(m, n))
    print(min(num1, num2), max(num1, num2))
    t -= 1