def count_unique_words():
    # Читаем количество строк
    n = int(input().strip())
    
    words_set = set()
    
    # Читаем n строк
    for _ in range(n):
        line = input().strip()
        
        # Разбиваем строку на слова, игнорируя пробелы и символы конца строки
        words = line.split()
        
        # Обрабатываем каждое слово
        for word in words:
            # Убираем знаки препинания в начале и конце слова
            clean_word = word.strip('.,;!?\'"()-:').lower()
            
            # Если слово не пустое после очистки, добавляем в множество
            if clean_word:
                words_set.add(clean_word)
    
    return len(words_set)

# Запускаем программу
if __name__ == "__main__":
    result = count_unique_words()
    print(result)