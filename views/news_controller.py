# загрузка типовых страниц сайта
from os import path

from config import app
from flask import render_template, request, session
from models.article import Article
from werkzeug.utils import secure_filename
from time import localtime, strftime

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
                title = request.form.get('title')
                about = request.form.get('about')
                content = request.form.get('content')
                status = request.form.get('status')

                file = request.files.get('image')
                filename = secure_filename(file.filename)
                extentions = ['png', 'jpg', 'jpeg', 'gif', 'bmp']
                size_limit = 10 * 1024 * 1024  # 10Mb

                if filename.split('.')[-1] not in extentions:
                    message = 'Файл не графического формата!'
                    mess_color = 'red'
                elif len(file.read()) > size_limit:
                    message = 'Файл больше 10Mb'
                    mess_color = 'red'
                else:
                    local_dir = path.dirname(path.abspath(__file__))
                    # по какому абсолютному пути мы находимся на сервере- news_controller
                    root_dir = path.abspath(local_dir + '\\..\\')
                    save_dir = root_dir + '\\static\\upload'
                    save_path = path.join(save_dir, filename)
                    file.stream.seek(0)
                    # в файловом потоке находим первій байт сохраняемого файла
                    file.save(save_path)

                    image = f'/upload/{filename}'
                    user_id = 9
                    publish = strftime('%Y-%m-%d %H:%M:%S', localtime())
                    Article.add_article(title, about, content, image, publish, user_id, status)
                    
                    message = 'Новость успешно добавлена'
                    message == 'Новость успешно добавлена'
                    mess_color = 'green'

                return render_template('news/create_info.html', context={
                    'message': message,
                    'mess_color': mess_color
                })
                # поле name в форме прикрепляет к введенным данным ключ и отправляет в виде словаря на сервер
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
        all_news = Article.get_all_articles()
        return render_template('news/list.html', context={
            'all_news': all_news
        })

    @staticmethod
    @app.route('/news/update')
    def update():
        return render_template('news/update.html')
