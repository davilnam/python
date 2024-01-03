def count_digit_occurrences(a, b):
    def count_digit(d, n):        
        count = 0
        multiplier = 1
        while multiplier <= n:
            q, r = divmod(n, multiplier * 10)
            count += q * multiplier
            count += min(max(r - d * multiplier + 1, 0), multiplier)
            if d == 0:
                count -= multiplier                
            multiplier *= 10
        return count
    
    for d in range(10):
        cnt = count_digit(d, b) - count_digit(d, a - 1)
        print(cnt, end=" ")
    print()
        
t = int(input())
while t > 0:
    a, b = [int(i) for i in input().split()]
    count_digit_occurrences(a, b)
    
    t -= 1          