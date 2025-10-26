from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import Alumno
# ⚠️ IMPORTANTE: Si tu archivo se llama forms.py, usa 'from forms import AlumnoForm'
from forms import AlumnoForm


# === 1. RUTAS DE AUTENTICACIÓN Y MENÚ ===

@app.route('/')
def home():  # Endpoint: 'home'
    # Redirige al login al entrar a la aplicación
    return redirect(url_for('login'))


@app.route('/login')
def login():  # Endpoint: 'login' <--- ¡IMPORTANTE!
    return render_template('login.html')


@app.route('/register')
def register():  # Endpoint: 'register' <--- ¡IMPORTANTE!
    return render_template('register.html')


# === 2. RUTA DEL PANEL DE ALUMNOS (CRUD Listado) ===

@app.route('/alumnos')
def index():  # Endpoint: 'index'
    alumnos = Alumno.query.all()
    # Usamos index.html para mostrar el listado de alumnos
    return render_template('index.html', alumnos=alumnos)


# === 3. RUTAS CRUD ===

@app.route('/crear', methods=['GET', 'POST'])
def crear():  # Endpoint: 'crear'
    form = AlumnoForm()
    if form.validate_on_submit():
        nuevo_alumno = Alumno(
            matricula=form.matricula.data,
            nombre=form.nombre.data,
            grupo=form.grupo.data
        )
        db.session.add(nuevo_alumno)
        db.session.commit()
        flash('Alumno creado con éxito!', 'success')
        # Redirige a la lista de alumnos
        return redirect(url_for('index'))
    return render_template('crear.html', form=form)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):  # Endpoint: 'editar'
    alumno = Alumno.query.get_or_404(id)
    form = AlumnoForm(obj=alumno)
    if form.validate_on_submit():
        form.populate_obj(alumno)
        db.session.commit()
        flash('Alumno actualizado con éxito!', 'success')
        # Redirige a la lista de alumnos
        return redirect(url_for('index'))
    return render_template('editar.html', form=form, alumno=alumno)


@app.route('/borrar/<int:id>')
def borrar(id):  # Endpoint: 'borrar'
    alumno = Alumno.query.get_or_404(id)
    db.session.delete(alumno)
    db.session.commit()
    flash('Alumno eliminado con éxito!', 'danger')
    # Redirige a la lista de alumnos
    return redirect(url_for('index'))


# from flask import render_template, request, redirect, url_for, flash
# from app import app, db
# from models import Alumno
# Asumimos que su archivo se llama forms.py
# from forms import AlumnoForm


# @app.route('/')
# def login_page():
    # Usamos la plantilla 'login.html' para forzar el inicio de sesión
    # return render_template('login.html')


# === 2. PANEL DE ALUMNOS (Nueva Ruta) ===
# La lista de alumnos ahora está en /alumnos
# @app.route('/alumnos')
# def panel_alumnos():
    # alumnos = Alumno.query.all()
    # Usa la plantilla index.html para mostrar la tabla de alumnos
    # return render_template('index.html', alumnos=alumnos)

# === 3. RUTAS CRUD (Manteniendo nombres cortos) ===

# @app.route('/crear', methods=['GET', 'POST'])
"""def crear():
    form = AlumnoForm()
    if form.validate_on_submit():
        nuevo_alumno = Alumno(
            matricula=form.matricula.data,
            nombre=form.nombre.data,
            grupo=form.grupo.data
        )
        db.session.add(nuevo_alumno)
        db.session.commit()
        flash('Alumno creado con éxito!', 'success')
        # Redirigir a la nueva ruta del panel
        return redirect(url_for('panel_alumnos'))
    return render_template('crear.html', form=form)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    alumno = Alumno.query.get_or_404(id)
    form = AlumnoForm(obj=alumno)
    if form.validate_on_submit():
        form.populate_obj(alumno)
        db.session.commit()
        flash('Alumno actualizado con éxito!', 'success')
        # Redirigir a la nueva ruta del panel
        return redirect(url_for('panel_alumnos'))
    return render_template('editar.html', form=form, alumno=alumno)


@app.route('/borrar/<int:id>')
def borrar(id):
    alumno = Alumno.query.get_or_404(id)
    db.session.delete(alumno)
    db.session.commit()
    flash('Alumno eliminado con éxito!', 'danger')
    # Redirigir a la nueva ruta del panel
    return redirect(url_for('panel_alumnos'))
"""
