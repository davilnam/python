sz = 2000000
prime = [0] * 2000009

# tìm ước nguyên tố nhỏ nhất của các số
def sang():
    i = 2
    while(i * i <= sz):
        if prime[i] == 0:
            j = i
            while (j <= sz):
                if prime[j] == 0:
                    prime[j] = i
                j += i
        i += 1
    for i in range(2, sz + 1):
        if (prime[i] == 0):
            prime[i] = i

def tinh(n):
    if (prime[n] == 0):
        return n
    sum = 0
    while (n != 1):
        sum += prime[n]
        n = n // prime[n]  
    return sum;  

tong = 0
t = int(input())
sang()
while t > 0:
    n = int(input())
    tong += tinh(n)
    t -= 1
print(tong)
