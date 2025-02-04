import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users(
# id INTEGER PRIMARY KEY,
# username TEXT NOT NULL,
# email TEXT NOT NULL,
# age INTEGER,
# balance INTEGER NOT NULL
# )
# ''')
# for i in range (30):
#     cursor.execute(' INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i+1}', f'example{i+1}@gmail.com', int(10*(i+1)), 1000))
#
# for i in range (30):
#     if i % 2 == 0:
#         pass
#     else:
#         cursor.execute('UPDATE Users SET balance= ? WHERE id = ?', (500, int(i)))
#
# for i in range (30):
#     if (i+2) % 3 == 0:
#         cursor.execute('DELETE FROM Users WHERE id = ?', (i,))
#
# cursor.execute('SELECT * FROM Users WHERE age <> ?', (60,))
#
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT(*) FROM Users')
count = cursor.fetchone()[0]
# print(count)
cursor.execute('SELECT SUM(balance) FROM Users')
sum_bal = cursor.fetchone()[0]
# print(sum_bal)
print(sum_bal / count)


connection.commit()
connection.close()

