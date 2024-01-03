def prime_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    
    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
                
    return primes

def prime_sum_divisors(numbers):
    limit = max(numbers)
    primes = prime_sieve(limit)
    
    prime_divisors = set()
    for num in numbers:
        for prime in primes:
            if prime * prime > num:
                break
            while num % prime == 0:
                prime_divisors.add(prime)
                num //= prime
        if num > 1:
            prime_divisors.add(num)
    
    prime_sum = sum(prime_divisors)
    return prime_sum

# Đọc dữ liệu đầu vào
N = int(input())
numbers = []
for _ in range(N):
    num = int(input())
    numbers.append(num)

# Tính và in ra kết quả
result = prime_sum_divisors(numbers)
print(result)
