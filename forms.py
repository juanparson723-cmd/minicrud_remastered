# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class AlumnoForm(FlaskForm):
    # La matrícula debe ser requerida y tener una longitud mínima
    matricula = StringField('Matrícula', validators=[
                            DataRequired(), Length(min=1, max=20)])

    # El nombre debe ser requerido
    nombre = StringField('Nombre del Alumno', validators=[
                         DataRequired(), Length(min=2, max=100)])

    # El grupo debe ser requerido
    grupo = StringField('Grupo', validators=[
                        DataRequired(), Length(min=1, max=10)])

    submit = SubmitField('Guardar Alumno')  # Botón de envío
