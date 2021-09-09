# загрузка типовых страниц сайта
from flask import render_template
from config import app
# контроллер запускает процесс прорисовки страницы в браузере


class NewsController(object):

    # метод для загрузки шаблона главной страницы
    @staticmethod
    @app.route('/news/create')
    def create():
        return render_template('news/create.html')

    @staticmethod
    @app.route('/news/delete')
    def delete():
        return render_template('news/delete.html')

    @staticmethod
    @app.route('/news/details')
    def details():
        return render_template('news/details.html')

    @staticmethod
    @app.route('/news/list')
    def list():
        return render_template('news/list.html')

    @staticmethod
    @app.route('/news/update')
    def update():
        return render_template('news/update.html')
