import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


prime_sum = 0
for i in range(2, 1001):
    if is_prime(i):
        prime_sum += i

print(prime_sum)
