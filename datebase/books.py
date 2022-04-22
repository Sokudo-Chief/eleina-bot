import sqlite3

# ================================== Удаление записи ====================================

def delete(id):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_delete_query = "DELETE FROM books WHERE id=?;"
        cursor.execute(sqlite_delete_query, (id,))
        sqlite_connection.commit()
        print("Запись", id, "успешна удалена.")
        cursor.close()
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# ==================================  ====================================

def selectBooks(book: tuple):
    try:
        sqlite_connection = sqlite3.connect("library.db")
        cursor = sqlite_connection.cursor()

        select_query = '''SELECT id, vis_name, surname, adress, book_id FROM books'''

        cursor.execute(select_query, (book[0][0],))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("При выполнении возникла ошибка:", error)
    finally:
        if sqlite_connection:
            cursor.close()

# ================================== Создание таблицы ====================================

def createTable():
    try:
        sqlite_connection = sqlite3.connect("library.db")
        cursor = sqlite_connection.cursor()
        print("База данных успешно подключена.")

        create_table = '''CREATE TABLE books (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            author TEXT NOT NULL,
                            toms INTEGER NOT NULL);'''
        cursor.execute(create_table)
        sqlite_connection.commit()
        print("Таблица создана.")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQLite:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")

# ================================== Вывод по айди ====================================

def recordID(id):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM books WHERE id=?;"
        cursor.execute(sqlite_selection_query, (id,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Вывод по автору ====================================

def recordAuthor(author):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * FROM books WHERE author=?;"
        cursor.execute(sqlite_selection_query, (author,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# ================================== Вывод по кол. томов ====================================

def recordToms(toms):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * FROM books WHERE toms=?;"
        cursor.execute(sqlite_selection_query, (toms,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
            
# ================================== Вывод по имени ====================================

def recordName(name):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * FROM books WHERE name=?;"
        cursor.execute(sqlite_selection_query, (name,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# ================================== Вставка ====================================

def insert(records):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()
        print('База данных подключена.')

        insert_query = '''INSERT INTO books (id, name, author, toms)
                            VALUES (?, ?, ?, ?);'''           

        cursor.execute(insert_query, records)
        sqlite_connection.commit()
        print('Запись успешно добавлена.')
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# ================================== Вывод таблицы ====================================

def SelectTable():
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * From books;"
        cursor.execute(sqlite_selection_query)
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# ================================== Айди ====================================

def maxID():
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT MAX(id) FROM books;"
        cursor.execute(sqlite_selection_query)
        records = cursor.fetchone()
        cursor.close()
        return records[0]
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# ================================== Вывод ====================================

def printB(records):
    try:
        for record in records:
            print()
            print("Name:", record[1])
            print("Author:", record[2])
            print("Toms:", record[3])
    except sqlite3.Error as error:
        print("Ничего не выбрано!") 

# ================================== Вывод по автору ====================================

def recordAuthor(author):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()
        print('База данных подкючена.')

        sqlite_selection_query = "SELECT * From books WHERE author=?Max;"
        cursor.execute(sqlite_selection_query, (author,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# ================================== Вывод всей таблицы ====================================

def SelectTable():
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM books;"
        cursor.execute(sqlite_selection_query)
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Изменение данных ====================================

def update(id, name, author, toms):
    try:
        sqlite_connection = sqlite3.connect("library.db")
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "UPDATE books SET name=?, author=?, toms=? WHERE id=?;"
        cursor.execute(sqlite_selection_query, (name, author, toms, id))
        sqlite_connection.commit()
        print("Запись", id, "успешна обновлена.")
        cursor.close
        
    except sqlite3.Error as error:
        print("Не удалось изменить данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Книги ====================================

books = [(1, 'Liver', 'Sokolov', 5),
       (2, 'Toxic', 'Sokolov', 2),
       (3, 'Friendly', 'Sokolov', 1),
       (4, 'PC', 'Max', 3),
       (5, 'Micro', 'Max', 6),
       (6, 'Adom', 'Maximov', 8),
       (7, 'Picture', 'Maximov', 8),
       (8, 'Home', 'Popusk', 4),
       (9, 'Sun', 'Popusk', 1),
       (10, 'Bihand', 'Point', 7),
       (11, 'Table', 'Point', 9),
       (12, 'About me', 'Nitro', 2),
       (13, 'Window', 'Nitro', 1),
       (14, 'Door', 'Cooler', 1),
       (15, 'Okey, go!', 'Cooler', 6),]

# insert(books)