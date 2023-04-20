import sqlite3


num_to_month = {'1': 'января',
                '2': 'февраля',
                '3': 'марта',
                '4': 'апреля',
                '5': 'мая',
                '6': 'июня',
                '7': 'июля',
                '8': 'августа',
                '9': 'сентября',
                '10': 'октября',
                '11': 'ноября',
                '12': 'декабря'}


def get_db_connection():
    return sqlite3.connect('sqlite_python.db')


def sql_exec(sql):
    try:
        sqlite_connection = get_db_connection()
        cursor = sqlite_connection.cursor()
        cursor.execute(sql)
        record = cursor.fetchall()
        return record
    except sqlite3.Error as error:
        print("SQLite Connection Error", error)
    finally:
        if(cursor):
            cursor.close()
        if (sqlite_connection):
            sqlite_connection.close()
            print("SQLite Connection is closed")


def get_user_birthdays(user_id: int):
    get_birthdays_query = f"""
    SELECT name, day, month, year
    FROM users
    WHERE user_id = {user_id}
    """
    record = sql_exec(get_birthdays_query)
    if record:
        result = "Содержатся следующие записи:\n"
        for row in record:
            name = row[0]
            day = row[1]
            month = row[2]
            year = row[3]
            if year:
                birthday = day + " " + num_to_month[month] + " " + year
            else:
                birthday = day + " " + num_to_month[month]
            result += name + " - " + birthday + "\n"
    else:
        result = "Не содержится никаких записей"

    return result
