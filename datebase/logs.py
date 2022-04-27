import sqlite3
from datebase import visitors as v
from datebase import books as b

# ================================== Айди ====================================

def maxID():
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "SELECT MAX(id) FROM logs;"
        cursor.execute(sqlite_selection_query)
        record = cursor.fetchone()
        cursor.close()
        if record[0] == None:
            return 1
        return record[0]
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Добавление книги ====================================

def delete(id):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        insert_query = "DELETE FROM logs WHERE id=?;"
        cursor.execute(insert_query, (id,))
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Добавление книги ====================================

def addBook(book_id: tuple, visitor_number: tuple):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        insert_query = "INSERT INTO logs (id, book_id, visitor_number) VALUES (?, ?, ?);"
        cursor.execute(insert_query, (maxID()+1, book_id[0][0], visitor_number[0][0]))
        sqlite_connection.commit()
        cursor.close()
        # print("Книга", book_id[1], "для посетителя", visitor_number[0][1], "успешна добавлена.")
        print("Книга добавлена к посетителю")
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Вывод ====================================

def SelectTable():
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        selection_query = "SELECT * FROM logs;"
        cursor.execute(selection_query)
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# ================================== Вывод ====================================

def selectLogs(visitor: tuple):
    try:
        sqlite_connection = sqlite3.connect("library.db")
        cursor = sqlite_connection.cursor()

        select_query = '''SELECT number, vis_name, surname, adress, book_id FROM logs JOIN visitors 
                          ON visitors.number = logs.visitor_number
                          WHERE visitor_number = ?'''

        cursor.execute(select_query, (visitor[0][0],))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("При выполнении возникла ошибка:", error)
    finally:
        if sqlite_connection:
            cursor.close()

# ================================== Редактирование ====================================

def UpdateRecord(id,book,visitor):
    try:
        sqlite_connection = sqlite3.connect('library.db')
        cursor = sqlite_connection.cursor()

        sqlite_selection_query = "UPDATE logs SET book_id=?, visitor_number=? WHERE id=?;"
        cursor.execute(sqlite_selection_query,(book,visitor,id))
        sqlite_connection.commit()
        print('Запись', id, 'успешно обновленна')
    except sqlite3.Error as error:
        print(error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# UpdateRecord(19, 10, 111)
# print(SelectTable())
# print(selectLogs(v.recordNumber(333)))