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

print("\n Дана строка. Необходимо найти те символы кириллицы, которые не задействованы в данной строке. ")

def find_cyrillic(text):
    cyrillic = "абвгдеёжзийклмнопрстуфхц"
    remove_chars = ""
    for char in text:
        if char.lower() in cyrillic:
            remove_chars += char.lower()
    result = set(cyrillic) - set(remove_chars)
    return sorted(result)

print(find_cyrillic("Дана строка. Необходимо найти те символы кириллицы, которые не задействованы в данной строке."))

print("\nTask 9")
print("\nПрочитать список строк с клавиатуры. Упорядочить по длине строки.")

def input_lines():
    lines = []
    print("Введите строки:")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines

lines = input_lines()
print(sorted(lines, key=len))

print("\nTask 10")
print("\nПрочитать список строк с клавиатуры. Упорядочить по количеству слов в строке.\n")

lines.sort(key=lambda x: len(x.split()))
print(lines)

print("\nTask 11 - 14") #3, 6, 8, 12
print("\nОтсортировать строки в порядке увеличения разницы между частотой наиболее часто встречаемого символа в строке и частотой его появления в алфавите.")

def task11(lines):
    def calculate_difference(text):
        if not text: 
            return float('inf')
        
      
        char_count = {}
        for char in text:
            char_count[char] = char_count.get(char, 0) + 1
        
        most_common_char, max_count = max(char_count.items(), key=lambda x: x[1])
        
        string_freq = max_count / len(text)
        
        alphabet_size = len(set(text))
        alphabet_freq = 1 / alphabet_size if alphabet_size > 0 else 0
        
        return abs(string_freq - alphabet_freq)
    
    return sorted(lines, key=calculate_difference)

result = task11(lines)

print("\nСортировка по разнице частот:")
for line in result:
    print(f"  {line}")

print("\nОтсортировать строки в порядке увеличения медианного значения выборки строк (прошлое \
медианное значение удаляется из выборки и производится поиск нового \
медианного значения). \n")

def task12(lines):
    def median_sort(strings):
        if not strings:
            return []
        
        working_list = strings.copy()
        result = []
        
        while working_list:
           
            sorted_list = sorted(working_list)
            n = len(sorted_list)
            
            if n % 2 == 1:
                median_index = n // 2
                median_value = sorted_list[median_index]
            else:
                median_index = n // 2 - 1
                median_value = sorted_list[median_index]
            
            result.append(median_value)
            
            for i in range(len(working_list)):
                if working_list[i] == median_value:
                    del working_list[i]
                    break
        
        return result
    
    return median_sort(lines)

print(task12(lines))

print("\n Отсортировать строки в порядке увеличения квадратичного отклонения между средним \
весом ASCII-кода символа в строке и максимально среднего ASCII-кода \
тройки подряд идущих символов в строке.\n")
def task13(lines):
    
    def calculate_metrics(text):
        if len(text) == 0:
            return 0, 0, 0

        ascii_sum = sum(ord(char) for char in text)
        mean_ascii = ascii_sum / len(text)
        
        max_triplet_mean = float('-inf')
        
        if len(text) >= 3:
            for i in range(len(text) - 2):
                triplet = text[i:i+3]
                triplet_mean = sum(ord(char) for char in triplet) / 3
                if triplet_mean > max_triplet_mean:
                    max_triplet_mean = triplet_mean
        else:
            max_triplet_mean = mean_ascii
        
        squared_deviation = (mean_ascii - max_triplet_mean) ** 2
        
        return mean_ascii, max_triplet_mean, squared_deviation
    
    sorted_lines = sorted(lines, key=lambda x: calculate_metrics(x)[2])
    return sorted_lines

print(task13(lines))

print("\nВ порядке увеличение квадратичного отклонения частоты \
встречаемости самого распространенного символа в наборе строк от частоты \
его встречаемости в данной строке.\n")
def task14(lines):
    
    if not lines:
        return []
    
    def find_most_common_char(strings):
        char_freq = {}
        total_chars = 0
        
        for string in strings:
            for char in string:
                char_freq[char] = char_freq.get(char, 0) + 1
                total_chars += 1
        
        if not char_freq:
            return None, 0

        most_common_char = max(char_freq.items(), key=lambda x: x[1])[0]
        overall_frequency = char_freq[most_common_char] / total_chars
        
        return most_common_char, overall_frequency

    most_common_char, overall_freq = find_most_common_char(lines)
    
    if most_common_char is None:
        return lines
    
    print(f"Самый распространенный символ в наборе: '{most_common_char}'")
    print(f"Его общая частота: {overall_freq:.4f}")
    print()

    def calculate_deviation(text):
        if not text:
            return overall_freq ** 2
        
        char_count = text.count(most_common_char)
        string_freq = char_count / len(text)

        deviation = (overall_freq - string_freq) ** 2
        return deviation

    sorted_lines = sorted(lines, key=calculate_deviation)
    return sorted_lines, most_common_char, overall_freq

print(task13(lines))

print("\nTask 15-19\n") #6, 18, 30, 42, 54
print("Выберите задачу: ")
print("\n\n15. Дан целочисленный массив. Необходимо осуществить циклический \
сдвиг элементов массива влево на три позиции. ")
print("\n\n16. Дан целочисленный массив. Необходимо найти элементы, \
расположенные перед первым минимальным. ")
print("\n\n17. Дан целочисленный массив и натуральный индекс (число, меньшее \
размера массива). Необходимо определить является ли элемент по указанному \
индексу локальным максимумом. ")
print("\n\n18. Дан целочисленный массив. Найти все элементы, которые меньше \
среднего арифметического элементов массива. ")
print("\n\n19. Для введенного списка построить список из элементов, \
встречающихся в исходном более трех раз. ")
n = input()

if n == 15:
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = cyclic_shift_left_3(arr)
    print(f"Исходный массив: {arr}")
    print(f"После сдвига влево на 3: {result}")

elif n == 16:
    arr = [5, 3, 8, 1, 9, 1, 4, 2]
    result = elements_before_first_min(arr)
    print(f"Исходный массив: {arr}")
    print(f"Первый минимальный элемент: {min(arr)} (индекс {arr.index(min(arr))})")
    print(f"Элементы перед первым минимальным: {result}")

elif n == 17:
elif n == 18:
elif n == 19:

def cyclic_shift_left_3(arr):
    if len(arr) <= 3:
        return arr

    return arr[3:] + arr[:3]

def elements_before_first_min(arr):
    if not arr:
        return []
    
    min_value = min(arr)
    first_min_index = arr.index(min_value)
    
    if first_min_index == 0:
        return []

    return arr[:first_min_index]

