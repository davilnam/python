n = input()
cnt = len([i for i in n if i == '4' or i == '7'])
if cnt == 4 or cnt == 7:
    print("YES")
else:
    print("NO")
