import functools
from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.exc import SQLAlchemyError
from my_blog.models.user import User   
from my_blog import db 

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username:
            error = 'Se requiere un nombre de usuario.'
        elif not password:
            error = 'Se requiere una contraseña.'
        else:
            try:
                # Verificar la existencia del usuario
                user = User.query.filter_by(username=username).first()

                if user:
                    error = f'El usuario {username} ya está registrado.'
                    flash(error)
                else:
                    # Crear y agregar el nuevo usuario
                    new_user = User(username, generate_password_hash(password))
                    db.session.add(new_user)
                    db.session.commit()
                    return redirect(url_for('auth.login'))

            except SQLAlchemyError as e:
                flash('Error en la base de datos al registrar el usuario.')

    return render_template('auth/register.html')

@auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        error = None

        user = User.query.filter_by(username=username).first()
        
        if user is None:
            error = 'Nombre de usuario incorrecto.'
        elif not check_password_hash(user.password, password):
            error = 'Contraseña incorrecta.'
        
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('blog.index'))
        
        flash(error)

    return render_template('auth/login.html')

@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    g.user = User.query.get(user_id) if user_id else None

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('blog.index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
