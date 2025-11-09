from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    
    # Configuraciones del proyecto
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todolist.db"
    
    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    
    # Importar y registrar blueprints
    from .todo import bp as todo_bp
    from .auth import bp as auth_bp
    
    app.register_blueprint(todo_bp)
    app.register_blueprint(auth_bp)
    
    @app.route('/')
    def index():
        if current_user.is_authenticated:
            return redirect(url_for('todo.index'))
        return render_template('index.html')
    
    # Migrar la base de datos
    with app.app_context():
        db.create_all()
    
    return app
    



