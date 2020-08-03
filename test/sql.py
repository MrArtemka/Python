import sqlite3

conn = sqlite3.connect("test.sqlite")
cursor = conn.cursor()

cursor.execute('''
                SELECT id, name, email
                FROM user
                ''')

conn.commit()

result = cursor.fetchall()
print(result)

cursor.close()