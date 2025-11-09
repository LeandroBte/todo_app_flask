# Contiene todas las vistas de tareas (maneja las listas de tareas) con blueprints

from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Todo
from flask_login import login_required, current_user

# Definir el Blueprint
bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/')
def index():
    todos = Todo.query.all()
    return render_template('todos.html', todos=todos)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        
        # Validación
        if not title:
            flash('El título es obligatorio', 'danger')
            return redirect(url_for('todo.create'))
            
        # Crear tarea
        todo = Todo(
            title=title, 
            description=description, 
            created_by=current_user.id,
            state=False
        )
        db.session.add(todo)
        db.session.commit()
        
        flash('Tarea creada exitosamente', 'success')
        return redirect(url_for('todo.index'))
    
    # Mostrar formulario de creación
    return render_template('task_form.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    todo = Todo.query.get_or_404(id)
    
    # Verificar que el usuario sea el autor
    if todo.created_by != current_user.id:
        flash('No tienes permiso para editar esta tarea', 'danger')
        return redirect(url_for('todo.index'))
    
    if request.method == 'POST':
        todo.title = request.form.get('title')
        todo.description = request.form.get('description')
        todo.state = 'state' in request.form
        
        db.session.commit()
        flash('Tarea actualizada exitosamente', 'success')
        return redirect(url_for('todo.index'))
    
    # Mostrar formulario de edición
    return render_template('task_form.html', todo=todo)

@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    todo = Todo.query.get_or_404(id)
    
    # Verificar que el usuario sea el autor
    if todo.created_by != current_user.id:
        flash('No tienes permiso para eliminar esta tarea', 'danger')
        return redirect(url_for('todo.index'))
    
    db.session.delete(todo)
    db.session.commit()
    flash('Tarea eliminada exitosamente', 'success')
    return redirect(url_for('todo.index'))

@bp.route('/change_state/<int:id>')
@login_required
def change_state(id):
    todo = Todo.query.get_or_404(id)
    
    # Verificar que el usuario sea el autor
    if todo.created_by != current_user.id:
        flash('No tienes permiso para modificar esta tarea', 'danger')
        return redirect(url_for('todo.index'))
    
    todo.state = not todo.state
    db.session.commit()
    
    status = 'completada' if todo.state else 'marcada como pendiente'
    flash(f'Tarea {status} exitosamente', 'success')
    return redirect(url_for('todo.index'))




