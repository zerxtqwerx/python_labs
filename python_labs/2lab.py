def count_unique_words():
    n = int(input().strip())
    
    words_set = set()

    for _ in range(n):
        line = input().strip()
        words = line.split()
        for word in words:
            clean_word = word.strip('.,;!?\'"()-:').lower()
            if clean_word:
                words_set.add(clean_word)
    
    return len(words_set)


def frequency_analysis():
    n = int(input().strip())

    word_count = {}

    for _ in range(n):
        line = input().strip()

        words = line.split()

        for word in words:
            word_lower = word.lower()
            word_count[word_lower] = word_count.get(word_lower, 0) + 1

    return word_count


def sort_words_by_frequency(word_count):
    frequency_list = []
    for word, count in word_count.items():
        frequency_list.append((count, word))

    sorted_list = sorted(frequency_list, key=lambda x: (-x[0], x[1]))

    return [word for count, word in sorted_list]

if __name__ == "__main__":
    print("Task 1")
    result = count_unique_words()
    print(result)

    print("Task 2")
    word_count = frequency_analysis()
    sorted_words = sort_words_by_frequency(word_count)

    for word in sorted_words:
        print(word)

