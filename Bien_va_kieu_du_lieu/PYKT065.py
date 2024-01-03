def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input())
count = 0

for p in range(2, int(N**0.5) + 1):
    if is_prime(p):
        for q in range(p + 1, int(N**0.5) + 1):
            if is_prime(q):
                    candidate = p**2 * q**2
                    if candidate <= N:
                        count += 1

print(count)