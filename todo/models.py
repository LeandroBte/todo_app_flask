# Contiene los modelos de la base de datos (maneja la base de datos)
from datetime import datetime
from todo import db, login_manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    todos = db.relationship('Todo', backref='author', lazy=True)
    
    def get_id(self):
        return str(self.id)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'

    def __str__(self):
        return self.username


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    state = db.Column(db.Boolean, nullable=False, default=False)
    
    
    def __init__(self, title, description, created_by, state=False):
        self.title = title
        self.description = description
        self.created_by = created_by
        self.state = state
        
    def __repr__(self):
        return f'<Todo {self.title}>'
        
    def __str__(self):
        return self.title
    
    