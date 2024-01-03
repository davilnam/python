t = int(input())
for i in range(1, t + 1):
    s1 = sorted(input())
    s2 = sorted(input())
    print(f"Test {i}:", end=" ")
    if s1 == s2:
        print("YES")
    else:
        print("NO")
    