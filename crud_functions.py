import sqlite3

def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL,
        image TEXT
    )
    ''')

    # Проверка на наличие записей в таблице
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

    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return [{'id': product[0], 'title': product[1], 'description': product[2], 'price': product[3], 'image': product[4]} for product in products]