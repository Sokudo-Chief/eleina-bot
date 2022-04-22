import sqlite3

# ================================== Создание таблицы ====================================

def createTable():
    try:
        sqlite_connection = sqlite3.connect("visitors.db")
        cursor = sqlite_connection.cursor()
        print("База данных успешно подключена.")

        create_table = '''CREATE TABLE visitors (
                            ID INTEGER PRIMARY KEY,
                            number INTEGER NOT NULL,
                            name TEXT NOT NULL,
                            surname TEXT NOT NULL,
                            adress TEXT NOT NULL);'''
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

# ================================== Вставка ====================================

def insert(records):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()
        print('База данных подключена.')

        insert_query = '''INSERT INTO visitors (number, vis_name, surname, adress)
                            VALUES (?, ?, ?, ?);'''              
        cursor.executemany(insert_query, records)
        sqlite_connection.commit()
        print('Запись успешно добавлена.')
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# ================================== Создание посетителя ====================================

def makingRecords():
    records = []
    while True:
        records.append((
            maxID() + 1,
            int(input('Номер: ')),
            input('Имя: '),
            input('Фамилия: '),
            input('Адресс: ')
        ))
        question = input('Выйти? y/n: ')
        if question == 'y':
            return records

# ================================== Вывод ====================================

def printV(visitors):
    try:
        for visitor in visitors:
            print()
            print("ID:", visitor[0])
            print("number:", visitor[1])
            print("name:", visitor[2])
            print("surname:", visitor[3])
            print("Adress:", visitor[4])
    except sqlite3.Error as error:
        print("Ничего не выбрано!")  

# ================================== Айди ====================================

def maxID():
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT MAX(id) FROM visitors;"
        cursor.execute(sqlite_selection_query)
        record = cursor.fetchone()
        cursor.close()
        return record[0]
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# ================================== Вывод по id ====================================

def recordNumber(number):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM visitors WHERE number=?;"
        cursor.execute(sqlite_selection_query, number)
        record = cursor.fetchone()
        cursor.close()
        return record[0][0]
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Вывод по имени ====================================

def recordName(name):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM visitors WHERE name=?;"
        cursor.execute(sqlite_selection_query, (name,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Вывод по фамилии ====================================

def recordSurname(surname):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM visitors WHERE surname=?;"
        cursor.execute(sqlite_selection_query, (surname,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Вывод по адресу ====================================

def recordAdress(adress):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM visitors WHERE adress=?;"
        cursor.execute(sqlite_selection_query, (adress,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Вывод по номеру ====================================

def recordNumber(number):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM visitors WHERE number=?;"
        cursor.execute(sqlite_selection_query, (number,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Удаление ====================================

def delete(num):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_delete_query = "DELETE FROM visitors WHERE number=?;"
        cursor.execute(sqlite_delete_query, (num,))
        sqlite_connection.commit()
        print("Запись", num, "успешна удалена.")
        cursor.close()
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# ================================== Изменение номера ====================================

def updateNumber(number, new_number):
    try:
        sqlite_connection = sqlite3.connect("library.db")
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "UPDATE visitors SET number=? WHERE number=?;"
        cursor.execute(sqlite_selection_query, (number, new_number))
        sqlite_connection.commit()
        print("Запись", id, "успешна обновлена.")
        cursor.close
        
    except sqlite3.Error as error:
        print("Не удалось изменить данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Изменение имени ====================================

def updateName(name, id):
    try:
        sqlite_connection = sqlite3.connect("library.db")
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "UPDATE visitors SET name=? WHERE ID=?;"
        cursor.execute(sqlite_selection_query, (name, id))
        sqlite_connection.commit()
        print("Запись", id, "успешна обновлена.")
        cursor.close
    except sqlite3.Error as error:
        print("Не удалось изменить данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Изменение фамилии ====================================

def updateSurname(surname, id):
    try:
        sqlite_connection = sqlite3.connect("library.db")
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "UPDATE visitors SET surname=? WHERE ID=?;"
        cursor.execute(sqlite_selection_query, (surname, id))
        sqlite_connection.commit()
        print("Запись", id, "успешна обновлена.")
        cursor.close

    except sqlite3.Error as error:
        print("Не удалось изменить данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Изменение адреса ====================================

def updateAdress(adress, id):
    try:
        sqlite_connection = sqlite3.connect("library.db")
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "UPDATE visitors SET adress=? WHERE ID=?;"
        cursor.execute(sqlite_selection_query, (adress, id))
        sqlite_connection.commit()
        print("Запись", id, "успешна обновлена.")
        cursor.close
        
    except sqlite3.Error as error:
        print("Не удалось изменить данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Изменение данных ====================================

def update(number, vis_name, surname, adress):
    try:
        sqlite_connection = sqlite3.connect("library.db")
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "UPDATE visitors SET vis_name=?, surname=?, adress=? WHERE number=?;"
        cursor.execute(sqlite_selection_query, (vis_name, surname, adress, number))
        sqlite_connection.commit()
        print("Запись", number, "успешна обновлена.")
        cursor.close
        
    except sqlite3.Error as error:
        print("Не удалось изменить данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Вывод всей таблицы ====================================

def SelectTable():
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT * FROM visitors;"
        cursor.execute(sqlite_selection_query)
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Посетители ====================================

Visi  = [(111, 'Роберт', 'Д.', 'Ряб'),
       (222, 'Рин', 'Ш.', 'Мах'),
       (333, 'Вика', 'Х.', 'Вул'),
       (444, 'Джон', 'Ч.', 'Кос'),
       (555, 'Диана', 'З.', 'Жоп'),
       (2280, 'Артём', 'Я.', 'Кав'),
       (777, 'Никита', 'Ш.', 'Гриб'),
       (888, 'Марк', 'О.', 'Пол'),
       (999, 'Натан', 'А.', 'Мос'),
       (1010, 'Егор', 'М.', 'Под'),
       (1111, 'Ден', 'С.', 'Хз'),
       (1212, 'Чиф', 'М.', 'Кос'),
       (1313, 'Люк', 'С.', 'Кос'),
       (1414, 'Леви', 'А.', 'Пар'),
       (1515, 'Давид', 'Х.', 'Хз'),]

# insert(Visi)