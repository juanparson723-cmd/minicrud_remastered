from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# 🔑 Clave secreta requerida para formularios CSRF (puede ser cualquier string aleatorio)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mi_clave_secreta_segura')

uri = os.getenv("DATABASE_URL", "sqlite:///local.db")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importar rutas y modelos (coloca aquí tus imports para evitar bucles)
from models import *
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
