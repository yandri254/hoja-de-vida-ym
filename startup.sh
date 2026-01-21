#!/bin/bash

# Script de inicio para Gunicorn en Azure
gunicorn --bind=0.0.0.0 --timeout 600 configuracion.wsgi
