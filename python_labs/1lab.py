import math

#Task 1
#Var 6
#function 1
print("Var 6\n")
print("Task 1 \n")

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

print("Найти сумму непростых делителей числа. ")
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

print("\nНайти количество цифр числа, меньших 3.")
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

print("\nНайти количество чисел, не являющихся делителями исходного числа, не взамнопростых с ним и взаимно простых с суммой простых цифр этого числа.")
print(f3(9712))



#Task 2-4
#Var 6 (6, 12, 12)
#6
import random
print("\nTask 2-4")

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

print("\nДана строка в которой записаны слова через пробел. Необходимо перемешать в каждом слове все символы в случайном порядке кроме первого и последнего.")
print(new_words)

#12
def digit_chars(str):
    new_str = ""
    for char in str:
        if char.isdigit():
            new_str += char
    for char in str:
        if char.isalpha():
            new_str+=char
    return new_str

print("\nДана строка в которой содержатся цифры и буквы. Необходимо расположить все цифры в начале строки, а буквы – в конце. ")
print(digit_chars("Вариант 6. Задачи 6, 12, 12."))


#Task 5
print("\nTask 5")
print("\nДана строка. Необходимо найти все даты, которые описаны в виде 31 февраля 2007.\n")
import re
from datetime import datetime

def is_valid_date(day, month, year):
    try:
        datetime.strptime(f"{day} {month} {year}", "%d %B %Y")
        return True
    except ValueError:
        return False

def find_valid_dates(text):
    month_names = {
        'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,
        'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
        'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
    }
    
    pattern = r'\b(\d{1,2})\s+([а-яё]+)\s+(\d{4})\b'
    dates = re.findall(pattern, text, re.IGNORECASE)
    
    valid_dates = []
    for day, month, year in dates:
        month_lower = month.lower()
        if month_lower in month_names: #and is_valid_date(int(day), month_names[month_lower], int(year)): #если нужна проверка на правильность даты
            valid_dates.append((day, month, year))
    
    return valid_dates

dates = find_valid_dates("""Дана строка.31 февраля 2007? 23 января 3004, 3 июля 1999 лыоадвфыодва""")
print("Найденные даты:")
for day, month, year in dates:
    print(f"{day} {month} {year}")


print("\nTask 6-8")
#6, 12, 12
def find_numbers_more_5(str):
    all_numbers = []
    i = 0
    while i < len(str):
        if str[i].isdigit():
            number = str[i]
            for j in range(i + 1, len(str)):
                if(str[j].isdigit()):
                    number+=str[j]
                else:
                    break
            i = j
            try:
                if int(number) > 5:
                    all_numbers.append(number)
            except ValueError:
                print("Error number")
        i += 1
    return all_numbers

print("\n Дана строка. Необходимо подсчитать количество чисел в этой строке, значение которых больше 5")
print(find_numbers_more_5("lasjflksj234739sdksld31 1odjs39503"))

