def sum_non_prime_divisors(n):
    sum = 0
    for i in range(2, n+1):
        if is_prime(i) == False:
            sum += i
    return sum

def is_prime(n):
    if n < 2:
        return False
    if n == 2: 
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True

print(sum_non_prime_divisors(500))