#!/usr/bin/env bash

# 1. Ejecuta la migración de la base de datos (crea la tabla Alumno)
echo "Ejecutando flask db upgrade..."
flask db upgrade

# 2. Inicia el servidor Gunicorn
echo "Iniciando servidor Gunicorn..."
gunicorn app:app