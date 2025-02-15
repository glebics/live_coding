"""
2. Задача "Поиск подстроки в тексте"
Реализовать функцию поиска всех вхождений подстроки в строку с учетом:
Регистронезависимого поиска
Возможности игнорировать пунктуацию
Поддержки кириллицы и латиницы
Функция должна возвращать список позиций начала каждого вхождения.
"""

from typing import List

test_string = "Генератор текста из набора слов на сайте. Для этого нужно написать список слов, которые должны быть использованы в тексте. Затем указать тему, задать структуру текста и количество символов. Текст из набора слов будет сгенерирован в режиме реального времени."
test_substring = "текст"

def substring_count(text: str, substring: str, punctuation_ignore: bool = True) -> List:
    punctuation_symbols = ".,!?:;"
    text = text.lower()
    substring = substring.lower()
    result = []

    if punctuation_ignore:
        list_without_punctuation = [i for i in text if i not in punctuation_symbols]
        text = "".join(list_without_punctuation)
        print(f"текст без знаков препинания: {text}\n")
    
    word_list = text.split()

    # нужно создать словарь, где будут содержаться слова и их длина – решил сделать по-другому
    # word_lengths = {word: len(word) for word in words}
    # counts_letter_in_words = {word: len(word) for word in word_list}

    for i, c in enumerate(word_list):
        if substring in c:
            print(f"вхождение на элементе {i}")
            substring_entry_index = 0 
            # нужно использовать slice, чтобы узнать первый индекс вхождения
            # i_object[start:stop:step]
            word_list_part = word_list[:i]
            print(f"частичный список, после среза: {word_list_part}, длина: {len(word_list_part)}")
            for word in word_list_part:
                substring_entry_index += len(word)
            substring_entry_index += len(word_list_part) # добавляем индексы пробелов
            # теперь я хочу проверить, с какого символа начинается вхождение при нахождении

            if substring != c:
                add_to_entry_index = int(c.find(substring)) + 1
                substring_entry_index += add_to_entry_index

                # full_word_letters = list(c) # ["т", "е", "к", "с", "т", "a"]
                # substring_letters = list(substring) # ["т", "е", "к", "с", "т"]
                # list_of_coincidence = []
                # # я пытаюсь сравнить поэлементно два списка
                # for index_letter_substring, letter_1 in enumerate(substring_letters):
                #     for index_letter_string, letter_2 in enumerate(full_word_letters):
                #         # как сравнить не только текущие буквы, но и рядом стоящие вместе?
                #         if letter_1 == letter_2:
                #             list_of_coincidence.append(letter_1)

                        # здесь нужно добавить код вхождения

            # может есть вариант совместить два списка, и индексом будет разница между объединенным
            # списком и искомым. – не сработает, потому что может учитываться разница с конца, а не только с начала

            try: # избегаем повторяющихся индексов
                result.append(substring_entry_index)
                print(f"добавлен индекс {substring_entry_index}")
            except:
                pass

    print(f"\ntest_string: {text}")
    print(f"\ntest_substring: {substring}\n")

    return result

print(substring_count(test_string, test_substring, True))
