def solve(s):
    myList = []
    if s[0] == '-':
        myList.append(int(s[:2]))
        for i in range(2, len(s)):
            myList.append(int(s[i]))
    else:
        for i in range(0, len(s)):
            myList.append(int(s[i]))
    return myList

s = input()
myList = solve(s)
n = len(myList)
if n == 1:
    print(1)
else:
    cnt = 0
    while(n != 1):
        sm = sum(myList)
        cnt += 1
        sm = str(sm)
        myList = solve(sm)
        n = len(myList)
    print(cnt)
