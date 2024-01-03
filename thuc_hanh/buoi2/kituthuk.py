def find_character(n, k):
    s = "A"
    for i in range(2, n + 1):
        s = s + chr(64 + i) + s[::-1]
    return s[k-1]

for t in range(int(input())):
    n, k = [int(i) for i in input().split()]
    c = find_character(n, k)
    print(c)