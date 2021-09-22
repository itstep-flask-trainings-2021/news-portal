# загрузка типовых страниц сайта
from flask import render_template, session, request
from config import app
# контроллер запускает процесс прорисовки страницы в браузере


class NewsController(object):

    # метод для загрузки шаблона главной страницы
    @staticmethod
    @app.route('/news/create', methods=['GET', 'POST'])
    def create():
        if 'user' in session and session['user'] == 'petya':
            if request.method == 'GET':
                return render_template('news/create.html')
            elif request.method == 'POST':
                message = 'Добавить новость не удалось'
                mess_color='red'
                return render_template('news/create_info.html', context={
                    'message': message,
                    'mess_color': mess_color
                })
        else:
            return render_template('access/page403.html')

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
