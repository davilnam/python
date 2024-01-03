def hn(n, st, ed):
    if n == 1:
        print(f"{st} -> {ed}")
        return
    tmp = ord('A') + ord('B') + ord('C') - ord(st) - ord(ed)
    hn(n - 1, st , chr(tmp))
    print(f"{st} -> {ed}")
    hn(n - 1, chr(tmp), ed)

n = int(input())
hn(n, 'A', 'C')