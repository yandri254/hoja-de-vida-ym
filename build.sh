#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== Instalando dependencias de Python ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== Instalando Node.js y npm ==="
# Render ya tiene Node.js instalado

echo "=== Construyendo frontend de React ==="
cd frontend
npm install
npm run build
cd ..

echo "=== Colectando archivos estáticos ==="
python manage.py collectstatic --no-input

echo "=== Ejecutando migraciones ==="
python manage.py migrate --no-input

echo "=== Poblando base de datos ==="
python populate_data.py

echo "=== Build completado ==="
