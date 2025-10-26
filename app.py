import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Importamos routes como un módulo (no sus variables)
import routes 

# 1. Instancias de Extensiones (SIN APLICACIÓN AÚN)
# Deben ser globales para que los modelos puedan importarlas.
db = SQLAlchemy()
migrate = Migrate()

# 2. FUNCIÓN FÁBRICA: Crea y configura la aplicación
def create_app():
    app = Flask(__name__)
    
    # Configuración de la aplicación
    # Render usará DATABASE_URL; tu local usará sqlite:///minicrud.db
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'mi_clave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///minicrud.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 3. Inicializar Extensiones CON la aplicación
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 4. Registrar Modelos y Rutas
    with app.app_context():
        # Importar los modelos para que SQLAlchemy los conozca
        import models
        # Registrar las rutas llamando a la función del módulo routes.py
        routes.register_routes(app, db) # <-- Solución final de la importación

    return app

# 5. Instancia Global para Gunicorn/Render
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