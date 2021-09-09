# загрузка типовых страниц сайта 
from flask import render_template
from config import app
# контроллер запускает процесс прорисовки страницы в браузере

class HomeController(object):

    # метод для загрузки шаблона главной страницы
    @staticmethod
    @app.route('/') # указывает, какое представление и когда должно вызываться
    def index():
        return render_template('home/index.html')


    # метод для загрузки шаблона страницы про сайт
    @staticmethod
    @app.route('/about')
    def about():
        return render_template('home/about.html')


        # метод для загрузки шаблона главной страницы
    @staticmethod
    @app.route('/contacts')
    def contacts():
        return render_template('home/contacts.html')