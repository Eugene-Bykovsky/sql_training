import sqlite3


def execute_query(db_file, query, data=None):
    """
    Функция для выполнения запроса к базе данных.
    Принимает имя файла базы данных, SQL-запрос и опциональные данные для вставки.
    """
    try:
        connection = sqlite3.connect(db_file, isolation_level='EXCLUSIVE')
        cursor = connection.cursor()

        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)

        connection.commit()

        return connection, cursor

    except sqlite3.Error as e:
        print("Ошибка при выполнении запроса:", e)


def add_student(db_file, student_name, group, course, age):
    """
    Функция для добавления нового студента в базу данных.
    """

    # Здесь тебе нужно написать SQL-запрос для вставки данных о новом
    # студенте в таблицу students
    query = '''INSERT INTO students (student_name, group_number, course, age) 
                VALUES (?, ?, ?, ?)'''
    data = (student_name, group, course, age)

    connection, cursor = execute_query(db_file, query, data)
    connection.close()
    print("Новый студент успешно добавлен в таблицу.")


def update_student(db_file, id, new_group, new_course, new_age):
    """
    Функция для обновления информации о существующем студенте.
    """

    # Здесь тебе нужно написать SQL-запрос для обновления информации о
    # студенте с указанным id
    query = '''UPDATE students
                SET group_number = ?, course = ?, age = ?
                WHERE id = ?'''
    data = (new_group, new_course, new_age, id)

    connection, cursor = execute_query(db_file, query, data)
    connection.close()
    print("Информация о студенте успешно обновлена.")


def delete_student(db_file, id):
    """
    Функция для удаления записи о студенте из базы данных.
    """

    # Здесь тебе нужно написать SQL-запрос для удаления записи о студенте с
    # указанным id
    query = '''DELETE FROM students WHERE id = ? '''
    data = (id,)

    connection, cursor = execute_query(db_file, query, data)
    connection.close()
    print("Запись о студенте успешно удалена.")


def get_students_sorted_by_name(db_file):
    """
    Функция для получения списка всех студентов, отсортированных по имени.
    """
    # Здесь тебе нужно написать SQL-запрос для выборки всех студентов из
    # таблицы students и сортировки их по имени
    query = '''SELECT * FROM students ORDER BY student_name ASC'''
    connection, cursor = execute_query(db_file, query)

    rows = cursor.fetchall()
    connection.close()  # Close connection after fetching results

    for row in rows:
        print(row)


# Пример использования
if __name__ == "__main__":
    db_file = 'sqlite3.db'

    # Добавление нового студента
    add_student(db_file, 'Илон Маск', 9, 'python-ai', 42)

    # Обновление информации о существующем студенте
    # update_student(db_file, 15, 999, 'superweb', 180)

    # Удаление записи о студенте
    # delete_student(db_file, 30)

    # Вывод списка всех студентов в алфавитном порядке по имени
    # get_students_sorted_by_name(db_file)
