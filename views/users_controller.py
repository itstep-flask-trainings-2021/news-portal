# загрузка типовых страниц сайта
from flask import render_template, request, session, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from time import strftime
from config import app
from models.user import User
# контроллер запускает процесс прорисовки страницы в браузере


class UsersController(object):

    # метод для загрузки шаблона главной страницы
    @staticmethod
    @app.route('/users')
    def admin():
        return render_template('users/admin.html')

    @staticmethod
    @app.route('/users/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('users/login.html')
        elif request.method == 'POST':
            message = 'Авторизация провалена'
            mess_color='red'

            login = request.form.get('login');
            pass1 = request.form.get('pass1');
            rem = request.form.get('rem');
            
            # транзитный словарь
            if User.auth(login, pass1) == True:
                session['user'] = login # Регистрация пользователя в сессии - сессия доступна для всех страниц приложения
                # сессия - это супер глобальный словарь
                # сохраняется в памяти сервера - в потоке выполнения
                if rem == 'yes':
                    response = make_response('setting coockie user') # любое сообщение, необходимо для отладки
                    response.set_cookie('user', login, max_age=7*24*3600)
                message = 'Вы успешно авторизованы!'
                mess_color='green'
            else:
                message = 'Пользователь не найден'
            return render_template('users/login_info.html', context={
                'message': message,
                'mess_color': mess_color
            })

    @staticmethod
    @app.route('/users/logout')
    def logout():
        session.pop('user', None)
        return render_template('users/logout.html')

    @staticmethod
    @app.route('/users/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'GET':
            return render_template('users/register.html')
        elif request.method == 'POST':
            message = 'Регистрация провалена'
            mess_color='red'

            login = request.form.get('login');
            pass1 = request.form.get('pass1');
            pass2 = request.form.get('pass2');
            email = request.form.get('email');
            
            password = generate_password_hash(pass1)
            regdate = strftime('%Y-%m-%d %H:%M:%S')
            status = "new_user"
            # транзитный словарь
            User.register(login, password, email, regdate, status)
            message = 'Вы успешно зарегистрированы!'
            mess_color='green'
            return render_template('users/register_info.html', context={
                'message': message,
                'mess_color': mess_color
            })


    @staticmethod
    @app.route('/users/profile')
    def profile():
        return render_template('users/profile.html')
