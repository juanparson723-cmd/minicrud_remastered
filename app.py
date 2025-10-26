import os
from flask import Flask
from flask_migrate import Migrate
from db import db  # importamos db desde un archivo separado (db.py)

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos
uri = os.getenv("DATABASE_URL", "sqlite:///local.db")

# Render a veces usa "postgres://" (obsoleto), lo convertimos a "postgresql://"
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos SQLAlchemy y Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)

# 👇 Importamos después de inicializar db
from routes import *
from models import *

# Crear tablas automáticamente si no existen
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return "Conexión a PostgreSQL en Render funcionando 🚀"


if __name__ == '__main__':
    app.run(debug=True)
