@echo off
title Servidor Bomberos B-120
cd /d "%~dp0backend"
echo Iniciando servidor Django...
echo Accede en: http://127.0.0.1:8000/
echo Para detener: presiona CTRL+C
echo.
venv\Scripts\python.exe manage.py runserver
pause
