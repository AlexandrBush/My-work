import time
from multiprocessing import Pool
import os

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data

def main():
    # Выводим текущую директорию для проверки
    print(f"Текущая директория: {os.getcwd()}")

    # Список файлов в текущей директории
    filenames = [f'File {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f"Линейный вызов: {linear_time:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocess_time = time.time() - start_time
    print(f"Многопроцессный вызов: {multiprocess_time:.6f} секунд")

if __name__ == '__main__':
    main()