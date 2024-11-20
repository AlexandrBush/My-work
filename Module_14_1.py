import sqlite3

# Подключаемся к базе данных (или создаем её, если она не существует)
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

# Создаем таблицу Users, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Создаем индекс на столбце email, если он не существует
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Заполняем таблицу 10 записями
for i in range(1, 11):  # Используем диапазон от 1 до 10 включительно
    username = f"User{i}"
    email = f"example{i}@gmail.com"
    age = i * 10  # Возраст увеличивается на 10 для каждого пользователя
    balance = 1000 if i % 2 == 0 else 500  # Баланс 1000 для четных, 500 для нечетных

    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, balance))

# Удаляем каждую третью запись, начиная с первой
for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

# Фиксируем транзакцию
connection.commit()

# Делаем выборку всех записей, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")

# Получаем все результаты
results = cursor.fetchall()

# Выводим результаты в консоль в указанном формате
for row in results:
    username, email, age, balance = row
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# Закрываем соединение
connection.close()