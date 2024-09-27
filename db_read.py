import sqlite3

def fetch_users():
    # Подключаемся к базе данных
    connection = sqlite3.connect('school_data.db')
    cursor = connection.cursor()

    try:
        # Выполняем SQL-запрос для получения всех данных из таблицы users
        cursor.execute("SELECT * FROM users")

        # Получаем все строки результата запроса
        rows = cursor.fetchall()

        # Печатаем каждую строку
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        # Закрываем соединение с базой данных
        connection.close()


# Вызываем функцию для выполнения кода
fetch_users()