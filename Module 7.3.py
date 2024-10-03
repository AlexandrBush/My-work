import re

class WordsFinder:
    def __init__(self, *file_names):
        """
        Инициализация класса с переданными именами файлов.
        :param file_names: Переменное количество аргументов с именами файлов.
        """
        self.file_names = file_names

    def get_all_words(self):
        """
        Метод для получения всех слов из файлов.
        :return: Словарь, где ключ - имя файла, значение - список слов в этом файле.
        """
        all_words = {}
        punctuation = r"[',.=!?;:\s\-]"  # Регулярное выражение для удаления пунктуации

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()  # Считываем текст и переводим в нижний регистр
                words = re.split(punctuation, text)  # Разбиваем текст на слова, удаляя пунктуацию
                words = [word for word in words if word]  # Удаляем пустые строки
                all_words[file_name] = words  # Сохраняем слова в словаре

        return all_words

    def find(self, word):
        """
        Метод для поиска первого вхождения слова в каждом файле.
        :param word: Искомое слово.
        :return: Словарь, где ключ - имя файла, значение - позиция первого вхождения слова.
        """
        word = word.lower()  # Переводим искомое слово в нижний регистр
        result = {}

        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word)  # Находим индекс первого вхождения слова

        return result

    def count(self, word):
        """
        Метод для подсчета количества вхождений слова в каждом файле.
        :param word: Искомое слово.
        :return: Словарь, где ключ - имя файла, значение - количество вхождений слова.
        """
        word = word.lower()  # Переводим искомое слово в нижний регистр
        result = {}

        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word)  # Считаем количество вхождений слова

        return result

# Пример использования класса
if __name__ == "__main__":
    finder = WordsFinder('test_file.txt')

    # Получаем все слова из файла
    print(finder.get_all_words())

    # Находим позицию первого вхождения слова 'text'
    print(finder.find('TEXT'))

    # Считаем количество вхождений слова 'text'
    print(finder.count('teXT'))