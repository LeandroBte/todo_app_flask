# Contiene todas las vistas de la autenticacion (maneja la autenticación)

from flask import Blueprint, redirect, url_for, flash, render_template, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from todo.models import User, db
from todo import login_manager

bp = Blueprint('auth', __name__, url_prefix='/auth')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username=username, password=generate_password_hash(password))
        existing_user = User.query.filter_by(username=username).first()
        if existing_user is None:
            db.session.add(user)
            db.session.commit()
            flash('¡Registro exitoso! Por favor inicia sesión.', 'success')
            return redirect(url_for('auth.login'))
        
        flash('El usuario ya existe', 'danger')
        return redirect(url_for('auth.register'))
    
    return render_template('auth/register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('todo.index'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            flash('¡Has iniciado sesión correctamente!', 'success')
            return redirect(next_page or url_for('todo.index'))
        
        flash('Usuario o contraseña incorrectos', 'danger')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/login.html')


# Cerrar sesión
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('auth.login'))
