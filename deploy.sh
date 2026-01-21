#!/bin/bash

# ----------------------
# Script de Despliegue para Azure App Service
# ----------------------

set -e

echo "=== Iniciando despliegue ==="

# 1. Instalar dependencias de Python
echo "=== Instalando dependencias de Python ==="
python -m pip install --upgrade pip
pip install -r requirements.txt

# 2. Construir el frontend de React
echo "=== Construyendo frontend de React ==="
cd frontend
npm install
npm run build
cd ..

# 3. Colectar archivos estáticos de Django
echo "=== Colectando archivos estáticos ==="
python manage.py collectstatic --noinput

# 4. Ejecutar migraciones de base de datos
echo "=== Ejecutando migraciones ==="
python manage.py migrate --noinput

echo "=== Despliegue completado ==="
