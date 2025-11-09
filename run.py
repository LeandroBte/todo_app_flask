# Aquí solo se ejecuta la aplicacion (maneja la aplicacion)

from todo import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
