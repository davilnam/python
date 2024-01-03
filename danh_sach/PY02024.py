# Hai tuple có thể được so sánh bằng cách so sánh các yếu tố từ đầu đến cuối. Nếu có một yếu tố bằng nhau, yếu tố thứ hai sẽ được so sánh... tiếp tục cho tới hết.
def solve(s):
    ans = 1
    for i in s:
        ans *= int(i)
    return (ans, int(s))

t = int(input())
while t > 0:
    n = int(input())
    arr = input().split()
    arr.sort(key=solve)
    print(*arr)
    t-=1