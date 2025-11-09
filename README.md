# 📝 Todo App

Una aplicación de lista de tareas (To-Do List) desarrollada con Flask que permite a los usuarios registrarse, iniciar sesión y gestionar sus tareas personales.

## 🚀 Características

- **Autenticación de usuarios**
  - Registro de nuevos usuarios
  - Inicio de sesión
  - Cierre de sesión

- **Gestión de tareas**
  - Crear nuevas tareas
  - Marcar tareas como completadas
  - Editar tareas existentes
  - Eliminar tareas
  - Ver lista de tareas pendientes

- **Interfaz intuitiva**
  - Diseño responsivo
  - Fácil de usar
  - Feedback visual para acciones del usuario

## 🛠️ Tecnologías utilizadas

- **Backend:**
  - Python 3.x
  - Flask (Framework web)
  - SQLAlchemy (ORM para base de datos)
  - Flask-Login (Manejo de autenticación)
  - Flask-WTF (Formularios web)
  - Flask-Bcrypt (Encriptación de contraseñas)

- **Frontend:**
  - HTML5
  - CSS3 (con Bootstrap para estilos)
  - JavaScript (para interacciones del lado del cliente)

- **Base de datos:**
  - SQLite (base de datos local)
  - Flask-Migrate (para migraciones de base de datos)

## 📦 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd todo_app
   ```

2. **Crear un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuración de la base de datos**
   ```bash
   # En Windows, usa 'set' en lugar de 'export'
   export FLASK_APP=run.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Iniciar la aplicación**
   ```bash
   flask run
   ```

6. **Abrir en el navegador**
   ```
   http://127.0.0.1:5000
   ```

## 🏗️ Estructura del proyecto

```
todo_app/
├── instance/
│   └── todolist.db       # Base de datos SQLite
├── todo/
│   ├── __init__.py       # Inicialización de la aplicación
│   ├── auth.py          # Rutas y lógica de autenticación
│   ├── models.py        # Modelos de la base de datos
│   ├── todo.py          # Rutas y lógica de la aplicación
│   └── templates/       # Plantillas HTML
│       ├── auth/        # Plantillas de autenticación
│       │   ├── login.html
│       │   └── register.html
│       ├── layout.html  # Plantilla base
│       ├── index.html   # Página de inicio
│       ├── todos.html   # Lista de tareas
│       └── task_form.html  # Formulario de tareas
├── requirements.txt     # Dependencias del proyecto
└── run.py              # Punto de entrada de la aplicación
```

## 🔒 Variables de entorno

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta_aqui
DATABASE_URL=sqlite:///todolist.db
```

## 📝 Uso

1. **Registra una nueva cuenta** en la ruta `/register`
2. **Inicia sesión** con tus credenciales en `/login`
3. **Crea nuevas tareas** usando el botón "Nueva Tarea"
4. **Marca tareas como completadas** haciendo clic en el checkbox
5. **Edita o elimina tareas** usando los botones correspondientes
6. **Cierra sesión** cuando hayas terminado

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

Desarrollado con ❤️ por Leandro Benitez
