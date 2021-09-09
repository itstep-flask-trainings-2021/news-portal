# загрузка типовых страниц сайта
from flask import render_template
from config import app
# контроллер запускает процесс прорисовки страницы в браузере


class UsersController(object):

    # метод для загрузки шаблона главной страницы
    @staticmethod
    @app.route('/users')
    def admin():
        return render_template('users/admin.html')

    @staticmethod
    @app.route('/users/login')
    def login():
        return render_template('users/login.html')

    @staticmethod
    @app.route('/users/logout')
    def logout():
        return render_template('users/logout.html')

    @staticmethod
    @app.route('/users/register')
    def register():
        return render_template('users/register.html')

    @staticmethod
    @app.route('/users/profile')
    def profile():
        return render_template('users/profile.html')
