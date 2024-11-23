import sqlite3

def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Создание таблицы Products, если она не существует
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL,
        image TEXT
    )
    ''')

    # Проверка на наличие записей в таблице Products
    cursor.execute('SELECT COUNT(*) FROM Products')
    count = cursor.fetchone()[0]

    if count == 0:
        # Вставка данных в таблицу Products, если она пуста
        cursor.execute('''
        INSERT INTO Products (title, description, price, image) VALUES
        ('Витамины', 'B 12', 100, 'https://via.placeholder.com/150'),
        ('Минералы', 'Кальций, Магний', 200, 'https://via.placeholder.com/150'),
        ('Слабительное', 'Помощь при запоре', 300, 'https://via.placeholder.com/150'),
        ('Активированный уголь', 'Помощь при отравлении', 400, 'https://via.placeholder.com/150')
        ''')

    # Создание таблицы Users, если она не существует
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return [{'id': product[0], 'title': product[1], 'description': product[2], 'price': product[3], 'image': product[4]} for product in products]

def add_user(username, email, age):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Добавление нового пользователя с балансом 1000
    cursor.execute('''
    INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)
    ''', (username, email, age))

    conn.commit()
    conn.close()

def is_included(username):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Проверка наличия пользователя в таблице Users
    cursor.execute('SELECT EXISTS(SELECT 1 FROM Users WHERE username = ?)', (username,))
    result = cursor.fetchone()[0]

    conn.close()
    return bool(result)