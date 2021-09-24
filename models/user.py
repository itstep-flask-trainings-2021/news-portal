from config import mysql
from werkzeug.security import check_password_hash


class User(object):

    @staticmethod
    def register(login: str, password: str, email: str, regdate: str, status: str) -> list:
        connection = mysql.get_db()
        cursor = connection.cursor()  # создаем курсор - итератор внутри базы данных
        sql_query = """
            insert into users (login, password, email, regdate, status)
            values (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql_query, (login, password, email, regdate, status))
        connection.commit()
        cursor.close()
        connection.close()

    # толко модель выполняет запросы
    @staticmethod
    def auth(login, password) -> list:
        print(password)
        connection = mysql.get_db()
        cursor = connection.cursor()
        sql_query = """
        select login, password from users 
        where login=%s
        """
        cursor.execute(sql_query, (login))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        if len(result) == 1:
            return check_password_hash(result[0][1], password)
        else:
            return False
    # select by user and password
