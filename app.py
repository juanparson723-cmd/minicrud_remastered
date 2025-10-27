import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# ¡NO importar models ni routes aquí!

# 1. Instancias Globales de Extensiones (SIN app)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # 2. Instancia de Flask y Configuración
    app = Flask(__name__)
    
    # Configuración: Usa DATABASE_URL de Render, o SQLite local
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'mi_clave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///minicrud.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 3. Inicializar Extensiones CON la aplicación (Vinculación)
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 4. Registrar Modelos y Rutas
    with app.app_context():
        import models # Registra modelos para db.create_all() y migraciones
        from models import Alumno # Obtenemos la clase Alumno
        import routes 
        
        # 🚨 Pasamos Alumno como argumento para romper el ciclo
        routes.register_routes(app, db, Alumno) 
        
        # Crear tablas (Necesario si no usas migraciones o si es la primera vez)
        db.create_all()

    return app

# 5. Instancia Global (Gunicorn/Render llama a esta variable)
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)





"""from flask import Flask
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
    app.run(debug=True)"""