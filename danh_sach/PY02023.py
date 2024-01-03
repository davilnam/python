# Hai tuple có thể được so sánh bằng cách so sánh các yếu tố từ đầu đến cuối. Nếu có một yếu tố bằng nhau, yếu tố thứ hai sẽ được so sánh... tiếp tục cho tới hết.
t = int(input())
while t > 0:
    n = int(input())
    arr = input().split()
    arr.sort(key=lambda s : (sum(int(i) for i in s), int(s)))
    print(*arr)
    t-=1