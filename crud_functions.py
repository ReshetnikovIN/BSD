import sqlite3


def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')



    cursor.execute('INSERT INTO Products (id, title, description, price) VALUES(?, ?, ?, ?)', (1, 'Продукт 1', 'Описание 1', 100))
    cursor.execute('INSERT INTO Products (id, title, description, price) VALUES(?, ?, ?, ?)', (2, 'Продукт 2', 'Описание 1', 200))
    cursor.execute('INSERT INTO Products (id, title, description, price) VALUES(?, ?, ?, ?)', (3, 'Продукт 3', 'Описание 1', 300))
    cursor.execute('INSERT INTO Products (id, title, description, price) VALUES(?, ?, ?, ?)', (4, 'Продукт 4', 'Описание 1', 400))
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    prod = cursor.fetchall()
    # print(prod)
    # print(prod[0])
    # print(prod[0][0])
    return prod

# initiate_db()
# get_all_products()