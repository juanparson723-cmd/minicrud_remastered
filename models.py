from app import db

class Alumno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    grupo = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Alumno {self.nombre}>'
