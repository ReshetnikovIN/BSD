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

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    growth INT NOT NULL,
    weight INT NOT NULL,
    gender TEXT NOT NULL,
    calories INT,
    balance INT NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

def add_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

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
    return prod

def add_user(username, userpass):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Users (username, password, email, age, growth, weight, gender, calories, balance) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', (username, userpass, '', 0, 0, 0, '', 0, 1000))

    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Users WHERE   USERNAME = ?', (username, ))
    user = cursor.fetchone()
    try:
        if user[0] > 0:
            username = user[1]
            password = user[2]
            email= user[3]
            age = user[4]
            growth = user[5]
            weight = user[6]
            gender = user[7]
            calories = user[8]
            balance = user[9]
            user_char = [username, password, email, age, growth, weight, gender, calories, balance]
        else:
            user_char = ['', '', '', 0, 0, 0, '', 0, 0]
    except:
        user_char = ['', '', '', 0, 0, 0, '', 0, 0]
    connection.commit()
    connection.close()

    return user_char

def get_user(username):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE   USERNAME = ?', (username, ))
    user = cursor.fetchone()
    try:
        if user[1] == username:
            username = user[1]
            password = user[2]
            email = user[3]
            age = user[4]
            growth = user[5]
            weight = user[6]
            gender = user[7]
            calories = user[8]
            balance = user[9]
        else:
            user_exist = False
    except:
        password = ''
        email = ''
        age = 0
        growth = 0
        weight = 0
        gender = ''
        calories = 0
        balance = 0
    connection.commit()
    connection.close()

    return (username, password, email, age, growth, weight, gender, calories, balance)

def update_user(username, password, email, age, growth, weight, gender, calories, balance):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM Users WHERE   USERNAME = ?', (username, ))
        if cursor.fetchone()[0] > 0:
            cursor.execute('UPDATE Users SET  password = ?, email = ?, age = ?, growth = ?, weight = ?, gender = ?, calories = ?, balance = ? WHERE username = ?', (password, email, age, growth, weight, gender, calories, balance, username))
            user_exist = True
            connection.commit()
            connection.close()
        else:
            user_exist = False
    except:
        pass

    return (username, password, email, age, growth, weight, gender, calories, balance)


# initiate_db()
# get_all_products()

# initiate_db()
# username = 'User_1'
# email = 'user_1@mail.ru'
# age = 99
# growth = 0 #299
# weight = 0 #399
# calories = 0
# balance = 1000
# add_user(username, email, age, growth, weight, calories, balance)

# username = 'User_1'
# # email = ''
# # age = 0
# # calories = 0
# # balance = 0
# res = is_included(username)
# print(res)
# print(f'username - {res[0]}, email - {res[1]}, age -{res[2]}, growth -{res[3]}, weight -{res[4]}, calories - {res[5]}, balance - {res[6]}')