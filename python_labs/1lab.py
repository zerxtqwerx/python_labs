import math

#Task 1
#Var 6
#function 1
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

#function 2
def count_digit_less_three(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit < 3:
            count += digit
        n = n // 10
    return count

print(count_digit_less_three(2423145))

#function 3
def f3(n):
    count = 0
    sum_p_d = sum_non_prime_divisors(n)
    for i in range(2, n//2):
        if (n % i == 0) and (math.gcd(n, i) > 1) and (math.gcd(i, sum_p_d) == 1):
            count += 1
    return count

def sum_prime_digit(n):
    sum = 0
    while n > 0:
        digit = n % 10
        if digit in [2, 3, 5, 7]:
            sum += digit
        n = n // 10
    return sum

print(f3(9712))



#Task 2-4
#Var 6 (6, 12, 12)
#6
import random

def shuffle_chars(word):
    if len(word) <= 2:
        return word
    chars = list(word[1:-1])
    random.shuffle(chars)
    new_word = word[0] + ''.join(chars) + word[-1]
    return new_word

str = "Необходимо перемешать в каждом слове все символы в случайном порядке кроме первого и последнего"
words = str.split(' ')
new_words = []
for word in words:
    new_words.append(shuffle_chars(word))

print(new_words)
